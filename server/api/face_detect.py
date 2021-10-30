import os
import io
import time
import random
from threading import Thread

import cv2
import gluoncv
import mxnet
import numpy
from facenet_pytorch import MTCNN
import torch
from PIL import Image
import base64

from api import base
import csv
from gluoncv import data, model_zoo, utils
from matplotlib import pyplot as plt
from mxnet import autograd, gluon

from nn.MTCNN import detect_faces_on_frame


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


def video_analyzer_thread():
    print('Start new video analyzer')
    classes = ['person']
    net = model_zoo.get_model('ssd_512_resnet50_v1_coco', pretrained=True)
    # train(net)
    net.reset_class(classes=classes, reuse_weights=classes)

    vidcap = cv2.VideoCapture('bus.avi')
    time.sleep(1)  ### letting the camera autofocus
    success, image = vidcap.read()

    count_skip = 6

    while success:
        cv2.imwrite("frame.jpg", image)
        x, image = data.transforms.presets.ssd.load_test("frame.jpg", short=512)
        class_IDs, scores, bounding_boxes = net(x)

        # ## (4) Display
        # for i in range(len(scores[0])):
        #   #print(class_IDs.reshape(-1))
        #   #print(scores.reshape(-1))
        #   cid = int(class_IDs[0][i].asnumpy())
        #   cname = net.classes[cid]
        #   score = float(scores[0][i].asnumpy())
        #   if score < 0.5:
        #     break
        #   x,y,w,h = bbox = bounding_boxes[0][i].astype(int).asnumpy()
        #   print(cid, score, bbox)
        #   tag = "{}; {:.4f}".format(cname, score)
        #   cv2.rectangle(img, (x,y), (w, h), (0, 255, 0), 2)
        #   cv2.putText(img, tag, (x, y-20),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 1)

        # cv2_imshow(img);
        # plt.cla()
        ax = utils.viz.plot_bbox(image, bounding_boxes[0], scores[0],
                                 class_IDs[0], class_names=net.classes)
        # plt.pause(0.0001)
        im = Image.open(r"frame.jpg")
        scale = 512 / (im.height if im.height < im.width else im.width)

        first_validator = [584, 63, 628, 128]
        second_validator = [685, 244, 750, 425]
        all_boxes = numpy.array([first_validator, second_validator])

        for i, bbox in enumerate(all_boxes):
            xmin, ymin, xmax, ymax = [int(x * scale) for x in bbox]
            rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                                 ymax - ymin, fill=False,
                                 edgecolor=(0.4, 0.8, 0.3),
                                 linewidth=3)
            ax.add_patch(rect)

        print('Read a new frame: ', success)
        plt.show()
        # Size of the image in pixels (size of original image)
        # (This is not mandatory)
        width, height = im.size

        srcs = scores[0].asnumpy()

        for i, bbox in enumerate(bounding_boxes[0].asnumpy()):
            if srcs.flat[i] < 0.5:
                continue

            xmin, ymin, xmax, ymax = [int(x) for x in bbox]
            left = xmin
            top = ymin
            right = xmax
            bottom = ymax

            # Cropped image of above dimension
            # (It will not change original image)

            scaled_width = int(im.width * scale)
            scaled_height = int(im.height * scale)

            scaled_im = im.resize((scaled_width, scaled_height))
            cropped_im = scaled_im.crop((left, top, right, bottom))

            # TODO To vector (cropped_im)
            # Shows the image in image viewer
            # im1.show()

        for i in range(count_skip):
            success, image = vidcap.read()
    print('Done')


class FaceDetection(base.ApiResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        mtcnn = MTCNN(keep_all=True, device=device)

        with open("screen.jpg", "rb") as image_file:
            img_bytes = image_file.read()
            encoded_string = base64.b64encode(img_bytes)
            frame = Image.open(io.BytesIO(img_bytes))

        coords = detect_faces_on_frame(frame, mtcnn)

        clients = list()

        for idx, coord in enumerate(coords):
            clients.append({'id': idx, 'coords': coord.tolist(), 'datetime': random_date("1/1/2018 1:30 PM", "1/1/2022 4:50 AM", random.random()), 'rating': random.uniform(1, 5)})

        return {'clients': clients, 'source_image_base_64': encoded_string.decode('utf-8')}

    def post(self):
        return self._dataset()
