"""
The root of the API Blueprint code
"""

from flask_restx import Api
from flask import Blueprint

from .schemas import register_all_schemas
from .utils.errorhandlers import register_all_exceptions


from .method_controller import NS as method_ns
from .module_controller import NS as module_ns

API_BLUEPRINT = Blueprint('api', __name__)
DESCRIPTION = 'A Flask Service for GRAPE application documentation sweet'
API = Api(API_BLUEPRINT,
          title='grape',
          version='0.0.1',
          description=DESCRIPTION,

          )
API = register_all_schemas(API)
API = register_all_exceptions(API)


API.add_namespace(method_ns)
API.add_namespace(module_ns)