import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def abstract_class(klass: typing.Type[ForwardRef('AbstractModel')]) -> Type:
    """Simply adds a descriptor for meta-programming and nothing else."""
