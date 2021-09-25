import time
from datetime import datetime
import random

from facenet_pytorch import MTCNN
import torch
from PIL import Image
import base64

from api import base
from flask import jsonify

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


class FaceDetection(base.ApiResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        mtcnn = MTCNN(keep_all=True, device=device)

        with Image.open("screen.jpg") as frame:
            coords = detect_faces_on_frame(frame, mtcnn)

        with open("screen.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        clients = list()

        for idx, coord in enumerate(coords):
            clients.append({'id': idx, 'coords': coord.tolist(), 'datetime': random_date("1/1/2018 1:30 PM", "1/1/2022 4:50 AM", random.random()), 'rating': random.uniform(1, 5)})

        return {'clients': clients, 'source_image_base_64': encoded_string.decode('utf-8')}

    def post(self):
        return self._dataset()
