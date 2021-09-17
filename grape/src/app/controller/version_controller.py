
"""
    The controller for methods
"""
#pylint: disable=R0201
from flask_restx import Resource, Namespace

NS = Namespace('entity', description='The entity endpoint', path="/entity")

@NS.route('/version')
class MethodController(Resource):
    """ FlaskRestx uses these docstrings """

    @staticmethod
    def get():
        """
            return all versions
        """
        return 200
