from typing import *


class Node2Vec:
    """Abstract class for sequence embedding models."""
    
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
    
    
    