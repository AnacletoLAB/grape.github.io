"""
Flask restplus error handlers
"""
import sys
import inspect
from src.utils.logging import get_module_logger

LOGGER = get_module_logger()


def register_all_exceptions(api):
    """
    Register restful-handles (if they exist) on all exceptions in
    src.utils.exceptions
    :param api: The API Object from Flask-RESTplus
    :return: The API Object with error handlers registered
    """
    clsmembers = inspect.getmembers(sys.modules['src.utils.exceptions'], inspect.isclass)
    for _, cls in clsmembers:
        restful_handler = getattr(cls, "restful_handler", None)
        if callable(restful_handler):
            api.errorhandler(cls)(restful_handler)
    return api
