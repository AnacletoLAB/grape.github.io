import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def tensorflow_version_is_less_or_equal_than(tensorflow_version: str) -> bool:
    """Returns boolean if the TensorFlow version is less or equal than provided one.

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
    Boolean representing if installed TensorFlow version is less or equal than given one.
    """
