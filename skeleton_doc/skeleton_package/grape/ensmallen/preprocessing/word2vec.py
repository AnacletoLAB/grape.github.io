import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def word2vec(sequences: List[List[int]], window_size: int):
    """Return training batches for Word2Vec models.
    
    The batch is composed of a tuple as the following:
    
    - (Contexts indices, central nodes indices): the tuple of nodes
    
    This does not provide any output value as the model uses NCE loss
    and basically the central nodes that are fed as inputs work as the
    outputs value.
    
    Arguments
    ---------
    
    sequences: List[List[int]],
        the sequence of sequences of integers to preprocess.
    window_size: int,
        Window size to consider for the sequences."""
