import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def convert_edge_list_to_numeric(original_edge_path: str, original_edge_list_separator: Optional[str], original_edge_list_header: Optional[bool], original_sources_column: Optional[str], original_sources_column_number: Optional[int], original_destinations_column: Optional[str], original_destinations_column_number: Optional[int], original_edge_list_edge_types_column: Optional[str], original_edge_list_edge_types_column_number: Optional[int], original_weights_column: Optional[str], original_weights_column_number: Optional[int], target_edge_path: str, target_edge_list_separator: Optional[str], target_edge_list_header: Optional[bool], target_sources_column: Optional[str], target_sources_column_number: Optional[int], target_destinations_column: Optional[str], target_destinations_column_number: Optional[int], target_edge_list_edge_types_column: Optional[str], target_edge_list_edge_types_column_number: Optional[int], target_weights_column: Optional[str], target_weights_column_number: Optional[int], target_node_path: Optional[str], target_node_list_separator: Optional[str], target_node_list_header: Optional[bool], target_nodes_column: Optional[str], target_nodes_column_number: Optional[int], target_edge_type_list_path: Optional[str], target_edge_type_list_edge_types_column_number: Optional[int], target_edge_type_list_edge_types_column: Optional[str], comment_symbol: Optional[str], default_edge_type: Optional[str], default_weight: Optional[float], max_rows_number: Optional[int], rows_to_skip: Optional[int], edges_number: Optional[int], skip_edge_types_if_unavailable: Optional[bool], skip_weights_if_unavailable: Optional[bool], verbose: Optional[bool], name: Optional[str]):
    """Create a new edge list starting from given one with node IDs densified.
    
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
    original_edge_list_edge_types_column: Optional[str],
        The column name to use for the edge types in the original edges list.
    original_edge_list_edge_types_column_number: Optional[int],
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
    target_edge_list_edge_types_column: Optional[str],
        The column name to use for the edge types in the target edges list. If None, the one provided from the original edge list will be used.
    target_edge_list_edge_types_column_number: Optional[int],
        The column number to use for the edge types in the target edges list. If None, the one provided from the original edge list will be used.
    target_weights_column: Optional[str],
        The column name to use for the weights in the target edges list. If None, the one provided from the original edge list will be used.
    target_weights_column_number: Optional[int],
        The column number to use for the weights in the target edges list. If None, the one provided from the original edge list will be used.
    target_node_path: Optional[str],
        The optional name for the node list to be written out.
    target_node_list_separator: Optional[str],
        The separator to use for the node list.
    target_node_list_header: Optional[bool],
        Whether to add the header to the node list.
    target_nodes_column: Optional[str],
        The column name for the node names.
    target_nodes_column_number: Optional[int],
        The column number for the node names.
    target_node_ids_column: Optional[str],
        The column name for the node IDs.
    target_node_ids_column_number: Optional[int],
        The column number for the node IDs.
    target_edge_type_list_path: Optional[str],
        The optional path where to store the parsed edge types.
    target_edge_type_list_edge_types_column_number: Optional[int],
        The column number where to store the edge type names.
    target_edge_type_list_edge_types_column: Optional[str],
        The column name where to store the edge type names.
    target_edge_types_ids_column_number: Optional[int],
        The column number where to the store the edge type IDs.
    target_edge_types_ids_column: Optional[str],
        The column name where to store the edge type IDs.
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
        The name of the graph to display in the loading bar.
    
    
    Raises
    -------
    ValueError
        If there are problems with opening the original or target file.
    ValueError
        If the original and target paths are identical."""
