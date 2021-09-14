import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_available_gpus() -> List:
    """Return list with IDs of available GPU devices."""
