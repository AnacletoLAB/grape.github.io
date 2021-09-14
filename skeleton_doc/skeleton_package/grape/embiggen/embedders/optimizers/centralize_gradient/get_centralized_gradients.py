import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def get_centralized_gradients(optimizer: "OptimizerV2", loss: Tensor, params: typing.List) -> List:
    """Centralize over zero mean all the provided gradients.

    Parameters
    -----------------------
    optimizer: Optimizer,
        The optimizer instance (e.g. Adam, Nadam, ...)
    loss: tf.Tensor,
        The loss function of this model.
    params: List,
        Parameters relevant to the computation of the gradient.

    References
    -----------------------
    [Gradient Centralization: A New Optimization Technique for Deep Neural Networks](https://arxiv.org/pdf/2004.01461.pdf)
    """
