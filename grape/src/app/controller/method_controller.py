
"""
    The controller for methods
"""
from flask_restx import Resource, Namespace
from src.utils.exceptions import ImATeapotException
from ..service.entity_service import say_hello




NS = Namespace('entity', description='The entity endpoint', path="/entity")

@NS.route('/method')
class MethodController(Resource):
    """ FlaskRestx uses these docstrings """

    @staticmethod
    def get():
        """
        TODO: Pagination here.
        return all methods
        """
        return say_hello(), 200

    @NS.route("/<method_id>")
    def get():
        """
            return the method with method_id for the newest
            should be a complex method with all params and args and types
        """
        return None

    @NS.route("/<method_id>/<version_id>")
    def get():
        """
            return the method with a particular version
        """
        return None