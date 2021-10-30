import faiss
import mxnet as mx
import numpy as np
from gluoncv.model_zoo import get_model
from PIL import Image

from torchreid.utils import FeatureExtractor

from collections import OrderedDict
import pickle
import heapq

import cv2 as cv


def extract_feature(img, extractor):
    features = extractor(img)
    features = features[0].reshape((1, 2048))
    print(features.shape) # output (5, 512)
    return features


def init_index():
    resize_dim = (64, 128)
    num_features = 300

    index_cluster = Cluster()
    Cluster.init_finder(num_features, resize_dim)

    path = 'test_faiss/test1.jpg'
    img = np.array(Image.open(path))
    index_cluster.append(path, img)
    
    index = FaissIndex(index_cluster)
    return index


class Cluster(OrderedDict):
    @classmethod
    def init_finder(cls, num_features, resize_dim):
        cls.finder = cv.HOGDescriptor()
        # cv.ORB_create(num_features, scoreType=cv.ORB_FAST_SCORE)
        cls.resize_dim = resize_dim

    def append(self, path: str, image: np.ndarray):
        _, desc = Cluster.calculate(image)
        self[path] = desc
        return desc

    @classmethod
    def calculate(cls, image):
        image_o = image.astype(np.uint8)
        image = cv.resize(image_o, cls.resize_dim)

        if image.ndim == 2:
            gray_image = image
        else:
            gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        des = cls.finder.compute(gray_image)

        finder_feature = np.float32(des).reshape((945, 4))
        print(finder_feature.shape)
        return 0, finder_feature


class FaissIndex:
    def __init__(self, index_cluster, index=None, index_dict=None):
        if isinstance(index, str):
            index = faiss.read_index(index)

        if isinstance(index_dict, str):
            with open(index_dict, 'rb') as f:
                index_dict = pickle.load(f)

        cuda = False
        index_key = 'IDMap,Flat'
        finder_dim = 4

        self.temp_memory = 400 * 1024 * 1024

        if index is None or index_dict is None:
            index, index_dict, res = self.train_index(finder_dim, index_key, index_cluster, cuda)

        self.index = index
        self.index_dict = index_dict
        self.similarity = 100

    def append(self, path, image):
        _, feature = Cluster.calculate(image)
        new_id = max(faiss.vector_to_array(self.index.id_map)) + 1
        ids_list = np.linspace(new_id, new_id, num=feature.shape[0], dtype='int64')

        self.index.add_with_ids(feature, ids_list)
        self.index_dict[new_id] = path

        return new_id

    def remove_with_ids(self, ids):
        # cpu only
        self.index.remove_ids(np.array([ids]))
        self.index_dict.pop(ids, None)

    def search_by_ids(self, ids, k):
        vectors = [self._id_to_vector(id_)[1] for id_ in ids]
        results = self.__search__(ids, vectors, k + 1)

        return results

    def find_by_image(self, image, k):
        ids = [None]
        _, vectors = Cluster.calculate(image)
        results = self.__search__(ids, [vectors], k)

        return results

    def find_by_image_closest(self, image):
        ids = [None]
        _, vectors = Cluster.calculate(image)
        result = self.__search__(ids, [vectors], 1)
        if result[0]['neighbors']:
            path = result[0]['neighbors'][0]['file_path']
            score = result[0]['neighbors'][0]['score']
        else:
            path, score = None, None
        return path, score

    def __search__(self, ids, vectors, topN):
        def neighbor_dict_with_path(id_, file_path, score):
            return {'id': int(id_), 'file_path': file_path, 'score': score}

        def neighbor_dict(id_, score):
            return {'id': int(id_), 'score': score}

        def result_dict_str(id_, neighbors):
            return {'id': id_, 'neighbors': neighbors}

        results = []
        need_hit = self.similarity

        for id_, feature in zip(ids, vectors):
            _, neighbors = self.index.search(feature, k=topN) if feature.size > 1 else ([], [])

            if isinstance(neighbors, list):
                continue

            n, _ = neighbors.shape
            result_dict = {}

            for i in range(n):
                l = np.unique(neighbors[i]).tolist()
                for r_id in l:
                    if r_id == -1:
                        continue
                    score = result_dict.get(r_id, 0)
                    score += 1
                    result_dict[r_id] = score

            h = []
            for k in result_dict:
                v = result_dict[k]
                if v < need_hit:
                    continue
                if len(h) < topN:
                    heapq.heappush(h, (v, k))
                else:
                    heapq.heappushpop(h, (v, k))

            result_list = heapq.nlargest(topN, h, key=lambda x: x[0])
            neighbors_scores = []
            for result in result_list:
                confidence = result[0] * 100 / n
                if self.index_dict:
                    file_path = self._id_to_vector(result[1])
                    neighbors_scores.append(neighbor_dict_with_path(result[1], file_path, str(confidence)))
                else:
                    neighbors_scores.append(neighbor_dict(result[1], str(confidence)))
            results.append(result_dict_str(id_, neighbors_scores))
        return results

    def reset_gpu(self):
        self.index.reset()

    def _id_to_vector(self, id_):
        return self.index_dict[id_]

    def train_index(self, finder_dim, index_key, cluster, cuda):
        index = faiss.index_factory(finder_dim, index_key)

        if cuda:
            res = faiss.StandardGpuResources()
            res.setTempMemory(self.temp_memory)
            index = faiss.index_cpu_to_gpu(res, 0, index)
        else:
            res = None

        ids_count = 0
        index_dict = {}
        ids = None
        features = np.array([])
        for path, feature in cluster.items():
            if feature.any():
                image_dict = {ids_count: path}
                index_dict.update(image_dict)
                ids_list = np.linspace(ids_count, ids_count, num=feature.shape[0], dtype='int64')
                ids_count += 1
                if features.any():
                    features = np.vstack((features, feature))
                    ids = np.hstack((ids, ids_list))
                else:
                    features = feature
                    ids = ids_list

        if features.any():
            if not index.is_trained and index_key != 'IDMap,Flat':
                index.train(features)
            # features = features.reshape((16, 32))
            # print(features.shape)
            # print('___')
            # ids = ids.reshape((16, 32))
            # print(ids.shape)
            index.add_with_ids(features, ids)

        return index, index_dict, res