import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas

def get_all_available_graphs_dataframe() -> pandas.DataFrame:
    """Return pandas dataframe with all the available graphs.,"""
