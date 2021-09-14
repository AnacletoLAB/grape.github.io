from typing import *


def must_have_tensorflow_version_higher_or_equal_than(tensorflow_version: str= None, feature_name: str):
    """Returns boolean if the TensorFlow version is higher than provided one.

    Parameters
    ----------------------
    tensorflow_version: str,
        The version of TensorFlow to check against.
    feature_name: str = None,
        The name of the feature that the requested version of TensorFlow
        has and previous version do not have.

    Raises
    ----------------------
    ValueError,
        If the provided version code is not a valid one.
    ValueError,
        If the installed TensorFlow version is lower than requested one.
    """
