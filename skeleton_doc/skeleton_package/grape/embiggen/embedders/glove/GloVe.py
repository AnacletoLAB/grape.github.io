import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

class GloVe:
    """GloVe model for graph and words embedding.

    The GloVe model for graph embedding receives two words and is asked to
    predict its cooccurrence probability.
    """
    
    @property
    def embedding(self):
        """Return model embeddings.
    
            Raises
            -------------------
            NotImplementedError,
                If the current embedding model does not have an embedding layer.
            """
    
    
    
    @property
    def name(self):
        """Return model name."""
    
    
    
    @property
    def trainable(self):
        """Return whether the embedding layer can be trained.
    
            Raises
            -------------------
            NotImplementedError,
                If the current embedding model does not have an embedding layer.
            """
    
    
    