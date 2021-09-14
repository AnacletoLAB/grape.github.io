import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_available_gpus_number() -> int:
    """Return whether GPUs can be detected."""
