"""
The root of the API Blueprint code
"""

from flask_restx import Api
from flask import Blueprint

from .schemas import register_all_schemas
from .utils.errorhandlers import register_all_exceptions


from .hello_world_controller import NS as hello_ns

API_BLUEPRINT = Blueprint('api', __name__)
DESCRIPTION = 'A Flask Service for GRAPE application documentation sweet'
API = Api(API_BLUEPRINT,
          title='grape',
          version='0.0.1',
          description=DESCRIPTION,

          )
API = register_all_schemas(API)
API = register_all_exceptions(API)


API.add_namespace(hello_ns)
