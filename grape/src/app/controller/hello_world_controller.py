"""
An example controller
"""
from flask_restx import Resource, Namespace


from src.utils.exceptions import ImATeapotException

from ..service.hello_world_service import say_hello




NS = Namespace('hello', description='The hello endpoint')


@NS.route('/sayhello')
class HelloWorld(Resource):
    """ Flask Restplus uses these docstrings """

    @staticmethod
    def get():
        """
        The first line provides a short description
        The following lines are shown on detail expansion and follow
        exactly the spacing and newlines defined in this comment.
        """
        return say_hello(), 200


@NS.route('/brewcoffee')
class BrewCoffee(Resource):
    """ Flask Restplus uses these docstrings """

    @staticmethod
    def get():
        """
        Ask the system to brew a cup of coffee
        This will clearly fail because the system is not a coffeemaker

        :raises ImATeapotException: If asked to brew coffee
        """
        raise ImATeapotException("Tea isn't coffee")
