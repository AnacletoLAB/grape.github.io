from typing import *


def tensorflow_version_is_higher_or_equal_than(tensorflow_version: str) -> bool:
    """Returns boolean if the TensorFlow version is higher than provided one.

    Parameters
    ----------------------
    tensorflow_version: str,
        The version of TensorFlow to check against.

    Raises
    ----------------------
    ValueError,
        If the provided version code is not a valid one.

    Returns
    ----------------------
    Boolean representing if installed TensorFlow version is higher than given one.
    """
