"""
The root of the API Blueprint code
"""
from flask_restx import Api
from flask import Blueprint
from src.utils.exceptions import GrapeBaseException, GrapeException
from .schemas import register_all_schemas
from .class_controller import NS as class_namespace
from .method_controller import NS as method_namespace
from .version_controller import NS as version_namespace
from .module_controller import NS as module_namespace

API_BLUEPRINT = Blueprint('api', __name__)
DESCRIPTION = 'A Flask Service for GRAPE application documentation sweet'
API = Api(API_BLUEPRINT,
          title='grape',
          version='0.0.1',
          description=DESCRIPTION,
          )
API = register_all_schemas(API)

API.add_namespace(class_namespace)
API.add_namespace(method_namespace)
API.add_namespace(version_namespace)
API.add_namespace(module_namespace)


@API.errorhandler(GrapeException)
def grape_restful_handler(cls, message=None):
    """
    This handler gets attached to flask-restplus as an errorhandler when then
    register_all_exceptions function of the src.app.controller.utils
    errorhandlers namespace is called.
    Must be named 'restful_handler'
    :param message: Message from the exception e.g. `ThisException('My Message')`
    """
    message = message or cls.message
    return {'message': message, 'detail': cls.detail}

@API.errorhandler(GrapeBaseException)
def base_restful_handler(cls, message=None):
    """
    This handler gets attached to flask-restplus as an errorhandler when then
    register_all_exceptions function of the src.app.controller.utils
    errorhandlers namespace is called.
    Must be named 'restful_handler'
    :param message: Message from the exception e.g. `ThisException('My Message')`
    """
    message = message or cls.message
    return {'message': message, 'detail': cls.detail}
