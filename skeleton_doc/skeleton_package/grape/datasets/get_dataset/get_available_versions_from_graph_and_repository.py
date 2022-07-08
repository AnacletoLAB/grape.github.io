import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_available_versions_from_graph_and_repository(name: str, repository: str) -> List:
    """Return list of available graphs from the given repositories.

    Parameters
    ----------------------
    name: str,
        The name of the graph to retrieve.
    repository: str,
        The name of the repository to retrieve the graph from.

    Raises
    ----------------------
    ValueError,
        If the given repository is not available.
    """
