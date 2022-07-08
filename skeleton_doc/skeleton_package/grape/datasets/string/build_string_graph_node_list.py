import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def build_string_graph_node_list(sequence_path: str, enrichment_path: str, info_path: str, node_list_path: str):
    """Processes string data into node list.

    Parameters
    ----------------------
    sequence_path: str
        File from where to load sequence data.
    enrichment_path: str
        File from where to load enrichment data.
    info_path: str
        File from where to load info data.
    node_list_path: str
        Path where to write the resulting TSV.
    """
