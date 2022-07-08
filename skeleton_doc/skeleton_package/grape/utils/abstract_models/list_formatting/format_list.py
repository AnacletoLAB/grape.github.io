import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def format_list(words: typing.List[str], bold_words: bool) -> str:
    """Returns formatted list with Oxford comma.

    Parameters
    --------------------------
    words: List[str]
        The list of words to format.
    bold_words: bool = False
        Whether to use bold letters.
    """
