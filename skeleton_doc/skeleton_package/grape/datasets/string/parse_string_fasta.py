import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas

def parse_string_fasta(path: str) -> pandas.DataFrame:
    """Return dataframe with aminoacid fasta sequences from given path.

    Parameters
    -----------------------
    path: str
        Path to the fasta file to load.
    """
