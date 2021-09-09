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
from ..model.hello_world_model import Hello

# Get the logger
LOGGER = get_module_logger()


def say_hello(name=None):
    """
    An example service function that says hello
    :param name: A name to say hello to, defaults to 'World'
    :return: dict {'message': <response>}
    """
    name = name or 'World'
    LOGGER.warning("Started saying hello to: %s", name)
    SESSION.add(Hello(who=name, when=dt.datetime.now()))
    SESSION.commit()
    LOGGER.warning("Said hello to: %s", name)
    return {"message": "Hello {}!".format(name if name else "World")}
