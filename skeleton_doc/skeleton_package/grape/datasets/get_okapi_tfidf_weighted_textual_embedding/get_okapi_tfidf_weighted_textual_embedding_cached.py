import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import numpy

def get_okapi_tfidf_weighted_textual_embedding_cached() -> numpy.ndarray:
    """Returns tokens od the textual data available at the given file.

    Parameters
    -------------------------
    path: str
        Path from where to load the CSV.
    separator: Optional[str] = None
        The separator for the CSV.
    header: Optional[bool] = None
        Whether to skip the header.
    k1: float = 1.5
        K1 parameter for the OKAPI TFIDF
    b: float = 0.75
        B parameter for the OKAPI TFIDF
    columns: Optional[str] = None
        The columns to be taken into consideration for the tokenization
    pretrained_model_name_or_path: str = "bert-base-uncased"
        Name of the pretrained model to be used.
    read_csv_kwargs: Optional[Dict] = None
        Kwargs to be used when opening a CSV to be read
    verbose: bool = True
        Whether to show the loading bars
    """
