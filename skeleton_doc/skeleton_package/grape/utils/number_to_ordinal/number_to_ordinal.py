import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def number_to_ordinal(number: int) -> str:
    """Returns the string ordinal curresponding to the provided number."""
