import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def holdouts_generator(holdout_callback: typing.Callable, train_size: float, holdouts_number: int, random_state: int, random_state_factor: int, desc: str, disable: bool, leave: bool, enable_speedup: bool) -> Generator:
    """Return generator of the holdouts.

    The generator returned yields a tuple with the current holdouts number
    and the training and test graphs.

    Parameters
    ----------------------------
    holdout_callback: Callable,
        The callback that generates the training and test holdout.
    train_size: float = 0.8,
        The portion of the data to reserve for the training data.
        Note that this value is a maximal, if there is an odd number
        of values the value will be assigned to the test set in order to
        avoid a potentially small positive evaluation bias.
    holdouts_number: int = 10,
        The number of holdouts to yield.
    random_state: int = 42,
        The random state to use to start generating the holdouts.
    random_state_factor: int = 1000,
        The factor to use to multiply the increase of the random state.
        This is needed to make the randomly generated holdouts more different.
    desc: str = "Computing holdouts",
        The description for the TQDM bar.
    disable: bool = False,
        Whether to show the loading bars,
    leave: bool = False,
        Whether to leave the loading bar after execution.
    enable_speedup: bool = True,
        Whether to enable all speedups in the holdouts graphs.
    **kwargs: Dict,
        The kwargs to pass to the given callback.
    """
