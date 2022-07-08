import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas

def load_string_info_node_list(path: str) -> pandas.DataFrame:
    """Return loaded STRING node list with informations.

    Parameters
    -----------------------
    path: str
        Path to the protein node list with informations.
    """
