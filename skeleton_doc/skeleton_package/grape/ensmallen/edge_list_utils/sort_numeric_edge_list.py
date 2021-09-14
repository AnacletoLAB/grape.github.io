import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def sort_numeric_edge_list(path: str, target_path: str, separator: Optional[str], header: Optional[bool], sources_column: Optional[str], sources_column_number: Optional[int], destinations_column: Optional[str], destinations_column_number: Optional[int], edge_types_column: Optional[str], edge_types_column_number: Optional[int], rows_to_skip: Optional[int], skip_edge_types_if_unavailable: Optional[bool]):
    """Sort given numeric edge list in place using the sort command.
    
    Parameters
    ----------
    path: str,
        The path from where to load the edge list.
    target_path: str,
        The where to store the edge list.
    separator: Optional[str],
        The separator for the rows in the edge list.
    header: Optional[bool],
        Whether the edge list has an header.
    sources_column: Optional[str],
        The column name to use for the source nodes.
    sources_column_number: Optional[int],
        The column number to use for the source nodes.
    destinations_column: Optional[str],
        The column name to use for the destination nodes.
    destinations_column_number: Optional[int],
        The column number to use for the destination nodes.
    edge_types_column: Optional[str],
        The column name to use for the edge types.
    edge_types_column_number: Optional[int],
        The column number to use for the edge types.
    rows_to_skip: Optional[int],
        Number of rows to skip in the edge list.
    skip_edge_types_if_unavailable: Optional[bool],
        Whether to automatically skip the edge types if they are not available."""
