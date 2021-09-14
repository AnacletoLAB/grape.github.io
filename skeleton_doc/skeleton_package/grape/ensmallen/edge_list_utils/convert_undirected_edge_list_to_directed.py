from typing import *


def convert_undirected_edge_list_to_directed(original_edge_path: str, original_edge_list_separator: Optional[str], original_edge_list_header: Optional[bool], original_sources_column: Optional[str], original_sources_column_number: Optional[int], original_destinations_column: Optional[str], original_destinations_column_number: Optional[int], original_edge_list_edge_type_column: Optional[str], original_edge_list_edge_type_column_number: Optional[int], original_weights_column: Optional[str], original_weights_column_number: Optional[int], target_edge_path: str, target_edge_list_separator: Optional[str], target_edge_list_header: Optional[bool], target_sources_column: Optional[str], target_sources_column_number: Optional[int], target_destinations_column: Optional[str], target_destinations_column_number: Optional[int], target_edge_list_edge_type_column: Optional[str], target_edge_list_edge_type_column_number: Optional[int], target_weights_column: Optional[str], target_weights_column_number: Optional[int], comment_symbol: Optional[str], default_edge_type: Optional[str], default_weight: Optional[float], max_rows_number: Optional[int], rows_to_skip: Optional[int], edges_number: Optional[int], skip_edge_types_if_unavailable: Optional[bool], skip_weights_if_unavailable: Optional[bool], verbose: Optional[bool], name: Optional[str]):
    """Create a new directed edge list from a given undirected one by duplicating the undirected edges.
    
    Parameters
    ----------
    original_edge_path: str,
        The path from where to load the original edge list.
    original_edge_list_separator: Optional[str],
        Separator to use for the original edge list.
    original_edge_list_header: Optional[bool],
        Whether the original edge list has an header.
    original_sources_column: Optional[str],
        The column name to use to load the sources in the original edges list.
    original_sources_column_number: Optional[int],
        The column number to use to load the sources in the original edges list.
    original_destinations_column: Optional[str],
        The column name to use to load the destinations in the original edges list.
    original_destinations_column_number: Optional[int],
        The column number to use to load the destinations in the original edges list.
    original_edge_list_edge_type_column: Optional[str],
        The column name to use for the edge types in the original edges list.
    original_edge_list_edge_type_column_number: Optional[int],
        The column number to use for the edge types in the original edges list.
    original_weights_column: Optional[str],
        The column name to use for the weights in the original edges list.
    original_weights_column_number: Optional[int],
        The column number to use for the weights in the original edges list.
    target_edge_path: str,
        The path from where to load the target edge list. This must be different from the original edge list path.
    target_edge_list_separator: Optional[str],
        Separator to use for the target edge list. If None, the one provided from the original edge list will be used.
    target_edge_list_header: Optional[bool],
        Whether the target edge list has an header. If None, the one provided from the original edge list will be used.
    target_sources_column: Optional[str],
        The column name to use to load the sources in the target edges list. If None, the one provided from the original edge list will be used.
    target_sources_column_number: Optional[int],
        The column number to use to load the sources in the target edges list. If None, the one provided from the original edge list will be used.
    target_destinations_column: Optional[str],
        The column name to use to load the destinations in the target edges list. If None, the one provided from the original edge list will be used.
    target_destinations_column_number: Optional[int],
        The column number to use to load the destinations in the target edges list. If None, the one provided from the original edge list will be used.
    target_edge_list_edge_type_column: Optional[str],
        The column name to use for the edge types in the target edges list. If None, the one provided from the original edge list will be used.
    target_edge_list_edge_type_column_number: Optional[int],
        The column number to use for the edge types in the target edges list. If None, the one provided from the original edge list will be used.
    target_weights_column: Optional[str],
        The column name to use for the weights in the target edges list. If None, the one provided from the original edge list will be used.
    target_weights_column_number: Optional[int],
        The column number to use for the weights in the target edges list. If None, the one provided from the original edge list will be used.
    comment_symbol: Optional[str],
        The comment symbol to use within the original edge list.
    default_edge_type: Optional[str],
        The default edge type to use within the original edge list.
    default_weight: Optional[float],
        The default weight to use within the original edge list.
    max_rows_number: Optional[int],
        The amount of rows to load from the original edge list.
    rows_to_skip: Optional[int],
        The amount of rows to skip from the original edge list.
    edges_number: Optional[int],
        The expected number of edges. It will be used for the loading bar.
    skip_edge_types_if_unavailable: Optional[bool],
        Whether to automatically skip the edge types if they are not available.
    skip_weights_if_unavailable: Optional[bool],
        Whether to automatically skip the weights if they are not available.
    verbose: Optional[bool],
        Whether to show the loading bar while processing the file.
    name: Optional[str],
        The name of the graph to display in the loading bar."""
