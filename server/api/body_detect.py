from api import base

from person_re_id import init_index


class BodyDetection(base.ApiResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        init_index()
        return None
