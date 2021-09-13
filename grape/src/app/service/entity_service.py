"""
A hello world example service
"""
# This next line disables checking that instance of 'scoped_session'
# has no 'commit' or 'bulk_save_objects' members, The members are there,
# pylint just can't tell
#
# pylint: disable=E1101

import datetime as dt
from src.utils.logging import get_module_logger

from ..model import SESSION
from ..model.module_model import Method

# Get the logger
LOGGER = get_module_logger()


def fetch_method(method_id=None, version_id=None):
    """
    A service method to fetch details about a particular method
    :param method_id: the id of the method
    :param version_id: a specific version of the id to look at.
    :return: ???
    """
    if version_id is not None:
        ## Get more complex and fetch types and arguments
        return SESSION.query(Method).filter(Method.method_id == method_id, Method.version_id == version_id)
    else:
         ## Get more complex and fetch types and arguments
        return SESSION.query(Method).filter(Method.method_id == method_id)

def fetch_modules(module_id=None, extras=None):
    """
    A service method to fetch details about a particular method
    :param method_id: the id of the method
    :param version_id: a specific version of the id to look at.
    :return: ???
    """
    if extras is not None:
        ## Get all the modules and all the methods for those modules?
        return SESSION.query(Method).filter(Method.method_id == method_id, Method.version_id == version_id)
    return None