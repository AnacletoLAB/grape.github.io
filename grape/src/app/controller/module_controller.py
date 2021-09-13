"""
    The controller for modules
"""
from flask_restx import Resource, Namespace
from src.utils.exceptions import ImATeapotException
from ..service.entity_service import say_hello




NS = Namespace('entity', description='The entity endpoint', path="/entity")


@NS.route('/module')
class ModuleController(Resource):
    """ Flask Restplus uses these docstrings """

    @staticmethod
    def get():
        """
        The first line provides a short description
        The following lines are shown on detail expansion and follow
        exactly the spacing and newlines defined in this comment.
        """
        return say_hello(), 200
