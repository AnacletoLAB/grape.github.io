"""
A hello world example service
"""
# This next line disables checking that instance of 'scoped_session'
# has no 'commit' or 'bulk_save_objects' members, The members are there,
# pylint just can't tell
#
# pylint: disable=E1101
from src.utils.logging import get_module_logger
from ..model import SESSION
from ..model.method_model import MethodModel
from ..model.class_model import ClassModel

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
        return SESSION.query(MethodModel).filter(MethodModel.method_id == method_id,
        MethodModel.version_id == version_id)
    ## Get more complex and fetch types and arguments
    return SESSION.query(MethodModel).filter(MethodModel.method_id == method_id)

def fetch_classes_list(module_id=None):
    """
     A service method to fetch all classes for a specific module.
    """
    if module_id is not None:
        return SESSION.query(ClassModel).filter(ClassModel.module_id == module_id)
    return []
