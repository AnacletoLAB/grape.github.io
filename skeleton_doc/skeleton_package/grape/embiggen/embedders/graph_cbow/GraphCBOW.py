import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

class GraphCBOW:
    """GraphCBOW model for graph embedding.

    The GraphCBOW model for graoh embedding receives a list of contexts and tries
    to predict the central word. The model makes use of an NCE loss layer
    during the training process to generate the negatives.
    """
    
    @property
    def embedding(self):
        """Return model embeddings."""
    
    
    
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
    
    
    