import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas

def get_models_dataframe() -> pandas.DataFrame:
    """Returns dataframe with informations about available models."""
