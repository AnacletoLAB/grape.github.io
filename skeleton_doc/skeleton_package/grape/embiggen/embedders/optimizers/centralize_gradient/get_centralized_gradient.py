import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_centralized_gradient(gradient: Tensor) -> Tensor:
    """Centralize over zero mean the provided gradient.

    Parameters
    -----------------------
    gradient: tf.Tensor,
        Gradient to centralize over zero mean.

    References
    -----------------------
    [Gradient Centralization: A New Optimization Technique for Deep Neural Networks](https://arxiv.org/pdf/2004.01461.pdf)
    """
