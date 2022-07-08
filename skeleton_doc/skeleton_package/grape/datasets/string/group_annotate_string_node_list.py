import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas

def group_annotate_string_node_list(path: str) -> pandas.DataFrame:
    """Return file grouped by protein node name.

    Parameters
    -----------------------
    path: str
        Path to the annotated protein node list file to load.
    """
