from typing import *


class GloveSequence:
    """Abstract Keras Sequence object for running models on huge datasets."""
    
    @property
    def batch_size(self):
        """Return batch size property of the sequence."""
    
    
    
    @property
    def elapsed_epochs(self):
        """Return elapsed epochs since training started."""
    
    
    
    @property
    def features(self):
        """Return number of features."""
    
    
    
    @property
    def sample_number(self):
        """Return total number of samples in sequence."""
    
    
    
    @property
    def steps_per_epoch(self):
        """Number of steps to execute on the sequence."""
    
    
    