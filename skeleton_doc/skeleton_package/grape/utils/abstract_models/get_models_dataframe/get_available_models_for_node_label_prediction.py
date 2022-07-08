import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas

def get_available_models_for_node_label_prediction() -> pandas.DataFrame:
    """Returns dataframe with informations about available models for node-label prediction."""
