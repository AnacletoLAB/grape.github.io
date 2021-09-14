import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def okapi_bm25_tfidf_str(documents: List[List[str]], k1: Optional[float], b: Optional[float], vocabulary_size: Optional[int], verbose: Optional[bool]):
    """Return vocabulary and TFIDF matrix of given documents.
    
    
    Arguments
    ---------
    documents: List[List[str]],
        The documents to parse
    k1: Optional[float],
        The default parameter for k1, tipically between 1.2 and 2.0.
    b: Optional[float],
        The default parameter for b, tipically equal to 0.75.
    vocabulary_size: Optional[int],
        The expected vocabulary size.
    verbose: Optional[bool],
        Whether to show a loading bar."""
