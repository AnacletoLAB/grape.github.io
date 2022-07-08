import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def create_species_tree_node_and_edge_list(tree_path: str, tree_metadata_path: str, node_list_path: str, edge_list_path: str):
    """Create the node and edge lists for the species tree at given path.

    Parameters
    -------------------
    tree_path: str
        The path from where to load the tree data.
    tree_metadata_path: str
        The path from where to load the tree metadata.
    node_list_path: str
        The path where to store the tree node list.
    edge_list_path: str
        The path where to store the tree edge list.
    """
