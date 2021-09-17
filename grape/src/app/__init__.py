"""
Factory that includes the api blueprint
"""
from flask import redirect
from flask_migrate import Migrate

from src import factory
from .controller import API_BLUEPRINT



def _root():  # pylint: disable=W0612
    """ Redirect the root endpoint to the api blueprint """
    return redirect('/api')


def create_app(config_name=None, app=None, config_object=None):
    """
    Create the app with the api blueprint registered
    :param config_name:
    :param app:
    :param config_object:
    :return:
    """
    app = factory.create_app(config_name, app, config_object)

    # Register blueprints, try is incase the blueprint has
    # already been registered on existing app instance
    try:
        app.register_blueprint(API_BLUEPRINT, url_prefix='/api')
        app.add_url_rule('/', 'index', _root)
    except (ValueError, AssertionError):
        pass


    @app.route('/')
    def root():  # pylint: disable=W0612
        """ Redirect the root endpoint to the api blueprint """
        return redirect('/api')

    return app
