import os
from datetime import datetime

from flask import make_response
from werkzeug.datastructures import FileStorage

from facenet_pytorch import MTCNN
import torch
import numpy as np
import mmcv, cv2
from PIL import Image

from api import base

from nn.MTCNN import detect_faces_on_frame


class FaceDetection(base.ApiResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        mtcnn = MTCNN(keep_all=True, device=device)

        with Image.open("screen.jpg") as frame:
            coords = detect_faces_on_frame(frame, mtcnn)
        
        l_coords = list()
        for coord in coords:
            l_coords.append(coord.tolist())

        dt = str(datetime(year=2021, month=9, day=11, hour=14))

        return {'coords': l_coords, 'datetime': dt}

    def post(self):
        return self._dataset()