import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def has_rocm_drivers() -> bool:
    """Return whether ROCM drivers can be detected."""
