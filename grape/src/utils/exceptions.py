"""
Base exceptions namespace for the app
"""
from werkzeug.exceptions import HTTPException

from src.utils.logging import get_module_logger

LOGGER = get_module_logger()


class GrapeException(Exception):
    """
    Base exception for the grape app
    """

    message = "Oops! Something went wrong and we couldn't process your request."
    detail = "This response means we couldn't generate a more specific error. Please" \
             "try again, but if the problem persists contact an application " \
             "administrator."
    @classmethod
    def restful_handler(cls, message=None):
        """
        This handler gets attached to flask-restplus as an errorhandler when then
        register_all_exceptions function of the src.app.controller.utils
        errorhandlers namespace is called.
        Must be named 'restful_handler'
        :param message: Message from the exception e.g. `ThisException('My Message')`
        """
        message = message or cls.message
        LOGGER.info("Using handler for error %s - %s", cls.__name__, message)
        return {'message': message, 'detail': cls.detail}



class ImATeapotException(GrapeException, HTTPException):
    """
    Example exception demonstrating flask-restplus api errorhandler
    """
    message = 'Short and Stout'
    @classmethod
    def restful_handler(cls, message=None):
        """
        This handler gets attached to flask-restplus as an errorhandler when then
        register_all_exceptions function of the src.app.controller.utils
        errorhandlers namespace is called.
        Must be named 'restful_handler'
        :param message:
        """
        message = message or cls.message
        LOGGER.info("Using handler for error %s - %s", cls.__name__, message)
        return {'message': message}, 418
