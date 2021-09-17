"""
    The controller for modules
"""
#pylint: disable=R0201
from flask_restx import Resource, Namespace

NS = Namespace('entity', description='The entity endpoint', path="/entity")

@NS.route('/module')
class ModuleController(Resource):
    """ FlaskRestx uses these docstrings """
    def get(self):
        """
            return all modules
        """
        return 200
