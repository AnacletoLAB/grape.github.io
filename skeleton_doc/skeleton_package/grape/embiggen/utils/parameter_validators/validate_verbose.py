import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def validate_verbose(candidate_verbose: typing.Union[bool, int]) -> bool:
    """Return validated verbose candidate, raising a meaningful error otherwise.

    Parameters
    -----------------
    candidate_verbose: Union[bool, int],
        The candidate verbose value to validate.

    Raises
    -----------------
    ValueError,
        If the provided verbose parameter is not within
        the allowed set of values.

    Returns
    -----------------
    The validated value.
    """
