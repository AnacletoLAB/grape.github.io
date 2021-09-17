
"""
    The controller for methods
"""
#pylint: disable=R0201
from flask_restx import Resource, Namespace

NS = Namespace('entity', description='The entity endpoint', path="/entity")

@NS.route('/class')
class ClassControllerList(Resource):
    """
        Get all classes
    """
    @NS.doc('get_classes')
    def get(self):
        """
            return all classes from all modules with methods
        """
        return []

@NS.route('/class/<class_id>')
@NS.param('class_id', 'The class identifier')
class ClassController(Resource):
    """
        Get a class by class id.
    """
    def get(self,class_id):
        """
            return a very specific class with much detail about its methods
        """
        return class_id
