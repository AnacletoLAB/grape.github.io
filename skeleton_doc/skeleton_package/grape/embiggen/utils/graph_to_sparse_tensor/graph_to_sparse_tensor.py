import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def graph_to_sparse_tensor(graph: Graph, use_weights: bool) -> SparseTensor:
    """Returns provided graph as sparse Tensor.

    Parameters
    -------------------
    graph: Graph,
        The graph to convert.
    use_weights: bool,
        Whether to load the graph weights.

    Raises
    -------------------
    ValueError,
        If the weights are requested but the graph does not contain any.
    ValueError,
        If the graph contains singletons.
    ValueError,
        If the graph is a multigraph.

    Returns
    -------------------
    SparseTensor with (weighted) adjacency matrix.
    """
