from functools import wraps

from flask import jsonify, current_app, Response
from flask_restful import Resource, Api, reqparse

from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions


def marshal_response(f):
    """
    Adds `result` field to the response.
    Wraps response object in `data` field.
    Keeps response structure consistent.
    """

    @wraps(f)
    def api_method(*args, **kwargs):
        response = f(*args, **kwargs)
        if isinstance(response, Response):
            return response
        if response is None:
            return {'result': True}
        return {'result': True, 'data': response}
    return api_method


class BaseApi(Api):
    """
    Registers `flask_restful`.
    Saves Flask default exception handlers
    and wraps the in `ExceptionHandler`.
    """

    def init_app(self, app):
        super().init_app(app)

    def add_resource(self, resource, *urls, **kwargs):
        """
        Adds a resource to the API via provided link.
        See: `flask_restful.Api.add_resource`.
        Overriden to add a AMPQ uri to a resource
        """

        resource_class_args = kwargs.pop('resource_class_args', ())
        resource_class_kwargs = kwargs.pop('resource_class_kwargs', {})
        resource_class_kwargs['config'] = self.app.config

        super().add_resource(resource, *urls,
                             resource_class_args=resource_class_args,
                             resource_class_kwargs=resource_class_kwargs)


class ApiResource(Resource):
    """
    Base resourse class.
    Marshals everything with `marshal_response`.
    """

    method_decorators = [marshal_response]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)