import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def add_numeric_id_to_csv(original_csv_path: str, original_csv_separator: Optional[str], original_csv_header: Optional[bool], target_csv_path: str, target_csv_separator: Optional[str], target_csv_header: Optional[bool], target_csv_ids_column: Optional[str], target_csv_ids_column_number: Optional[int], comment_symbol: Optional[str], max_rows_number: Optional[int], rows_to_skip: Optional[int], verbose: Optional[bool]):
    """Create a new CSV with the lines number added to it.
    
    Parameters
    ----------
    original_csv_path: str,
        The path from where to load the original CSV.
    original_csv_separator: Optional[str],
        Separator to use for the original CSV.
    original_csv_header: Optional[bool],
        Whether the original CSV has an header.
    target_csv_path: str,
        The path from where to load the target CSV. This cannot be the same as the original CSV.
    target_csv_separator: Optional[str],
        Separator to use for the target CSV. If None, the one provided from the original CSV will be used.
    target_csv_header: Optional[bool],
        Whether the target CSV has an header. If None, the one provided from the original CSV will be used.
    target_csv_ids_column: Optional[str],
        The column name to use for the ids in the target list.
    target_csv_ids_column_number: Optional[int],
        The column number to use for the ids in the target list.
    comment_symbol: Optional[str],
        The comment symbol to use within the original CSV.
    max_rows_number: Optional[int],
        The amount of rows to load from the original CSV.
    rows_to_skip: Optional[int],
        The amount of rows to skip from the original CSV.
    verbose: Optional[bool],
        Whether to show the loading bar while processing the file.
    
    
    Raises
    -------
    ValueError
        If there are problems with opening the original or target file.
    ValueError
        If the original and target paths are identical."""
