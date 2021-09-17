"""
Base exceptions namespace for the app
"""
from werkzeug.exceptions import HTTPException
from src.utils.logging import get_module_logger

LOGGER = get_module_logger()


class GrapeBaseException(HTTPException):
    """
    Base exception for the grape app
    """

    message = "Oops! Something went wrong and we couldn't process your request."
    detail = "This response means we couldn't generate a more specific error. Please" \
             "try again, but if the problem persists contact an application " \
             "administrator."

class GrapeException(GrapeBaseException, HTTPException):

    message = "Oops! Something went wrong and we couldn't process your request."
    detail = "This response means we couldn't generate a more specific error. Please" \
             "try again, but if the problem persists contact an application " \
             "administrator."
