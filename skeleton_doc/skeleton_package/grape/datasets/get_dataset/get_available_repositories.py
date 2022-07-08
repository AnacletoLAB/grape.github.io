import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_available_repositories() -> List:
    """Return list of available repositories."""
