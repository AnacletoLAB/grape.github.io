import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def has_single_gpu() -> bool:
    """Return whether there is only a GPU available."""
