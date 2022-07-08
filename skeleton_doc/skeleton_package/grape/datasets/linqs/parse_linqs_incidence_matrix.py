import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def parse_linqs_incidence_matrix(cites_path: str, content_path: str, edge_path: str, node_path: str):
    """Parse Cora and Citeseer incidence matrix and generates proper edge list and node file.

    Parameters
    -------------------
    cites_path: str,
        Path from where to load the cites file.
    content_path: str,
        Path from where to load the content file.
    edge_path: str,
        Path where to store the edge list.
    node_path: str,
        Path where to store the node list.
    """
