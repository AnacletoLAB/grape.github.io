from typing import *


def cooccurence_matrix(sequences: List[List[int]]):
    """Return triple with CSR representation of cooccurrence matrix.
    
    The first vector has the sources, the second vector the destinations
    and the third one contains the min-max normalized frequencies.
    
    Arguments
    ---------
    
    sequences: List[List[int]],
        the sequence of sequences of integers to preprocess.
    window_size: int = 4,
        Window size to consider for the sequences.
    verbose: bool = False,
        whether to show the progress bars.
        The default behaviour is false."""
