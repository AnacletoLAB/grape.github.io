from typing import *


def get_rows_number(file_path: str):
    """Return number of rows in given CSV path.
    
    Parameters
    ----------
    file_path: str,
        The path from where to load the original CSV.
    
    
    Raises
    -------
    ValueError
        If there are problems with opening the file."""
