import os, zipfile
from gluoncv import utils
import mxnet as mx
import numpy as np
from matplotlib import pyplot as plt

def write_line(img_path, im_shape, boxes, ids, idx):
    h, w, c = im_shape
    # for header, we use minimal length 2, plus width and height
    # with A: 4, B: 5, C: width, D: height
    A = 4
    B = 5
    C = w
    D = h
    # concat id and bboxes
    labels = np.hstack((ids.reshape(-1, 1), boxes)).astype('float')
    # normalized bboxes (recommanded)
    labels[:, (1, 3)] /= float(w)
    labels[:, (2, 4)] /= float(h)
    # flatten
    labels = labels.flatten().tolist()
    str_idx = [str(idx)]
    str_header = [str(x) for x in [A, B, C, D]]
    str_labels = [str(x) for x in labels]
    str_path = [img_path]
    line = '\t'.join(str_idx + str_header + str_labels + str_path) + '\n'
    return line

if __name__ == "__main__":
    img = mx.image.imread('frame.jpg')
    ax = utils.viz.plot_image(img)
    print(img.shape)
    plt.show()

    first_validator = [584, 63, 628, 128]
    second_validator = [685, 244, 750, 425]
    all_boxes = np.array([first_validator, second_validator])
    all_ids = np.array([0, 0])
    class_names = ['validator']

    # see how it looks by rendering the boxes into image
    ax = utils.viz.plot_bbox(img, all_boxes, labels=all_ids, class_names=class_names, linewidth=1)
    plt.show()

    with open('validators.lst', 'w') as fw:
        for i in range(4):
            line = write_line('./train/frame.jpg', img.shape, all_boxes, all_ids, i)
            print(line)
            fw.write(line)
