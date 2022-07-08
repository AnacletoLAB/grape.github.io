import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def validate_graph_version(name: str, repository: str, version: str):
    """Validates given triple.

    Parameters
    ----------------------
    name: str,
        The name of the graph to retrieve.
    repository: str,
        The name of the repository to retrieve the graph from.
    version: str,
        The version to check for.

    Raises
    ----------------------
    ValueError,
        If the given repository is not available.
    """
