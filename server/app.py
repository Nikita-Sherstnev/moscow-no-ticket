from threading import Thread

from flask import Flask
from flask_restful import Resource, Api

from api import face_detect
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'It':'works'}

api.add_resource(HelloWorld, '/')
api.add_resource(face_detect.FaceDetection, '/detect')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
