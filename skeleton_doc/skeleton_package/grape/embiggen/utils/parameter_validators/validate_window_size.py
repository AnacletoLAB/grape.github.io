from typing import *


def validate_window_size(candidate_window_size: int) -> int:
    """Return validated window size candidate, raising a meaningful error otherwise.

    Parameters
    -----------------
    candidate_window size: int,
        The candidate window size value to validate.

    Raises
    -----------------
    ValueError,
        If the provided window size parameter is not within
        the allowed set of values.

    Returns
    -----------------
    The validated value.
    """
