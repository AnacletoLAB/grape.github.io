import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def has_nvidia_drivers() -> bool:
    """Return whether NVIDIA drivers can be detected."""
