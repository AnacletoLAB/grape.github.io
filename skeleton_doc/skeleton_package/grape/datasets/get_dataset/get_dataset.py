import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_dataset(name: str, repository: typing.Optional[str], version: typing.Optional[str]) -> Callable:
    """Return the graph curresponding to the given graph name, repository and version.

    Parameters
    ----------------------
    name: str = None
        The name of the graph to retrieve.
    repository: Optional[str] = None
        The name of the repository to retrieve the graph from.
        This is needed only when there is not an unique graph name for the
        provided graph.
    version: Option[str] = None
        The version of the graph to retrieve.
        Note that this will ONLY check that the version is available.

    Raises
    ----------------------
    ValueError,
        If the given repository is not available.
    ValueError,
        If the given graph is not available.
    """
