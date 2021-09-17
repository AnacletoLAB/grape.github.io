
"""
    The controller for methods
"""
#pylint: disable=R0201
from flask_restx import Resource, Namespace
from ..service.entity_service import fetch_method

NS = Namespace('entity', description='The entity endpoint', path="/entity")

@NS.route('/method')
class MethodControllerList(Resource):
    """ FlaskRestx uses these docstrings """
    def get(self):
        """
            Get all methods
        """
        return []

@NS.route('/method/<method_id>/<version_id>')
@NS.param('method_id', "The id of the method")
@NS.param('version_id', "The id of the version")
class MethodController(Resource):
    """ FlaskRestx uses these docstrings """
    def get(self, method_id, version_id):
        """
            Get a method by method id from a particular version
        """
        return fetch_method(method_id, version_id)
