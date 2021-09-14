from typing import *


def apply_centralized_gradients(optimizers: OptimizerV2):
    """Replaces the get_gradients method with the one centralizing the gradient."""
