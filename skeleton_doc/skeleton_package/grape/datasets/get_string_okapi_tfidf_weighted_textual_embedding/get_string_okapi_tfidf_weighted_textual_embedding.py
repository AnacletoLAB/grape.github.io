import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import numpy

def get_string_okapi_tfidf_weighted_textual_embedding(name: str, version: str, k1: float, b: float, pretrained_model_name_or_path: str, columns_to_use: typing.List[str], bert_model_kwargs: typing.Optional[typing.Dict], verbose: bool) -> numpy.ndarray:
    """Return OKAPI TFIDF-weighted textual embedding of the data available for the selected graph.
    
    Parameters
    ------------------------
    name: str
        The name of the graph to be retrieved and loaded.
    version: str = "links.v11.5"
        The version of the graph to be retrieved.
    k1: float = 1.5
        K1 parameter for the OKAPI TFIDF
    b: float = 0.75
        B parameter for the OKAPI TFIDF
    pretrained_model_name_or_path: str = "bert-base-uncased"
        Name of the pretrained model to be used.
    bert_model_kwargs: Optional[Dict] = None
        Arguments to be used to retrieve the model.
    verbose: bool = True
        Whether to show the loading bars
    """
