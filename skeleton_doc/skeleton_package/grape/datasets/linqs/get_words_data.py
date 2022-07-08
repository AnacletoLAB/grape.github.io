import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_words_data(graph: Graph, remove_nodes_without_features: bool) -> Tuple:
    """Return dataframe with words features.

    Parameters
    --------------------
    graph: Graph
        Graph containing the words features to be extracted.
    remove_nodes_without_features: bool = True
        Whether to remove the nodes without known node features.

    Returns
    --------------------
    Tuple containing:
        - Provided graph without the Word nodes.
        - Pandas DataFrame with words features as columns and nodes as rows.
    """
