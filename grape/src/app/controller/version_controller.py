
"""
    The controller for methods
"""
from flask_restx import Resource, Namespace
from src.utils.exceptions import ImATeapotException
from ..service.entity_service import say_hello




NS = Namespace('entity', description='The entity endpoint', path="/entity")

@NS.route('/version')
class MethodController(Resource):
    """ FlaskRestx uses these docstrings """

    @staticmethod
    def get():
        """
        return all versions
        """
        return say_hello(), 200