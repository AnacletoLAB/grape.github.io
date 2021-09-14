from typing import *


def are_there_selfloops_in_edge_list(path: str, separator: Optional[str], header: Optional[bool], sources_column: Optional[str], sources_column_number: Optional[int], destinations_column: Optional[str], destinations_column_number: Optional[int], comment_symbol: Optional[str], max_rows_number: Optional[int], rows_to_skip: Optional[int], edges_number: Optional[int], load_edge_list_in_parallel: Optional[bool], verbose: Optional[bool], name: Optional[str]):
    """Return whether there are selfloops in the edge list.
    
    Parameters
    ----------
    path: str,
        The path from where to load the edge list.
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
    comment_symbol: Optional[str],
        The comment symbol to use for the lines to skip.
    max_rows_number: Optional[int],
        The number of rows to read at most. Note that this parameter is ignored when reading in parallel.
    rows_to_skip: Optional[int],
        Number of rows to skip in the edge list.
    edges_number: Optional[int],
        Number of edges in the edge list.
    load_edge_list_in_parallel: Optional[bool],
        Whether to execute the task in parallel or sequential. Generally, parallel is preferable.
    verbose: Optional[bool],
        Whether to show the loading bar while processing the file.
    name: Optional[str],
        The name of the graph to display in the loading bar."""
