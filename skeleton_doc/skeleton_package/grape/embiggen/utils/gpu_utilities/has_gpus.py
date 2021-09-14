import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def has_gpus() -> bool:
    """Return whether GPUs can be detected."""
