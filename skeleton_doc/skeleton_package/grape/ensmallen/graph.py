from typing import *


class Graph:
    """TODO!: document this"""
    
    def add_selfloops(self):
        """Returns new graph with added in missing self-loops with given edge type and weight.
        
        Parameters
        ----------
        
        
        Raises
        -------
        ValueError
            If the edge type for the new selfloops is provided but the graph does not have edge types.
        ValueError
            If the edge weight for the new selfloops is provided but the graph does not have edge weights.
        ValueError
            If the edge weight for the new selfloops is NOT provided but the graph does have edge weights."""
    
    
    
    def approximated_vertex_cover_set(self):
        """Returns 2-approximated verted cover set using greedy algorithm."""
    
    
    
    def are_nodes_remappable(self, other: Graph):
        """Return whether nodes are remappable to those of the given graph.
        
        Parameters
        ----------
        other: Graph,
            graph towards remap the nodes to."""
    
    
    
    def connected_components(self, verbose: Optional[bool]):
        """Compute the connected components building in parallel a spanning tree using [bader's algorithm](https://www.sciencedirect.com/science/article/abs/pii/S0743731505000882).
        
        **This works only for undirected graphs.**
        
        This method is **not thread save and not deterministic** but by design of the algorithm this
        shouldn't matter but if we will encounter non-detemristic bugs here is where we want to look.
        
        The returned quadruple contains:
        - Vector of the connected component for each node.
        - Number of connected components.
        - Minimum connected component size.
        - Maximum connected component size.
        
        Parameters
        ----------
        verbose: Optional[bool],
            Whether to show a loading bar or not.
        
        
        Raises
        -------
        ValueError
            If the given graph is directed.
        ValueError
            If the system configuration does not allow for the creation of the thread pool."""
    
    
    
    def connected_holdout(self, train_size: float, random_state: Optional[int], edge_types: Optional[List[Optional[str]]], include_all_edge_types: Optional[bool], verbose: Optional[bool]):
        """Returns holdout for training ML algorithms on the graph structure.
        
        The holdouts returned are a tuple of graphs. The first one, which
        is the training graph, is garanteed to have the same number of
        graph components as the initial graph. The second graph is the graph
        meant for testing or validation of the algorithm, and has no garantee
        to be connected. It will have at most (1-train_size) edges,
        as the bound of connectivity which is required for the training graph
        may lead to more edges being left into the training partition.
        
        In the option where a list of edge types has been provided, these
        edge types will be those put into the validation set.
        
        Parameters
        ----------
        train_size: float,
            Rate target to reserve for training.
        random_state: Optional[int],
            The random_state to use for the holdout,
        edge_types: Optional[List[Optional[str]]],
            Edge types to be selected for in the validation set.
        include_all_edge_types: Optional[bool],
            Whether to include all the edges between two nodes.
        verbose: Optional[bool],
            Whether to show the loading bar.
        
        
        Raises
        -------
        ValueError
            If the edge types have been specified but the graph does not have edge types.
        ValueError
            If the required training size is not a real value between 0 and 1.
        ValueError
            If the current graph does not allow for the creation of a spanning tree for the requested training size."""
    
    
    
    def contains(self, other: Graph):
        """Return true if given graph edges are all contained within current graph.
        
        Parameters
        ----------
        other: Graph,
            The graph to check against.
        
        
        Raises
        -------
        ValueError
            If a graph is directed and the other is undirected.
        ValueError
            If one of the two graphs has edge weights and the other does not.
        ValueError
            If one of the two graphs has node types and the other does not.
        ValueError
            If one of the two graphs has edge types and the other does not."""
    
    
    
    def decode_edge(self, edge: int):
        """Returns source and destination nodes corresponding to given edge ID.
        
        Parameters
        ----------
        edge: int,
            The edge value to decode."""
    
    
    
    def disable_all(self):
        """Disable all extra perks, reducing memory impact but incresing time requirements"""
    
    
    
    def drop_disconnected_nodes(self):
        """Returns new graph without disconnected nodes.
        
        A disconnected node is a node with no connection to any other node."""
    
    
    
    def drop_parallel_edges(self):
        """Returns new graph without parallel edges"""
    
    
    
    def drop_selfloops(self):
        """Returns new graph without selfloops."""
    
    
    
    def drop_singleton_nodes(self):
        """Returns new graph without singleton nodes.
        
        A node is singleton when does not have neither incoming or outgoing edges."""
    
    
    
    def drop_singleton_nodes_with_selfloops(self):
        """Returns new graph without singleton nodes with selfloops.
        
        A node is singleton with selfloop when does not have neither incoming or outgoing edges."""
    
    
    
    def drop_unknown_edge_types(self):
        """Returns new graph without unknown edge types and relative edges.
        
        Note that this method will remove ALL edges labeled with unknown edge
        type!"""
    
    
    
    def drop_unknown_node_types(self):
        """Returns new graph without unknown node types and relative nodes.
        
        Note that this method will remove ALL nodes labeled with unknown node
        type!"""
    
    
    
    def enable(self, vector_sources: Optional[bool], vector_destinations: Optional[bool], vector_cumulative_node_degrees: Optional[bool]):
        """Enable extra perks that buys you time as you accept to spend more memory.
        
        Parameters
        ----------
        vector_sources: Optional[bool],
            Whether to cache sources into a vector for faster walks.
        vector_destinations: Optional[bool],
            Whether to cache destinations into a vector for faster walks.
        vector_cumulative_node_degrees: Optional[bool],
            Whether to cache cumulative_node_degrees into a vector for faster walks."""
    
    
    
    def encode_edge(self, src: int, dst: int):
        """Return edge value corresponding to given node IDs.
        
        Parameters
        ----------
        src: int,
            The source node ID.
        dst: int,
            The destination node ID."""
    
    
    
    def filter_from_ids(self, node_ids_to_keep: Optional[List[int]], node_ids_to_filter: Optional[List[int]], node_type_ids_to_keep: Optional[List[Optional[List[int]]]], node_type_ids_to_filter: Optional[List[Optional[List[int]]]], node_type_id_to_keep: Optional[List[Optional[int]]], node_type_id_to_filter: Optional[List[Optional[int]]], edge_ids_to_keep: Optional[List[int]], edge_ids_to_filter: Optional[List[int]], edge_node_ids_to_keep: Optional[List[Tuple[int, int]]], edge_node_ids_to_filter: Optional[List[Tuple[int, int]]], edge_type_ids_to_keep: Optional[List[Optional[int]]], edge_type_ids_to_filter: Optional[List[Optional[int]]], min_edge_weight: Optional[float], max_edge_weight: Optional[float], filter_singleton_nodes: Optional[bool], filter_singleton_nodes_with_selfloop: Optional[bool], filter_selfloops: Optional[bool], filter_parallel_edges: Optional[bool]):
        """Returns a **NEW** Graph that does not have the required attributes.
        
        Parameters
        ----------
        node_ids_to_keep: Optional[List[int]],
            List of node IDs to keep during filtering.
        node_ids_to_filter: Optional[List[int]],
            List of node IDs to remove during filtering.
        node_type_ids_to_keep: Optional[List[Optional[List[int]]]],
            List of node type IDs to keep during filtering. The node types must match entirely the given node types vector provided.
        node_type_ids_to_filter: Optional[List[Optional[List[int]]]],
            List of node type IDs to remove during filtering. The node types must match entirely the given node types vector provided.
        node_type_id_to_keep: Optional[List[Optional[int]]],
            List of node type IDs to keep during filtering. Any of node types must match with one of the node types given.
        node_type_id_to_filter: Optional[List[Optional[int]]],
            List of node type IDs to remove during filtering. Any of node types must match with one of the node types given.
        edge_ids_to_keep: Optional[List[int]],
            List of edge IDs to keep during filtering.
        edge_ids_to_filter: Optional[List[int]],
            List of edge IDs to remove during filtering.
        edge_node_ids_to_keep: Optional[List[Tuple[int, int]]],
            List of tuple of node IDs to keep during filtering.
        edge_node_ids_to_filter: Optional[List[Tuple[int, int]]],
            List of tuple of node IDs to remove during filtering.
        edge_type_ids_to_keep: Optional[List[Optional[int]]],
            List of edge type IDs to keep during filtering.
        edge_type_ids_to_filter: Optional[List[Optional[int]]],
            List of edge type IDs to remove during filtering.
        min_edge_weight: Optional[float],
            Minimum edge weight. Values lower than this are removed.
        max_edge_weight: Optional[float],
            Maximum edge weight. Values higher than this are removed.
        filter_singleton_nodes: Optional[bool],
            Whether to filter out singleton nodes.
        filter_singleton_nodes_with_selfloop: Optional[bool],
            Whether to filter out singleton nodes with selfloops.
        filter_selfloops: Optional[bool],
            Whether to filter out selfloops.
        filter_parallel_edges: Optional[bool],
            Whether to filter out parallel edges.
        verbose: Optional[bool],
            Whether to show loading bar while building the graphs."""
    
    
    
    def filter_from_names(self, node_names_to_keep: Optional[List[str]], node_names_to_filter: Optional[List[str]], node_type_names_to_keep: Optional[List[Optional[List[str]]]], node_type_names_to_filter: Optional[List[Optional[List[str]]]], node_type_name_to_keep: Optional[List[Optional[str]]], node_type_name_to_filter: Optional[List[Optional[str]]], edge_node_names_to_keep: Optional[List[Tuple[str, str]]], edge_node_names_to_filter: Optional[List[Tuple[str, str]]], edge_type_names_to_keep: Optional[List[Optional[str]]], edge_type_names_to_filter: Optional[List[Optional[str]]], min_edge_weight: Optional[float], max_edge_weight: Optional[float], filter_singleton_nodes: Optional[bool], filter_singleton_nodes_with_selfloop: Optional[bool], filter_selfloops: Optional[bool], filter_parallel_edges: Optional[bool]):
        """Returns a **NEW** Graph that does not have the required attributes.
        
        Parameters
        ----------
        node_names_to_keep: Optional[List[str]],
            List of node names to keep during filtering.
        node_names_to_filter: Optional[List[str]],
            List of node names to remove during filtering.
        node_type_names_to_keep: Optional[List[Optional[List[str]]]],
            List of node type names to keep during filtering. The node types must match entirely the given node types vector provided.
        node_type_names_to_filter: Optional[List[Optional[List[str]]]],
            List of node type names to remove during filtering. The node types must match entirely the given node types vector provided.
        node_type_name_to_keep: Optional[List[Optional[str]]],
            List of node type name to keep during filtering. Any of node types must match with one of the node types given.
        node_type_name_to_filter: Optional[List[Optional[str]]],
            List of node type name to remove during filtering. Any of node types must match with one of the node types given.
        edge_node_names_to_keep: Optional[List[Tuple[str, str]]],
            List of tuple of node names to keep during filtering.
        edge_node_names_to_filter: Optional[List[Tuple[str, str]]],
            List of tuple of node names to remove during filtering.
        edge_type_names_to_keep: Optional[List[Optional[str]]],
            List of edge type names to keep during filtering.
        edge_type_names_to_filter: Optional[List[Optional[str]]],
            List of edge type names to remove during filtering.
        min_edge_weight: Optional[float],
            Minimum edge weight. Values lower than this are removed.
        max_edge_weight: Optional[float],
            Maximum edge weight. Values higher than this are removed.
        filter_singleton_nodes: Optional[bool],
            Whether to filter out singletons.
        filter_singleton_nodes_with_selfloop: Optional[bool],
            Whether to filter out singleton nodes with selfloops.
        filter_selfloops: Optional[bool],
            Whether to filter out selfloops.
        filter_parallel_edges: Optional[bool],
            Whether to filter out parallel edges.
        verbose: Optional[bool],
            Whether to show loading bar while building the graphs."""
    
    
    
    def from_csv(node_type_path: Optional[str], node_type_list_separator: Optional[str], node_types_column_number: Optional[int], node_types_column: Optional[str], node_types_number: Optional[int], numeric_node_type_ids: Optional[bool], minimum_node_type_id: Optional[int], node_type_list_header: Optional[bool], node_type_list_rows_to_skip: Optional[int], node_type_list_is_correct: Optional[bool], node_type_list_max_rows_number: Optional[int], node_type_list_comment_symbol: Optional[str], load_node_type_list_in_parallel: Optional[bool], node_path: Optional[str], node_list_separator: Optional[str], node_list_header: Optional[bool], node_list_rows_to_skip: Optional[int], node_list_is_correct: Optional[bool], node_list_max_rows_number: Optional[int], node_list_comment_symbol: Optional[str], default_node_type: Optional[str], nodes_column_number: Optional[int], nodes_column: Optional[str], node_types_separator: Optional[str], node_list_node_types_column_number: Optional[int], node_list_node_types_column: Optional[str], node_ids_column: Optional[str], node_ids_column_number: Optional[int], nodes_number: Optional[int], minimum_node_id: Optional[int], numeric_node_ids: Optional[bool], node_list_numeric_node_type_ids: Optional[bool], skip_node_types_if_unavailable: Optional[bool], load_node_list_in_parallel: Optional[bool], edge_type_path: Optional[str], edge_types_column_number: Optional[int], edge_types_column: Optional[str], edge_types_number: Optional[int], numeric_edge_type_ids: Optional[bool], minimum_edge_type_id: Optional[int], edge_type_list_separator: Optional[str], edge_type_list_header: Optional[bool], edge_type_list_rows_to_skip: Optional[int], edge_type_list_is_correct: Optional[bool], edge_type_list_max_rows_number: Optional[int], edge_type_list_comment_symbol: Optional[str], load_edge_type_list_in_parallel: Optional[bool], edge_path: Optional[str], edge_list_separator: Optional[str], edge_list_header: Optional[bool], edge_list_rows_to_skip: Optional[int], sources_column_number: Optional[int], sources_column: Optional[str], destinations_column_number: Optional[int], destinations_column: Optional[str], edge_list_edge_types_column_number: Optional[int], edge_list_edge_types_column: Optional[str], default_edge_type: Optional[str], weights_column_number: Optional[int], weights_column: Optional[str], default_weight: Optional[float], edge_ids_column: Optional[str], edge_ids_column_number: Optional[int], edge_list_numeric_edge_type_ids: Optional[bool], edge_list_numeric_node_ids: Optional[bool], skip_weights_if_unavailable: Optional[bool], skip_edge_types_if_unavailable: Optional[bool], edge_list_is_complete: Optional[bool], edge_list_may_contain_duplicates: Optional[bool], edge_list_is_sorted: Optional[bool], edge_list_is_correct: Optional[bool], edge_list_max_rows_number: Optional[int], edge_list_comment_symbol: Optional[str], edges_number: Optional[int], load_edge_list_in_parallel: Optional[bool], verbose: Optional[bool], may_have_singletons: Optional[bool], may_have_singleton_with_selfloops: Optional[bool], directed: bool, name: Optional[str]):
        """Return graph renderized from given CSVs or TSVs-like files.
        
        Parameters
        ----------
        node_type_path: Optional[str],
            The path to the file with the unique node type names.
        node_type_list_separator: Optional[str],
            The separator to use for the node types file. Note that if this is not provided, one will be automatically detected among the following`: comma, semi-column, tab and space.
        node_types_column_number: Optional[int],
            The number of the column of the node types file from where to load the node types.
        node_types_column: Optional[str],
            The name of the column of the node types file from where to load the node types.
        node_types_number: Optional[int],
            The number of the unique node types. This will be used in order to allocate the correct size for the data structure.
        numeric_node_type_ids: Optional[bool],
            Whether the node type names should be loaded as numeric values, i.e. casted from string to a numeric representation.
        minimum_node_type_id: Optional[int],
            The minimum node type ID to be used when using numeric node type IDs.
        node_type_list_header: Optional[bool],
            Whether the node type file has an header.
        node_type_list_rows_to_skip: Optional[int],
            The number of lines to skip in the node types file`: the header is already skipped if it has been specified that the file has an header.
        node_type_list_is_correct: Optional[bool],
            Whether the node types file can be assumed to be correct, i.e. does not have something wrong in it. If this parameter is passed as true on a malformed file, the constructor will crash.
        node_type_list_max_rows_number: Optional[int],
            The maximum number of lines to be loaded from the node types file.
        node_type_list_comment_symbol: Optional[str],
            The comment symbol to skip lines in the node types file. Lines starting with this symbol will be skipped.
        load_node_type_list_in_parallel: Optional[bool],
            Whether to load the node type list in parallel. Note that when loading in parallel, the internal order of the node type IDs may result changed across different iterations. We are working to get this to be stable.
        node_path: Optional[str],
            The path to the file with the unique node names.
        node_list_separator: Optional[str],
            The separator to use for the nodes file. Note that if this is not provided, one will be automatically detected among the following`: comma, semi-column, tab and space.
        node_list_header: Optional[bool],
            Whether the nodes file has an header.
        node_list_rows_to_skip: Optional[int],
            Number of rows to skip in the node list file.
        node_list_is_correct: Optional[bool],
            Whether the nodes file can be assumed to be correct, i.e. does not have something wrong in it. If this parameter is passed as true on a malformed file, the constructor will crash.
        node_list_max_rows_number: Optional[int],
            The maximum number of lines to be loaded from the nodes file.
        node_list_comment_symbol: Optional[str],
            The comment symbol to skip lines in the nodes file. Lines starting with this symbol will be skipped.
        default_node_type: Optional[str],
            The node type to be used when the node type for a given node in the node file is None.
        nodes_column_number: Optional[int],
            The number of the column of the node file from where to load the node names.
        nodes_column: Optional[str],
            The name of the column of the node file from where to load the node names.
        node_types_separator: Optional[str],
            The node types separator.
        node_list_node_types_column_number: Optional[int],
            The number of the column of the node file from where to load the node types.
        node_list_node_types_column: Optional[str],
            The name of the column of the node file from where to load the node types.
        node_ids_column: Optional[str],
            The name of the column of the node file from where to load the node IDs.
        node_ids_column_number: Optional[int],
            The number of the column of the node file from where to load the node IDs
        nodes_number: Optional[int],
            The expected number of nodes. Note that this must be the EXACT number of nodes in the graph.
        minimum_node_id: Optional[int],
            The minimum node ID to be used, when loading the node IDs as numerical.
        numeric_node_ids: Optional[bool],
            Whether to load the numeric node IDs as numeric.
        node_list_numeric_node_type_ids: Optional[bool],
            Whether to load the node types IDs in the node file to be numeric.
        skip_node_types_if_unavailable: Optional[bool],
            Whether to skip the node types without raising an error if these are unavailable.
        load_node_list_in_parallel: Optional[bool],
            Whether to load the node list in parallel. When loading in parallel, without node IDs, the nodes may not be loaded in a deterministic order.
        edge_type_path: Optional[str],
            The path to the file with the unique edge type names.
        edge_types_column_number: Optional[int],
            The number of the column of the edge types file from where to load the edge types.
        edge_types_column: Optional[str],
            The name of the column of the edge types file from where to load the edge types.
        edge_types_number: Optional[int],
            The number of the unique edge types. This will be used in order to allocate the correct size for the data structure.
        numeric_edge_type_ids: Optional[bool],
            Whether the edge type names should be loaded as numeric values, i.e. casted from string to a numeric representation.
        minimum_edge_type_id: Optional[int],
            The minimum edge type ID to be used when using numeric edge type IDs.
        edge_type_list_separator: Optional[str],
            The separator to use for the edge type list. Note that, if None is provided, one will be attempted to be detected automatically between ';', ',', tab or space.
        edge_type_list_header: Optional[bool],
            Whether the edge type file has an header.
        edge_type_list_rows_to_skip: Optional[int],
            Number of rows to skip in the edge type list file.
        edge_type_list_is_correct: Optional[bool],
            Whether the edge types file can be assumed to be correct, i.e. does not have something wrong in it. If this parameter is passed as true on a malformed file, the constructor will crash.
        edge_type_list_max_rows_number: Optional[int],
            The maximum number of lines to be loaded from the edge types file.
        edge_type_list_comment_symbol: Optional[str],
            The comment symbol to skip lines in the edge types file. Lines starting with this symbol will be skipped.
        load_edge_type_list_in_parallel: Optional[bool],
            Whether to load the edge type list in parallel. When loading in parallel, without edge type IDs, the edge types may not be loaded in a deterministic order.
        edge_path: Optional[str],
            The path to the file with the edge list.
        edge_list_separator: Optional[str],
            The separator to use for the edge list. Note that, if None is provided, one will be attempted to be detected automatically between ';', ',', tab or space.
        edge_list_header: Optional[bool],
            Whether the edges file has an header.
        edge_list_rows_to_skip: Optional[int],
            Number of rows to skip in the edge list file.
        sources_column_number: Optional[int],
            The number of the column of the edges file from where to load the source nodes.
        sources_column: Optional[str],
            The name of the column of the edges file from where to load the source nodes.
        destinations_column_number: Optional[int],
            The number of the column of the edges file from where to load the destinaton nodes.
        destinations_column: Optional[str],
            The name of the column of the edges file from where to load the destinaton nodes.
        edge_list_edge_types_column_number: Optional[int],
            The number of the column of the edges file from where to load the edge types.
        edge_list_edge_types_column: Optional[str],
            The name of the column of the edges file from where to load the edge types.
        default_edge_type: Optional[str],
            The edge type to be used when the edge type for a given edge in the edge file is None.
        weights_column_number: Optional[int],
            The number of the column of the edges file from where to load the edge weights.
        weights_column: Optional[str],
            The name of the column of the edges file from where to load the edge weights.
        default_weight: Optional[float],
            The edge weight to be used when the edge weight for a given edge in the edge file is None.
        edge_ids_column: Optional[str],
            The name of the column of the edges file from where to load the edge IDs.
        edge_ids_column_number: Optional[int],
            The number of the column of the edges file from where to load the edge IDs.
        edge_list_numeric_edge_type_ids: Optional[bool],
            Whether to load the edge type IDs as numeric from the edge list.
        edge_list_numeric_node_ids: Optional[bool],
            Whether to load the edge node IDs as numeric from the edge list.
        skip_weights_if_unavailable: Optional[bool],
            Whether to skip the weights without raising an error if these are unavailable.
        skip_edge_types_if_unavailable: Optional[bool],
            Whether to skip the edge types without raising an error if these are unavailable.
        edge_list_is_complete: Optional[bool],
            Whether to consider the edge list as complete, i.e. the edges are presented in both directions when loading an undirected graph.
        edge_list_may_contain_duplicates: Optional[bool],
            Whether the edge list may contain duplicates. If the edge list surely DOES NOT contain duplicates, a validation step may be skipped. By default, it is assumed that the edge list may contain duplicates.
        edge_list_is_sorted: Optional[bool],
            Whether the edge list is sorted. Note that a sorted edge list has the minimal memory peak, but requires the nodes number and the edges number.
        edge_list_is_correct: Optional[bool],
            Whether the edges file can be assumed to be correct, i.e. does not have something wrong in it. If this parameter is passed as true on a malformed file, the constructor will crash.
        edge_list_max_rows_number: Optional[int],
            The maximum number of lines to be loaded from the edges file.
        edge_list_comment_symbol: Optional[str],
            The comment symbol to skip lines in the edges file. Lines starting with this symbol will be skipped.
        edges_number: Optional[int],
            The expected number of edges. Note that this must be the EXACT number of edges in the graph.
        load_edge_list_in_parallel: Optional[bool],
            Whether to load the edge list in parallel. Note that, if the edge IDs indices are not given, it is NOT possible to load a sorted edge list. Similarly, when loading in parallel, without edge IDs, the edges may not be loaded in a deterministic order.
        verbose: Optional[bool],
            Whether to show a loading bar while reading the files. Note that, if parallel loading is enabled, loading bars will not be showed because they are a synchronization bottleneck.
        may_have_singletons: Optional[bool],
            Whether the graph may be expected to have singleton nodes. If it is said that it surely DOES NOT have any, it will allow for some speedups and lower mempry peaks.
        may_have_singleton_with_selfloops: Optional[bool],
            Whether the graph may be expected to have singleton nodes with selfloops. If it is said that it surely DOES NOT have any, it will allow for some speedups and lower mempry peaks.
        directed: bool,
            Whether to load the graph as directed or undirected.
        name: Optional[str],
            The name of the graph to be loaded."""
    
    
    
    def generate_barbell_graph(minimum_node_id: Optional[int], left_clique_nodes_number: Optional[int], right_clique_nodes_number: Optional[int], chain_nodes_number: Optional[int], include_selfloops: Optional[bool], left_clique_node_type: Optional[str], right_clique_node_type: Optional[str], chain_node_type: Optional[str], left_clique_edge_type: Optional[str], right_clique_edge_type: Optional[str], chain_edge_type: Optional[str], left_clique_weight: Optional[float], right_clique_weight: Optional[float], chain_weight: Optional[float], directed: Optional[bool], name: Optional[str]):
        """Creates new barbell graph with given sizes and types.
        
        Parameters
        ----------
        minimum_node_id: Optional[int],
            Minimum node ID to start with. May be needed when chaining graphs. By default 0.
        left_clique_nodes_number: Optional[int],
            Number of nodes in the left clique. By default 10.
        right_clique_nodes_number: Optional[int],
             Number of nodes in the right clique. By default equal to the left clique.
        chain_nodes_number: Optional[int],
            Number of nodes in the chain. By default 10.
        include_selfloops: Optional[bool],
            Whether to include selfloops.
        left_clique_node_type: Optional[str],
            The node type to use for the left clique. By default 'left_clique'.
        right_clique_node_type: Optional[str],
            The node type to use for the right clique. By default 'right_clique'.
        chain_node_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        left_clique_edge_type: Optional[str],
            The node type to use for the left clique. By default 'left_clique'.
        right_clique_edge_type: Optional[str],
            The node type to use for the right clique. By default 'right_clique'.
        chain_edge_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        left_clique_weight: Optional[float],
            The weight to use for the edges in the left clique. By default None.
        right_clique_weight: Optional[float],
            The weight to use for the edges in the right clique. By default None.
        chain_weight: Optional[float],
            The weight to use for the edges in the chain. By default None.
        directed: Optional[bool],
            Whether the graph is to built as directed. By default false.
        name: Optional[str],
            Name of the graph. By default 'Barbell'.
        
        
        Raises
        -------
        ValueError
            If the edge weights are provided only for a subset."""
    
    
    
    def generate_chain_graph(minimum_node_id: Optional[int], nodes_number: Optional[int], include_selfloops: Optional[bool], node_type: Optional[str], edge_type: Optional[str], weight: Optional[float], directed: Optional[bool], name: Optional[str]):
        """Creates new chain graph with given sizes and types.
        
        Parameters
        ----------
        minimum_node_id: Optional[int],
            Minimum node ID to start with. May be needed when chaining graphs. By default 0.
        nodes_number: Optional[int],
            Number of nodes in the chain. By default 10.
        include_selfloops: Optional[bool],
            Whether to include selfloops.
        node_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        edge_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        weight: Optional[float],
            The weight to use for the edges in the chain. By default None.
        directed: Optional[bool],
            Whether the graph is to built as directed. By default false.
        name: Optional[str],
            Name of the graph. By default 'Chain'."""
    
    
    
    def generate_circle_graph(minimum_node_id: Optional[int], nodes_number: Optional[int], include_selfloops: Optional[bool], node_type: Optional[str], edge_type: Optional[str], weight: Optional[float], directed: Optional[bool], name: Optional[str]):
        """Creates new circle graph with given sizes and types.
        
        Parameters
        ----------
        minimum_node_id: Optional[int],
            Minimum node ID to start with. May be needed when circleing graphs. By default 0.
        nodes_number: Optional[int],
            Number of nodes in the circle. By default 10.
        include_selfloops: Optional[bool],
            Whether to include selfloops.
        node_type: Optional[str],
            The node type to use for the circle. By default 'circle'.
        edge_type: Optional[str],
            The node type to use for the circle. By default 'circle'.
        weight: Optional[float],
            The weight to use for the edges in the circle. By default None.
        directed: Optional[bool],
            Whether the graph is to built as directed. By default false.
        name: Optional[str],
            Name of the graph. By default 'Circle'."""
    
    
    
    def generate_complete_graph(minimum_node_id: Optional[int], nodes_number: Optional[int], include_selfloops: Optional[bool], node_type: Optional[str], edge_type: Optional[str], weight: Optional[float], directed: Optional[bool], name: Optional[str]):
        """Creates new complete graph with given sizes and types.
        
        Parameters
        ----------
        minimum_node_id: Optional[int],
            Minimum node ID to start with. May be needed when combining graphs. By default 0.
        nodes_number: Optional[int],
            Number of nodes in the chain. By default 10.
        include_selfloops: Optional[bool],
            Whether to include selfloops.
        node_type: Optional[str],
            The node type to use. By default 'complete'.
        edge_type: Optional[str],
            The node type to use. By default 'complete'.
        weight: Optional[float],
            The weight to use for the edges. By default None.
        directed: Optional[bool],
            Whether the graph is to built as directed. By default false.
        name: Optional[str],
            Name of the graph. By default 'Complete'."""
    
    
    
    def generate_new_edges_from_node_features(self, features: List[List[float]], neighbours_number: Optional[int], max_degree: Optional[int], distance_name: Optional[str], verbose: Optional[bool]):
        """Returns graph with edges added extracted from given node_features.
        
        This operation might distrupt the graph topology.
        Proceed with caution!
        
        Parameters
        ----------
        features: List[List[float]],
            node_features to use to identify the new neighbours.
        neighbours_number: Optional[int],
            Number of neighbours to add.
        max_degree: Optional[int],
            The maximum degree a node can have its neighbours augmented. By default 0, that is, only singletons are augmented.
        distance_name: Optional[str],
            Name of distance to use. Can either be L2 or COSINE. By default COSINE.
        verbose: Optional[bool],
            Whether to show loading bars.
        
        
        Raises
        -------
        ValueError
            If the graph does not have nodes.
        ValueError
            If the given node_features are not provided exactly for each node.
        ValueError
            If the node_features do not have a consistent shape.
        ValueError
            If the provided number of neighbours is zero."""
    
    
    
    def generate_random_connected_graph(random_state: int, minimum_node_id: int, minimum_node_sampling: int, maximum_node_sampling: int, nodes_number: Optional[int], include_selfloops: Optional[bool], node_type: Optional[str], edge_type: Optional[str], weight: Optional[float], directed: Optional[bool], name: Optional[str]):
        """Creates new random connected graph with given sizes and types.
        
        Parameters
        ----------
        random_state: int,
            The random state to use to reproduce the sampling.
        minimum_node_id: int,
            The minimum node ID for the connected graph.
        minimum_node_sampling: int,
            The minimum amount of nodes to sample per node.
        maximum_node_sampling: int,
            The maximum amount of nodes to sample per node.
        nodes_number: Optional[int],
            Number of nodes in the chain. By default 10.
        include_selfloops: Optional[bool],
            Whether to include selfloops.
        node_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        edge_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        weight: Optional[float],
            The weight to use for the edges in the chain. By default None.
        directed: Optional[bool],
            Whether the graph is to built as directed. By default false.
        name: Optional[str],
            Name of the graph. By default 'Chain'."""
    
    
    
    def generate_random_spanning_tree(random_state: int, minimum_node_id: int, nodes_number: Optional[int], include_selfloops: Optional[bool], node_type: Optional[str], edge_type: Optional[str], weight: Optional[float], directed: Optional[bool], name: Optional[str]):
        """Creates new random connected graph with given sizes and types.
        
        Parameters
        ----------
        random_state: int,
            The random state to use to reproduce the sampling.
        minimum_node_id: int,
            The minimum node ID for the connected graph.
        minimum_node_sampling: int,
            The minimum amount of nodes to sample per node.
        maximum_node_sampling: int,
            The maximum amount of nodes to sample per node.
        nodes_number: Optional[int],
            Number of nodes in the chain. By default 10.
        include_selfloops: Optional[bool],
            Whether to include selfloops.
        node_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        edge_type: Optional[str],
            The node type to use for the chain. By default 'chain'.
        weight: Optional[float],
            The weight to use for the edges in the chain. By default None.
        directed: Optional[bool],
            Whether the graph is to built as directed. By default false.
        name: Optional[str],
            Name of the graph. By default 'Chain'."""
    
    
    
    def get_adamic_adar_index_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the Adamic/Adar Index for the given pair of nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the node IDs are higher than the number of nodes in the graph."""
    
    
    
    def get_adamic_adar_index_from_node_names(self, first_node_name: str, second_node_name: str):
        """Returns the Adamic/Adar Index for the given pair of nodes from the given node names.
        
        Parameters
        ----------
        first_node_name: str,
            Node name of the first node.
        second_node_name: str,
            Node name of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the given node names do not exist in the current graph."""
    
    
    
    def get_all_shortest_paths(self, iterations: Optional[int], verbose: Optional[bool]):
        """Returns graph with unweighted shortest paths computed up to the given depth.
        
        The returned graph will have no selfloops.
        
        Parameters
        ----------
        iterations: Optional[int],
            The number of iterations of the transitive closure to execute. If None, the complete transitive closure is computed.
        verbose: Optional[bool],
            Whether to show a loading bar while building the graph."""
    
    
    
    def get_average_clustering_coefficient(self, low_centrality: Optional[int], verbose: Optional[bool]):
        """Returns the graph average clustering coefficient.
        
        Parameters
        ----------
        low_centrality: Optional[int],
            The threshold over which to switch to parallel matryoshka. By default 50.
        verbose: Optional[bool],
            Whether to show a loading bar."""
    
    
    
    def get_betweenness_centrality(self, normalize: Optional[bool], verbose: Optional[bool]):
        """Returns vector of betweenness centrality for all nodes.
        
        Parameters
        ----------
        normalize: Optional[bool],
            Whether to normalize the values. By default, it is false.
        verbose: Optional[bool],
            Whether to show a loading bar. By default, it is true."""
    
    
    
    def get_bfs_topological_sorting_from_node_id(self, root_node_id: int):
        """Returns topological sorting map using breadth-first search from the given node.
        
        Parameters
        ----------
        root_node_id: int,
            Node ID of node to be used as root of BFS
        
        
        Raises
        -------
        ValueError
            If the given root node ID does not exist in the graph"""
    
    
    
    def get_bipartite_edge_names(self, removed_existing_edges: Optional[bool], first_nodes_set: Optional[Set[str]], second_nodes_set: Optional[Set[str]], first_node_types_set: Optional[Set[str]], second_node_types_set: Optional[Set[str]]):
        """Return vector of tuple of Node IDs that form the edges of the required bipartite graph.
        
        Parameters
        ----------
        removed_existing_edges: Optional[bool],
            Whether to filter out the existing edges. By default, true.
        first_nodes_set: Optional[Set[str]],
            Optional set of nodes to use to create the first set of nodes of the graph.
        second_nodes_set: Optional[Set[str]],
            Optional set of nodes to use to create the second set of nodes of the graph.
        first_node_types_set: Optional[Set[str]],
            Optional set of node types to create the first set of nodes of the graph.
        second_node_types_set: Optional[Set[str]],
            Optional set of node types to create the second set of nodes of the graph."""
    
    
    
    def get_bipartite_edges(self, removed_existing_edges: Optional[bool], first_nodes_set: Optional[Set[str]], second_nodes_set: Optional[Set[str]], first_node_types_set: Optional[Set[str]], second_node_types_set: Optional[Set[str]]):
        """Return vector of tuple of Node IDs that form the edges of the required bipartite graph.
        
        Parameters
        ----------
        removed_existing_edges: Optional[bool],
            Whether to filter out the existing edges. By default, true.
        first_nodes_set: Optional[Set[str]],
            Optional set of nodes to use to create the first set of nodes of the graph.
        second_nodes_set: Optional[Set[str]],
            Optional set of nodes to use to create the second set of nodes of the graph.
        first_node_types_set: Optional[Set[str]],
            Optional set of node types to create the first set of nodes of the graph.
        second_node_types_set: Optional[Set[str]],
            Optional set of node types to create the second set of nodes of the graph."""
    
    
    
    def get_breadth_first_search_from_node_ids(self, src_node_id: int, compute_predecessors: Optional[bool], maximal_depth: Optional[int]):
        """Returns vector of minimum paths distances and vector of nodes predecessors from given source node ID and optional destination node ID.
        
        Parameters
        ----------
        src_node_id: int,
            Node ID root of the tree of minimum paths.
        compute_predecessors: Optional[bool],
            Whether to compute the vector of predecessors.
        maximal_depth: Optional[int],
            The maximal number of iterations to execute the DFS for.
        
        
        Raises
        -------
        ValueError
            If the given source node ID does not exist in the current graph.
        ValueError
            If the given optional destination node ID does not exist in the current graph."""
    
    
    
    def get_breadth_first_search_from_node_names(self, src_node_name: str, dst_node_name: Optional[str], compute_predecessors: Optional[bool], maximal_depth: Optional[int]):
        """Returns vector of minimum paths distances and vector of nodes predecessors from given source node name and optional destination node name.
        
        Parameters
        ----------
        src_node_name: str,
            Node name root of the tree of minimum paths.
        dst_node_name: Optional[str],
            Destination node name.
        compute_predecessors: Optional[bool],
            Whether to compute the vector of predecessors.
        maximal_depth: Optional[int],
            The maximal depth to execute the DFS for.
        
        
        Raises
        -------
        ValueError
            If the weights are to be used and the graph does not have weights.
        ValueError
            If the given source node name does not exist in the current graph.
        ValueError
            If the given optional destination node name does not exist in the current graph."""
    
    
    
    def get_breadth_first_search_random_nodes(self, number_of_nodes_to_sample: int, root_node: int):
        """Return nodes sampled from the neighbourhood of given root nodes.
        
        Parameters
        ----------
        number_of_nodes_to_sample: int,
            The number of nodes to sample.
        root_node: int,
            The root node from .
        
        
        Raises
        -------
        ValueError
            If the number of requested nodes is higher than the number of nodes in the graph.
        ValueError
            If the given root node does not exist in the curret graph instance."""
    
    
    
    def get_clique_edge_names(self, directed: Optional[bool], allow_selfloops: Optional[bool], removed_existing_edges: Optional[bool], allow_node_type_set: Optional[Set[str]], allow_node_set: Optional[Set[str]]):
        """Return vector of tuple of Node names that form the edges of the required clique.
        
        Parameters
        ----------
        directed: Optional[bool],
            Whether to return the edges as directed or undirected. By default, equal to the graph.
        allow_selfloops: Optional[bool],
            Whether to allow self-loops in the clique. By default, equal to the graph.
        removed_existing_edges: Optional[bool],
            Whether to filter out the existing edges. By default, true.
        allow_node_type_set: Optional[Set[str]],
            Node types to include in the clique.
        allow_node_set: Optional[Set[str]],
            Nodes to include i the clique."""
    
    
    
    def get_clique_edges(self, directed: Optional[bool], allow_selfloops: Optional[bool], removed_existing_edges: Optional[bool], allow_node_type_set: Optional[Set[str]], allow_node_set: Optional[Set[str]]):
        """Return vector of tuple of Node IDs that form the edges of the required clique.
        
        Parameters
        ----------
        directed: Optional[bool],
            Whether to return the edges as directed or undirected. By default, equal to the graph.
        allow_selfloops: Optional[bool],
            Whether to allow self-loops in the clique. By default, equal to the graph.
        removed_existing_edges: Optional[bool],
            Whether to filter out the existing edges. By default, true.
        allow_node_type_set: Optional[Set[str]],
            Node types to include in the clique.
        allow_node_set: Optional[Set[str]],
            Nodes to include i the clique."""
    
    
    
    def get_closeness_centrality(self, verbose: Optional[bool]):
        """Return closeness centrality for all nodes.
        
        Parameters
        ----------
        verbose: Optional[bool],
            Whether to show an indicative progress bar."""
    
    
    
    def get_clustering_coefficient(self, low_centrality: Optional[int], verbose: Optional[bool]):
        """Returns the graph clustering coefficient.
        
        Parameters
        ----------
        low_centrality: Optional[int],
            The threshold over which to switch to parallel matryoshka. By default 50.
        verbose: Optional[bool],
            Whether to show a loading bar."""
    
    
    
    def get_clustering_coefficient_per_node(self, low_centrality: Optional[int], verbose: Optional[bool]):
        """Returns clustering coefficients for all nodes in the graph.
        
        Parameters
        ----------
        low_centrality: Optional[int],
            The threshold over which to switch to parallel matryoshka. By default 50.
        verbose: Optional[bool],
            Whether to show a loading bar."""
    
    
    
    def get_comulative_node_degree_from_node_id(self, node_id: int):
        """Returns the comulative node degree up to the given node.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node."""
    
    
    
    def get_connected_components_number(self, verbose: Optional[bool]):
        """Returns number a triple with (number of components, number of nodes of the smallest component, number of nodes of the biggest component )
        
        Parameters
        ----------
        verbose: Optional[bool],
            Whether to show a loading bar or not."""
    
    
    
    def get_connected_nodes_number(self):
        """Returns number of connected nodes in the graph."""
    
    
    
    def get_cumulative_node_degrees(self):
        """Return vector with node cumulative_node_degrees, that is the comulative node degree"""
    
    
    
    def get_degree_centrality(self):
        """Returns vector of unweighted degree centrality for all nodes"""
    
    
    
    def get_dense_binary_adjacency_matrix(self):
        """Returns binary dense adjacency matrix.
        
        Beware of using this method on big graphs!
        It'll use all of your RAM!"""
    
    
    
    def get_dense_nodes_mapping(self):
        """Return mapping from instance not trap nodes to dense nodes"""
    
    
    
    def get_dense_weighted_adjacency_matrix(self, weight: Optional[float]):
        """Returns binary weighted adjacency matrix.
        
        Beware of using this method on big graphs!
        It'll use all of your RAM!
        
        Parameters
        ----------
        weight: Optional[float],
            The weight value to use for absent edges. By default, `0.0`.
        
        
        Raises
        -------
        ValueError
            If the graph does not have edge weights."""
    
    
    
    def get_density(self):
        """Returns density of the graph."""
    
    
    
    def get_destination_names(self, directed: bool):
        """Return vector of the non-unique destination nodes names.
        
        Parameters
        ----------
        directed: bool,
            Whether to filter out the undirected edges."""
    
    
    
    def get_destination_node_id_from_edge_id(self, edge_id: int):
        """Returns destination node ID corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose destination node ID is to be retrieved.
        
        
        Raises
        -------
        ValueError
            If the given edge ID does not exist in the current graph."""
    
    
    
    def get_destination_node_ids(self, directed: bool):
        """Return vector on the (non unique) destination nodes of the graph.
        
        Parameters
        ----------
        directed: bool,
            Whether to filter out the undirected edges."""
    
    
    
    def get_destination_node_name_from_edge_id(self, edge_id: int):
        """Returns destination node name corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose destination node name is to be retrieved.
        
        
        Raises
        -------"""
    
    
    
    def get_diameter(self, ignore_infinity: Optional[bool], verbose: Optional[bool]):
        """Returns diameter of the graph.
        
        Parameters
        ----------
        ignore_infinity: Optional[bool],
            Whether to ignore infinite distances, which are present when in the graph exist multiple components.
        verbose: Optional[bool],
            Whether to show a loading bar.
        
        
        Raises
        -------
        ValueError
            If the graph does not contain nodes."""
    
    
    
    def get_diameter_naive(self, ignore_infinity: Optional[bool], verbose: Optional[bool]):
        """Returns diameter of the graph using naive method.
        
        Note that there exists the non-naive method for undirected graphs
        and it is possible to implement a faster method for directed graphs
        but we still need to get to it, as it will require an updated
        succinct data structure.
        
        Parameters
        ----------
        ignore_infinity: Optional[bool],
            Whether to ignore infinite distances, which are present when in the graph exist multiple components.
        verbose: Optional[bool],
            Whether to show a loading bar.
        
        
        Raises
        -------
        ValueError
            If the graph does not contain nodes."""
    
    
    
    def get_dijkstra_from_node_ids(self, src_node_id: int, maybe_dst_node_id: Optional[int], maybe_dst_node_ids: Optional[List[int]], compute_predecessors: Optional[bool], maximal_depth: Optional[int], use_edge_weights_as_probabilities: Optional[bool]):
        """Returns vector of minimum paths distances and vector of nodes predecessors from given source node ID and optional destination node ID.
        
        Parameters
        ----------
        src_node_id: int,
            Node ID root of the tree of minimum paths.
        maybe_dst_node_id: Optional[int],
            Optional target destination. If provided, Dijkstra will stop upon reaching this node.
        maybe_dst_node_ids: Optional[List[int]],
            Optional target destinations. If provided, Dijkstra will stop upon reaching all of these nodes.
        compute_predecessors: Optional[bool],
            Whether to compute the vector of predecessors.
        maximal_depth: Optional[int],
            The maximal depth to execute the DFS for.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        
        
        Raises
        -------
        ValueError
            If the weights are to be used and the graph does not have weights.
        ValueError
            If the given source node ID does not exist in the current graph.
        ValueError
            If the given optional destination node ID does not exist in the current graph.
        ValueError
            If weights are requested to be treated as probabilities but are not between 0 and 1.
        ValueError
            If the graph contains negative weights."""
    
    
    
    def get_dijkstra_from_node_names(self, src_node_name: str, maybe_dst_node_name: Optional[str], maybe_dst_node_names: Optional[List[str]], compute_predecessors: Optional[bool], maximal_depth: Optional[int], use_edge_weights_as_probabilities: Optional[bool]):
        """Returns vector of minimum paths distances and vector of nodes predecessors from given source node name and optional destination node name.
        
        Parameters
        ----------
        src_node_name: str,
            Node name root of the tree of minimum paths.
        maybe_dst_node_name: Optional[str],
            Optional target destination node name. If provided, Dijkstra will stop upon reaching this node.
        maybe_dst_node_names: Optional[List[str]],
            Optional target destination node names. If provided, Dijkstra will stop upon reaching all of these nodes.
        compute_predecessors: Optional[bool],
            Whether to compute the vector of predecessors.
        maximal_depth: Optional[int],
            The maximal depth to execute the DFS for.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        
        
        Raises
        -------
        ValueError
            If the weights are to be used and the graph does not have weights.
        ValueError
            If the given source node name does not exist in the current graph.
        ValueError
            If the given optional destination node name does not exist in the current graph."""
    
    
    
    def get_directed_destination_node_ids(self):
        """Return vector on the (non unique) directed destination nodes of the graph"""
    
    
    
    def get_directed_edge_node_ids(self):
        """Return vector with the sorted directed edge Ids"""
    
    
    
    def get_directed_edge_node_names(self):
        """Return vector with the sorted directed edge names"""
    
    
    
    def get_directed_edges_number(self):
        """Returns number of directed edges in the graph"""
    
    
    
    def get_directed_modularity_from_node_community_memberships(self):
        """Returns the directed modularity of the graph from the given memberships.
        
        Parameters
        ----------
        
        
        Raises
        -------
        ValueError
            If the number of provided memberships does not match the number of nodes of the graph."""
    
    
    
    def get_directed_source_node_ids(self):
        """Return vector on the (non unique) directed source nodes of the graph"""
    
    
    
    def get_disconnected_nodes_number(self):
        """Returns number of disconnected nodes within the graph.
        A Disconnected node is a node which is nor a singleton nor a singleton
        with selfloops."""
    
    
    
    def get_eccentricity_from_node_id(self, node_id: int):
        """Returns unweighted eccentricity of the given node ID.
        
        Parameters
        ----------
        node_id: int,
            Node for which to compute the eccentricity.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        
        
        Raises
        -------
        ValueError
            If the given node ID does not exist in the graph."""
    
    
    
    def get_eccentricity_from_node_name(self, node_name: str):
        """Returns unweighted eccentricity of the given node name.
        
        Parameters
        ----------
        node_name: str,
            Node for which to compute the eccentricity.
        
        
        Raises
        -------
        ValueError
            If the given node name does not exist in the current graph instance."""
    
    
    
    def get_edge_count_from_edge_type_id(self, edge_type_id: Optional[int]):
        """Return number of edges with given edge type ID.
        
        If None is given as an edge type ID, the unknown edge type IDs
        will be returned.
        
        Parameters
        ----------
        edge_type_id: Optional[int],
            The edge type ID to count the edges of."""
    
    
    
    def get_edge_count_from_edge_type_name(self, edge_type_name: Optional[str]):
        """Return number of edges with given edge type name.
        
        If None is given as an edge type name, the unknown edge types
        will be returned.
        
        Parameters
        ----------
        edge_type_name: Optional[str],
            The edge type name to count the edges of."""
    
    
    
    def get_edge_id_from_node_ids(self, src: int, dst: int):
        """Returns edge ID corresponding to given source and destination node IDs.
        
        Parameters
        ----------
        src: int,
            The source node ID.
        dst: int,
            The destination node ID."""
    
    
    
    def get_edge_id_from_node_ids_and_edge_type_id(self, src: int, dst: int, edge_type: Optional[int]):
        """Return edge ID for given tuple of nodes and edge type.
        
        This method will return an error if the graph does not contain the
        requested edge with edge type.
        
        Parameters
        ----------
        src: int,
            Source node of the edge.
        dst: int,
            Destination node of the edge.
        edge_type: Optional[int],
            Edge Type of the edge."""
    
    
    
    def get_edge_id_from_node_names(self, src_name: str, dst_name: str):
        """Return edge ID for given tuple of node names.
        
        This method will return an error if the graph does not contain the
        requested edge with edge type.
        
        Parameters
        ----------
        src_name: str,
            Source node name of the edge.
        dst_name: str,
            Destination node name of the edge."""
    
    
    
    def get_edge_id_from_node_names_and_edge_type_name(self, src_name: str, dst_name: str, edge_type_name: Optional[str]):
        """Return edge ID for given tuple of node names and edge type name.
        
        This method will return an error if the graph does not contain the
        requested edge with edge type.
        
        Parameters
        ----------
        src_name: str,
            Source node name of the edge.
        dst_name: str,
            Destination node name of the edge.
        edge_type_name: Optional[str],
            Edge type name."""
    
    
    
    def get_edge_ids_with_known_edge_types(self):
        """Returns edge IDs of the edges with known edge types
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_ids_with_known_edge_types_mask(self):
        """Returns a boolean vector that for each node contains whether it has an
        unknown edge type.
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_ids_with_unknown_edge_types(self):
        """Returns edge IDs of the edges with unknown edge types
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_ids_with_unknown_edge_types_mask(self):
        """Returns a boolean vector that for each node contains whether it has an
        unknown node type.
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_label_holdout_graphs(self, train_size: float, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns edge-label holdout for training ML algorithms on the graph edge labels.
        This is commonly used for edge type prediction tasks.
        
        This method returns two graphs, the train and the test one.
        The edges of the graph will be splitted in the train and test graphs according
        to the `train_size` argument.
        
        If stratification is enabled, the train and test will have the same ratios of
        edge types.
        
        Parameters
        ----------
        train_size: float,
            rate target to reserve for training,
        use_stratification: Optional[bool],
            Whether to use edge-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have edge types.
        ValueError
            If stratification is required but the graph has singleton edge types."""
    
    
    
    def get_edge_label_kfold(self, k: int, k_index: int, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns edge-label kfold for training ML algorithms on the graph edge labels.
        This is commonly used for edge type prediction tasks.
        
        This method returns two graphs, the train and the test one.
        The edges of the graph will be splitted in the train and test graphs according
        to the `train_size` argument.
        
        If stratification is enabled, the train and test will have the same ratios of
        edge types.
        
        Parameters
        ----------
        k: int,
            The number of folds.
        k_index: int,
            Which fold to use for the validation.
        use_stratification: Optional[bool],
            Whether to use edge-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have edge types.
        ValueError
            If stratification is required but the graph has singleton edge types."""
    
    
    
    def get_edge_label_random_holdout(self, train_size: float, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns edge-label holdout for training ML algorithms on the graph edge labels.
        This is commonly used for edge type prediction tasks.
        
        This method returns two graphs, the train and the test one.
        The edges of the graph will be splitted in the train and test graphs according
        to the `train_size` argument.
        
        If stratification is enabled, the train and test will have the same ratios of
        edge types.
        
        Parameters
        ----------
        train_size: float,
            rate target to reserve for training,
        use_stratification: Optional[bool],
            Whether to use edge-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have edge types.
        ValueError
            If stratification is required but the graph has singleton edge types."""
    
    
    
    def get_edge_node_ids(self, directed: bool):
        """Return vector with the sorted edge Ids.
        
        Parameters
        ----------
        directed: bool,
            Whether to filter out the undirected edges."""
    
    
    
    def get_edge_node_ids_from_edge_node_names(self, edge_node_names: List[Tuple[str, str]]):
        """Returns result with the edge node IDs.
        
        Parameters
        ----------
        edge_node_names: List[Tuple[str, str]],
            The node names whose node IDs is to be returned.
        
        
        Raises
        -------
        ValueError
            When any of the given node name does not exists in the current graph."""
    
    
    
    def get_edge_node_ids_with_known_edge_types(self, directed: bool):
        """Returns edge node IDs of the edges with known edge types
        
        Parameters
        ----------
        directed: bool,
            Whether to iterated the edges as a directed or undirected edge list.
        
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_node_ids_with_unknown_edge_types(self, directed: bool):
        """Returns edge node IDs of the edges with unknown edge types
        
        Parameters
        ----------
        directed: bool,
            Whether to iterated the edges as a directed or undirected edge list.
        
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_node_names(self, directed: bool):
        """Return vector with the sorted edge names.
        
        Parameters
        ----------
        directed: bool,
            Whether to filter out the undirected edges."""
    
    
    
    def get_edge_node_names_from_edge_node_ids(self, edge_node_ids: List[Tuple[int, int]]):
        """Returns result with the edge node names.
        
        Parameters
        ----------
        edge_node_ids: List[Tuple[int, int]],
            The node names whose node names is to be returned.
        
        
        Raises
        -------
        ValueError
            When any of the given node IDs does not exists in the current graph."""
    
    
    
    def get_edge_node_names_with_known_edge_types(self, directed: bool):
        """Returns edge node names of the edges with known edge types
        
        Parameters
        ----------
        directed: bool,
            Whether to iterated the edges as a directed or undirected edge list.
        
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_node_names_with_unknown_edge_types(self, directed: bool):
        """Returns edge node names of the edges with unknown edge types
        
        Parameters
        ----------
        directed: bool,
            Whether to iterated the edges as a directed or undirected edge list.
        
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_edge_prediction_kfold(self, k: int, k_index: int, edge_types: Optional[List[Optional[str]]], random_state: Optional[int], verbose: Optional[bool]):
        """Returns train and test graph following kfold validation scheme.
        
        The edges are splitted into k chunks. The k_index-th chunk is used to build
        the validation graph, all the other edges create the training graph.
        
        Parameters
        ----------
        k: int,
            The number of folds.
        k_index: int,
            Which fold to use for the validation.
        edge_types: Optional[List[Optional[str]]],
            Edge types to be selected when computing the folds (All the edge types not listed here will be always be used in the training set).
        random_state: Optional[int],
            The random_state (seed) to use for the holdout,
        verbose: Optional[bool],
            Whether to show the loading bar.
        
        
        Raises
        -------
        ValueError
            If the number of requested k folds is one or zero.
        ValueError
            If the given k fold index is greater than the number of k folds.
        ValueError
            If edge types have been specified but it's an empty list.
        ValueError
            If the number of k folds is higher than the number of edges in the graph."""
    
    
    
    def get_edge_type_id_counts_hashmap(self):
        """Returns edge type IDs counts hashmap.
        
        Raises
        -------
        ValueError
            If there are no edge types in the current graph instance."""
    
    
    
    def get_edge_type_id_from_edge_id(self, edge_id: int):
        """Returns edge type of given edge.
        
        Parameters
        ----------
        edge_id: int,
            edge whose edge type is to be returned."""
    
    
    
    def get_edge_type_id_from_edge_type_name(self, edge_type_name: Optional[str]):
        """Return edge type ID curresponding to given edge type name.
        
        If None is given as an edge type ID, None is returned.
        
        Parameters
        ----------
        edge_type_name: Optional[str],
            The edge type name whose ID is to be returned."""
    
    
    
    def get_edge_type_ids(self):
        """Return the edge types of the edges"""
    
    
    
    def get_edge_type_ids_from_edge_type_names(self, edge_type_names: List[Optional[str]]):
        """Return translated edge types from string to internal edge ID.
        
        Parameters
        ----------
        edge_type_names: List[Optional[str]],
            Vector of edge types to be converted."""
    
    
    
    def get_edge_type_name_from_edge_id(self, edge_id: int):
        """Returns option with the edge type of the given edge id.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose edge type is to be returned."""
    
    
    
    def get_edge_type_name_from_edge_type_id(self, edge_type_id: int):
        """Return edge type name of given edge type.
        
        Parameters
        ----------
        edge_type_id: int,
            Id of the edge type."""
    
    
    
    def get_edge_type_names(self):
        """Return the edge types names"""
    
    
    
    def get_edge_type_names_counts_hashmap(self):
        """Returns edge type names counts hashmap.
        
        Raises
        -------
        ValueError
            If there are no edge types in the current graph instance."""
    
    
    
    def get_edge_types_number(self):
        """Returns number of edge types in the graph.
        
        Raises
        -------
        ValueError
            If there are no edge types in the current graph."""
    
    
    
    def get_edge_types_total_memory_requirements(self):
        """Returns how many bytes are currently used to store the edge types"""
    
    
    
    def get_edge_types_total_memory_requirements_human_readable(self):
        """Returns human readable amount of how many bytes are currently used to store the edge types"""
    
    
    
    def get_edge_weight_from_edge_id(self, edge_id: int):
        """Returns weight of the given edge id.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose weight is to be returned."""
    
    
    
    def get_edge_weight_from_node_ids(self, src: int, dst: int):
        """Returns weight of the given node ids.
        
        Parameters
        ----------
        src: int,
            The node ID of the source node.
        dst: int,
            The node ID of the destination node."""
    
    
    
    def get_edge_weight_from_node_ids_and_edge_type_id(self, src: int, dst: int, edge_type: Optional[int]):
        """Returns weight of the given node ids and edge type.
        
        Parameters
        ----------
        src: int,
            The node ID of the source node.
        dst: int,
            The node ID of the destination node.
        edge_type: Optional[int],
            The edge type ID of the edge."""
    
    
    
    def get_edge_weight_from_node_names(self, src_name: str, dst_name: str):
        """Returns weight of the given node names.
        
        Parameters
        ----------
        src_name: str,
            The node name of the source node.
        dst_name: str,
            The node name of the destination node."""
    
    
    
    def get_edge_weight_from_node_names_and_edge_type_name(self, src: str, dst: str, edge_type: Optional[str]):
        """Returns weight of the given node names and edge type.
        
        Parameters
        ----------
        src: str,
            The node name of the source node.
        dst: str,
            The node name of the destination node.
        edge_type: Optional[str],
            The edge type name of the edge."""
    
    
    
    def get_edge_weighting_methods(self):
        """Return list of the supported edge weighting methods"""
    
    
    
    def get_edge_weights(self):
        """Return the weights of the graph edges."""
    
    
    
    def get_edge_weights_total_memory_requirements(self):
        """Returns how many bytes are currently used to store the edge weights"""
    
    
    
    def get_edge_weights_total_memory_requirements_human_readable(self):
        """Returns human readable amount of how many bytes are currently used to store the edge weights"""
    
    
    
    def get_edges_number(self):
        """Returns number of edges of the graph."""
    
    
    
    def get_edges_total_memory_requirement(self):
        """Returns how many bytes are currently used to store the edges"""
    
    
    
    def get_edges_total_memory_requirement_human_readable(self):
        """Returns human readable amount of how many bytes are currently used to store the edges"""
    
    
    
    def get_eigenvector_centrality(self, maximum_iterations_number: Optional[int], tollerance: Optional[float]):
        """Returns vector with unweighted eigenvector centrality.
        
        Parameters
        ----------
        maximum_iterations_number: Optional[int],
            The maximum number of iterations to consider.
        tollerance: Optional[float],
            The maximum error tollerance for convergence."""
    
    
    
    def get_harmonic_centrality(self, verbose: Optional[bool]):
        """Return harmonic centrality for all nodes.
        
        Parameters
        ----------
        verbose: Optional[bool],
            Whether to show an indicative progress bar."""
    
    
    
    def get_jaccard_coefficient_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the Jaccard index for the two given nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the node IDs are higher than the number of nodes in the graph."""
    
    
    
    def get_jaccard_coefficient_from_node_names(self, first_node_name: str, second_node_name: str):
        """Returns the Jaccard index for the two given nodes from the given node names.
        
        Parameters
        ----------
        first_node_name: str,
            Node name of the first node.
        second_node_name: str,
            Node name of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the given node names do not exist in the current graph."""
    
    
    
    def get_k_shortest_path_node_ids_from_node_ids(self, src_node_id: int, dst_node_id: int, k: int):
        """Return vector of the k minimum paths node IDs between given source node and destination node ID.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        k: int,
            Number of paths to find.
        
        
        Raises
        -------
        ValueError
            If any of the given node IDs does not exist in the graph."""
    
    
    
    def get_k_shortest_path_node_ids_from_node_names(self, src_node_name: str, dst_node_name: str, k: int):
        """Return vector of the k minimum paths node IDs between given source node and destination node name.
        
        Parameters
        ----------
        src_node_name: str,
            Source node name.
        dst_node_name: str,
            Destination node name.
        k: int,
            Number of paths to find.
        
        
        Raises
        -------
        ValueError
            If any of the given node names does not exist in the graph."""
    
    
    
    def get_k_shortest_path_node_names_from_node_names(self, src_node_name: str, dst_node_name: str, k: int):
        """Return vector of the k minimum paths node names between given source node and destination node name.
        
        Parameters
        ----------
        src_node_name: str,
            Source node name.
        dst_node_name: str,
            Destination node name.
        k: int,
            Number of paths to find.
        
        
        Raises
        -------
        ValueError
            If any of the given node names does not exist in the graph."""
    
    
    
    def get_known_edge_types_number(self):
        """Returns the number of edge with known edge type.
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_known_edge_types_rate(self):
        """Returns rate of known edge types over total edges number.
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_known_node_types_mask(self):
        """Returns boolean mask of known node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_known_node_types_number(self):
        """Returns the number of node with known node type.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_known_node_types_rate(self):
        """Returns rate of known node types over total nodes number.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_laplacian_coo_matrix_edges_number(self):
        """Returns number of edges in the laplacian COO matrix representation of the graph"""
    
    
    
    def get_laplacian_transformed_graph(self):
        """Returns unweighted laplacian transformation of the graph"""
    
    
    
    def get_max_encodable_edge_number(self):
        """Return maximum encodable edge number"""
    
    
    
    def get_maximum_edge_weight(self):
        """Return the maximum weight, if graph has weights.
        
        Raises
        -------
        ValueError
            If the graph does not contain edge weights."""
    
    
    
    def get_maximum_multilabel_count(self):
        """Returns number of maximum multilabel count.
        
        This value is the maximum number of multilabel counts
        that appear in any given node in the graph"""
    
    
    
    def get_maximum_node_degree(self):
        """Returns maximum node degree of the graph.
        
        Raises
        -------
        ValueError
            If the graph does not contain any node (is an empty graph)."""
    
    
    
    def get_maximum_node_types_number(self):
        """Returns maximum number of node types.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_memory_stats(self):
        """Returns a string describing the memory usage of all the fields of all the
        structures used to store the current graph"""
    
    
    
    def get_minimum_edge_types_number(self):
        """Returns minimum number of edge types.
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_minimum_node_degree(self):
        """Returns minimum node degree of the graph.
        
        Raises
        -------
        ValueError
            If the graph does not contain any node (is an empty graph)."""
    
    
    
    def get_minimum_node_types_number(self):
        """Returns minimum number of node types.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_mininum_edge_weight(self):
        """Return the minimum weight, if graph has weights.
        
        Raises
        -------
        ValueError
            If the graph does not contain edge weights."""
    
    
    
    def get_minmax_edge_ids_from_node_ids(self, src: int, dst: int):
        """Return range of outbound edges IDs for all the edges bewteen the given
        source and destination nodes.
        This operation is meaningfull only in a multigraph.
        
        Parameters
        ----------
        src: int,
            Source node.
        dst: int,
            Destination node."""
    
    
    
    def get_minmax_edge_ids_from_source_node_id(self, src: int):
        """Return range of outbound edges IDs which have as source the given Node.
        
        Parameters
        ----------
        src: int,
            Node for which we need to compute the cumulative_node_degrees range."""
    
    
    
    def get_most_central_node_id(self):
        """Returns maximum node degree of the graph."""
    
    
    
    def get_multiple_node_type_ids_from_node_type_names(self, node_type_names: List[Optional[List[str]]]):
        """Return translated node types from string to internal node ID.
        
        Parameters
        ----------
        node_type_names: List[Optional[List[str]]],
            Vector of node types to be converted.
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If any of the given node type names do not exists in the graph."""
    
    
    
    def get_name(self):
        """Return name of the graph."""
    
    
    
    def get_neighbour_node_ids_from_node_id(self, node_id: int):
        """Return vector of destinations for the given source node ID.
        
        Parameters
        ----------
        node_id: int,
            Node ID whose neighbours are to be retrieved."""
    
    
    
    def get_neighbour_node_ids_from_node_name(self, node_name: str):
        """Return vector of destinations for the given source node name.
        
        Parameters
        ----------
        node_name: str,
            Node ID whose neighbours are to be retrieved."""
    
    
    
    def get_neighbour_node_names_from_node_name(self, node_name: str):
        """Return vector of destination names for the given source node name.
        
        Parameters
        ----------
        node_name: str,
            Node name whose neighbours are to be retrieved."""
    
    
    
    def get_node_connected_component_ids(self, verbose: Optional[bool]):
        """Return a vector with the components each node belongs to.
        
        E.g. If we have two components `[0, 2, 3]` and `[1, 4, 5]` the result will look like
        `[0, 1, 0, 0, 1, 1]`
        
        Parameters
        ----------
        verbose: Optional[bool],
            Whether to show the loading bar."""
    
    
    
    def get_node_count_from_node_type_id(self, node_type_id: Optional[int]):
        """Return number of nodes with given node type ID.
        
        If None is given as an node type ID, the unknown node types
        will be returned.
        
        Parameters
        ----------
        node_type_id: Optional[int],
            The node type ID to count the nodes of."""
    
    
    
    def get_node_count_from_node_type_name(self, node_type_name: Optional[str]):
        """Return number of nodes with given node type name.
        
        If None is given as an node type name, the unknown node types
        will be returned.
        
        Parameters
        ----------
        node_type_name: Optional[str],
            The node type name to count the nodes of."""
    
    
    
    def get_node_degree_from_node_id(self, node_id: int):
        """Returns the number of outbound neighbours of given node ID.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node."""
    
    
    
    def get_node_degree_from_node_name(self, node_name: str):
        """Returns the number of outbound neighbours of given node name.
        
        Parameters
        ----------
        node_name: str,
            Integer ID of the node.
        
        
        Raises
        -------
        ValueError
            If the given node name does not exist in the graph."""
    
    
    
    def get_node_degrees(self):
        """Returns the unweighted degree of every node in the graph"""
    
    
    
    def get_node_degrees_mean(self):
        """Returns unweighted mean node degree of the graph."""
    
    
    
    def get_node_degrees_median(self):
        """Returns unweighted median node degree of the graph"""
    
    
    
    def get_node_degrees_mode(self):
        """Returns mode node degree of the graph."""
    
    
    
    def get_node_id_from_node_name(self, node_name: str):
        """Returns result with the node ID.
        
        Parameters
        ----------
        node_name: str,
            The node name whose node ID is to be returned.
        
        
        Raises
        -------
        ValueError
            When the given node name does not exists in the current graph."""
    
    
    
    def get_node_ids(self):
        """Return vector with the sorted nodes Ids"""
    
    
    
    def get_node_ids_and_edge_type_id_and_edge_weight_from_edge_id(self, edge_id: int):
        """Return the src, dst, edge type and weight of a given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source, destination, edge type and weight are to be retrieved."""
    
    
    
    def get_node_ids_and_edge_type_id_from_edge_id(self, edge_id: int):
        """Return the src, dst, edge type of a given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source, destination and edge type are to be retrieved."""
    
    
    
    def get_node_ids_from_edge_id(self, edge_id: int):
        """Returns node names corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source and destination node IDs are to e retrieved."""
    
    
    
    def get_node_ids_from_node_names(self, node_names: List[str]):
        """Returns result with the node IDs.
        
        Parameters
        ----------
        node_names: List[str],
            The node names whose node IDs is to be returned.
        
        
        Raises
        -------
        ValueError
            When any of the given node name does not exists in the current graph."""
    
    
    
    def get_node_ids_with_known_node_types(self):
        """Returns node IDs of the nodes with known node types
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_node_ids_with_known_node_types_mask(self):
        """Returns a boolean vector that for each node contains whether it has an
        known node type.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_node_ids_with_unknown_node_types(self):
        """Returns node IDs of the nodes with unknown node types
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_node_ids_with_unknown_node_types_mask(self):
        """Returns a boolean vector that for each node contains whether it has an
        unknown node type.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_node_indegrees(self):
        """Return the indegree for each node."""
    
    
    
    def get_node_label_holdout_graphs(self, train_size: float, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns node-label holdout for training ML algorithms on the graph node labels.
        
        Parameters
        ----------
        train_size: float,
            rate target to reserve for training,
        use_stratification: Optional[bool],
            Whether to use node-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If stratification is requested but the graph has a single node type.
        ValueError
            If stratification is requested but the graph has a multilabel node types."""
    
    
    
    def get_node_label_holdout_indices(self, train_size: float, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns node-label holdout indices for training ML algorithms on the graph node labels.
        
        Parameters
        ----------
        train_size: float,
            rate target to reserve for training,
        use_stratification: Optional[bool],
            Whether to use node-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If stratification is requested but the graph has a single node type.
        ValueError
            If stratification is requested but the graph has a multilabel node types."""
    
    
    
    def get_node_label_holdout_labels(self, train_size: float, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns node-label holdout indices for training ML algorithms on the graph node labels.
        
        Parameters
        ----------
        train_size: float,
            rate target to reserve for training,
        use_stratification: Optional[bool],
            Whether to use node-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If stratification is requested but the graph has a single node type.
        ValueError
            If stratification is requested but the graph has a multilabel node types."""
    
    
    
    def get_node_label_kfold(self, k: int, k_index: int, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns node-label fold for training ML algorithms on the graph node labels.
        
        Parameters
        ----------
        k: int,
            The number of folds.
        k_index: int,
            Which fold to use for the validation.
        use_stratification: Optional[bool],
            Whether to use node-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If stratification is requested but the graph has a single node type.
        ValueError
            If stratification is requested but the graph has a multilabel node types."""
    
    
    
    def get_node_label_random_holdout(self, train_size: float, use_stratification: Optional[bool], random_state: Optional[int]):
        """Returns node-label holdout for training ML algorithms on the graph node labels.
        
        Parameters
        ----------
        train_size: float,
            rate target to reserve for training,
        use_stratification: Optional[bool],
            Whether to use node-label stratification,
        random_state: Optional[int],
            The random_state to use for the holdout,
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If stratification is requested but the graph has a single node type.
        ValueError
            If stratification is requested but the graph has a multilabel node types."""
    
    
    
    def get_node_name_from_node_id(self, node_id: int):
        """Returns result with the node name.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose name is to be returned."""
    
    
    
    def get_node_names(self):
        """Return vector with the sorted nodes names"""
    
    
    
    def get_node_names_from_edge_id(self, edge_id: int):
        """Returns node names corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source and destination node IDs are to e retrieved."""
    
    
    
    def get_node_names_with_known_node_types(self):
        """Returns node names of the nodes with known node types
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_node_names_with_unknown_node_types(self):
        """Returns node names of the nodes with unknown node types
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_node_ontologies(self):
        """Return vector with the node predicted ontology."""
    
    
    
    def get_node_report_from_node_id(self, node_id: int):
        """Return human-readable html report of the given node.
        
        The report, by default, is rendered using html.
        
        Parameters
        ----------
        node_id: int,
            Whether to show a loading bar in graph operations."""
    
    
    
    def get_node_report_from_node_name(self, node_name: str):
        """Return human-readable html report of the given node.
        
        The report, by default, is rendered using html.
        
        Parameters
        ----------
        node_name: str,
            Whether to show a loading bar in graph operations."""
    
    
    
    def get_node_sampling_methods(self):
        """Return list of the supported node sampling methods"""
    
    
    
    def get_node_type_id_counts_hashmap(self):
        """Returns node type IDs counts hashmap.
        
        Raises
        -------
        ValueError
            If there are no node types in the current graph instance."""
    
    
    
    def get_node_type_id_from_node_type_name(self, node_type_name: str):
        """Return node type ID curresponding to given node type name.
        
        If None is given as an node type ID, None is returned.
        
        Parameters
        ----------
        node_type_name: str,
            The node type name whose ID is to be returned."""
    
    
    
    def get_node_type_ids(self):
        """Return the node types of the graph nodes."""
    
    
    
    def get_node_type_ids_from_node_id(self, node_id: int):
        """Returns node type of given node.
        
        Parameters
        ----------
        node_id: int,
            node whose node type is to be returned."""
    
    
    
    def get_node_type_ids_from_node_name(self, node_name: str):
        """Return node type ID for the given node name if available.
        
        Parameters
        ----------
        node_name: str,
            Name of the node."""
    
    
    
    def get_node_type_ids_from_node_type_names(self, node_type_names: List[Optional[str]]):
        """Return translated node types from string to internal node ID.
        
        Parameters
        ----------
        node_type_names: List[Optional[str]],
            Vector of node types to be converted."""
    
    
    
    def get_node_type_name_from_node_name(self, node_name: str):
        """Return node type name for the given node name if available.
        
        Parameters
        ----------
        node_name: str,
            Name of the node."""
    
    
    
    def get_node_type_name_from_node_type_id(self, node_type_id: int):
        """Return node type name of given node type.
        
        There is no need for a unchecked version since we will have to map
        on the note_types anyway.
        
        Parameters
        ----------
        node_type_id: int,
            Id of the node type."""
    
    
    
    def get_node_type_names(self):
        """Return the node types names."""
    
    
    
    def get_node_type_names_counts_hashmap(self):
        """Returns node type names counts hashmap.
        
        Raises
        -------
        ValueError
            If there are no node types in the current graph instance."""
    
    
    
    def get_node_type_names_from_node_id(self, node_id: int):
        """Returns result of option with the node type of the given node id.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose node types are to be returned.
        
        
        Raises
        -------
        ValueError
            If the node types are not available for the current graph instance."""
    
    
    
    def get_node_type_names_from_node_name(self, node_name: str):
        """Returns result of option with the node type of the given node name.
        
        Parameters
        ----------
        node_name: str,
            The node name whose node types are to be returned."""
    
    
    
    def get_node_types_number(self):
        """Returns number of node types in the graph.
        
        Raises
        -------
        ValueError
            If there are no node types in the current graph."""
    
    
    
    def get_node_types_total_memory_requirements(self):
        """Returns how many bytes are currently used to store the node types"""
    
    
    
    def get_node_types_total_memory_requirements_human_readable(self):
        """Returns human readable amount of how many bytes are currently used to store the node types"""
    
    
    
    def get_node_urls(self):
        """Return vector with the node URLs."""
    
    
    
    def get_nodes_mapping(self):
        """Return the nodes mapping"""
    
    
    
    def get_nodes_number(self):
        """Returns number of nodes in the graph"""
    
    
    
    def get_nodes_total_memory_requirement(self):
        """Returns how many bytes are currently used to store the nodes"""
    
    
    
    def get_nodes_total_memory_requirement_human_readable(self):
        """Returns human readable amount of how many bytes are currently used to store the nodes"""
    
    
    
    def get_not_singletons_node_ids(self):
        """Return set of nodes that are not singletons"""
    
    
    
    def get_number_of_triangles(self, normalize: Optional[bool], low_centrality: Optional[int], verbose: Optional[bool]):
        """Returns total number of triangles ignoring the weights.
        
        The method dispatches the fastest method according to the current
        graph instance. Specifically:
        - For directed graphs it will use the naive algorithm.
        - For undirected graphs it will use Bader's version.
        
        Parameters
        ----------
        normalize: Optional[bool],
            Whether to normalize the number of triangles.
        low_centrality: Optional[int],
            The threshold over which to switch to parallel matryoshka. By default 50.
        verbose: Optional[bool],
            Whether to show a loading bar."""
    
    
    
    def get_number_of_triangles_per_node(self, normalize: Optional[bool], low_centrality: Optional[int], verbose: Optional[bool]):
        """Returns number of triangles in the graph without taking into account the weights.
        
        The method dispatches the fastest method according to the current
        graph instance. Specifically:
        - For directed graphs it will use the naive algorithm.
        - For undirected graphs it will use Bader's version.
        
        Parameters
        ----------
        normalize: Optional[bool],
            Whether to normalize the number of triangles.
        low_centrality: Optional[int],
            The threshold over which to switch to parallel matryoshka. By default 50.
        verbose: Optional[bool],
            Whether to show a loading bar."""
    
    
    
    def get_okapi_bm25_node_feature_propagation(self, features: List[Optional[List[float]]], iterations: Optional[int], maximal_distance: Optional[int], k1: Optional[float], b: Optional[float], include_central_node: Optional[bool], verbose: Optional[bool]):
        """Returns okapi node features propagation within given maximal distance.
        
        Parameters
        ----------
        features: List[Optional[List[float]]],
            The features to propagate. Use None to represent eventual unknown features.
        iterations: Optional[int],
            The number of iterations to execute. By default one.
        maximal_distance: Optional[int],
            The distance to consider for the cooccurrences. The default value is 3.
        k1: Optional[float],
            The k1 parameter from okapi. Tipicaly between 1.2 and 2.0. It can be seen as a smoothing.
        b: Optional[float],
            The b parameter from okapi. Tipicaly 0.75.
        include_central_node: Optional[bool],
            Whether to include the central node. By default true.
        verbose: Optional[bool],
            Whether to show loading bar.
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_okapi_bm25_node_label_propagation(self, iterations: Optional[int], maximal_distance: Optional[int], k1: Optional[float], b: Optional[float], verbose: Optional[bool]):
        """Returns okapi node label propagation within given maximal distance.
        
        Parameters
        ----------
        iterations: Optional[int],
            The number of iterations to execute. By default one.
        maximal_distance: Optional[int],
            The distance to consider for the cooccurrences. The default value is 3.
        k1: Optional[float],
            The k1 parameter from okapi. Tipicaly between 1.2 and 2.0. It can be seen as a smoothing.
        b: Optional[float],
            The b parameter from okapi. Tipicaly 0.75.
        verbose: Optional[bool],
            Whether to show loading bar.
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_one_hot_encoded_edge_types(self):
        """Returns one-hot encoded edge types.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def get_one_hot_encoded_known_edge_types(self):
        """Returns one-hot encoded known edge types.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def get_one_hot_encoded_known_node_types(self):
        """Returns one-hot encoded known node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_one_hot_encoded_node_types(self):
        """Returns one-hot encoded node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_parallel_edges_number(self):
        """Return number of edges that have multigraph syblings"""
    
    
    
    def get_preferential_attachment_from_node_ids(self, source_node_id: int, destination_node_id: int, normalize: bool):
        """Returns the unweighted preferential attachment from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        normalize: bool,
            Whether to normalize by the square of maximum degree.
        
        
        Raises
        -------
        ValueError
            If either of the node IDs are higher than the number of nodes in the graph."""
    
    
    
    def get_preferential_attachment_from_node_names(self, first_node_name: str, second_node_name: str, normalize: bool):
        """Returns the unweighted preferential attachment from the given node names.
        
        Parameters
        ----------
        first_node_name: str,
            Node name of the first node.
        second_node_name: str,
            Node name of the second node.
        normalize: bool,
            Whether to normalize by the square of maximum degree.
        
        
        Raises
        -------
        ValueError
            If either of the given node names do not exist in the current graph."""
    
    
    
    def get_random_nodes(self, number_of_nodes_to_sample: int, random_state: int):
        """Return random unique sorted numbers.
        
        Parameters
        ----------
        number_of_nodes_to_sample: int,
            The number of nodes to sample.
        random_state: int,
            The random state to use to reproduce the sampling."""
    
    
    
    def get_random_subgraph(self, nodes_number: int, random_state: Optional[int], verbose: Optional[bool]):
        """Returns subgraph with given number of nodes.
        
        **This method creates a subset of the graph starting from a random node
        sampled using given random_state and includes all neighbouring nodes until
        the required number of nodes is reached**. All the edges connecting any
        of the selected nodes are then inserted into this graph.
        
        This is meant to execute distributed node embeddings.
        It may also sample singleton nodes.
        
        Parameters
        ----------
        nodes_number: int,
            Number of nodes to extract.
        random_state: Optional[int],
            Random random_state to use.
        verbose: Optional[bool],
            Whether to show the loading bar.
        
        
        Raises
        -------
        ValueError
            If the requested number of nodes is one or less.
        ValueError
            If the graph has less than the requested number of nodes."""
    
    
    
    def get_random_walk_normalized_laplacian_transformed_graph(self):
        """Returns unweighted random walk normalized laplacian transformation of the graph"""
    
    
    
    def get_resource_allocation_index_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the unweighted Resource Allocation Index for the given pair of nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the node IDs are higher than the number of nodes in the graph."""
    
    
    
    def get_resource_allocation_index_from_node_names(self, first_node_name: str, second_node_name: str):
        """Returns the unweighted Resource Allocation Index for the given pair of nodes from the given node names.
        
        Parameters
        ----------
        first_node_name: str,
            Node name of the first node.
        second_node_name: str,
            Node name of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the given node names do not exist in the current graph."""
    
    
    
    def get_reversed_bfs_topological_sorting_from_node_id(self, root_node_id: int):
        """Returns topological sorting reversed map using breadth-first search from the given node.
        
        Parameters
        ----------
        root_node_id: int,
            Node ID of node to be used as root of BFS
        
        
        Raises
        -------
        ValueError
            If the given root node ID does not exist in the graph"""
    
    
    
    def get_selfloop_nodes_rate(self):
        """Returns rate of self-loops."""
    
    
    
    def get_selfloops_number(self):
        """Returns number of self-loops, including also those in eventual multi-edges."""
    
    
    
    def get_shortest_path_node_ids_from_node_ids(self, src_node_id: int, dst_node_id: int, maximal_depth: Optional[int]):
        """Returns minimum path node names from given node ids.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        
        
        Raises
        -------
        ValueError
            If any of the given node IDs do not exist in the current graph."""
    
    
    
    def get_shortest_path_node_ids_from_node_names(self, src_node_name: str, dst_node_name: str, maximal_depth: Optional[int]):
        """Returns minimum path node names from given node names.
        
        Parameters
        ----------
        src_node_name: str,
            Source node name.
        dst_node_name: str,
            Destination node name.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        
        
        Raises
        -------
        ValueError
            If any of the given node names do not exist in the current graph."""
    
    
    
    def get_shortest_path_node_names_from_node_names(self, src_node_name: str, dst_node_name: str, maximal_depth: Optional[int]):
        """Returns minimum path node names from given node names.
        
        Parameters
        ----------
        src_node_name: str,
            Source node name.
        dst_node_name: str,
            Destination node name.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        
        
        Raises
        -------
        ValueError
            If any of the given node names do not exist in the current graph."""
    
    
    
    def get_singleton_edge_type_ids(self):
        """Returns vector of singleton edge types IDs.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def get_singleton_edge_type_names(self):
        """Returns vector of singleton edge types names.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def get_singleton_edge_types_number(self):
        """Returns number of singleton edge types.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def get_singleton_node_ids(self):
        """Returns vector of singleton node IDs of the graph."""
    
    
    
    def get_singleton_node_names(self):
        """Returns vector of singleton node names of the graph."""
    
    
    
    def get_singleton_node_type_ids(self):
        """Returns vector of singleton node types IDs.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_singleton_node_type_names(self):
        """Returns vector of singleton node types names.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_singleton_node_types_number(self):
        """Returns number of singleton node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_singleton_nodes_number(self):
        """Returns number of singleton nodes within the graph."""
    
    
    
    def get_singleton_nodes_with_selfloops_number(self):
        """Returns number of singleton nodes with selfloops within the graph."""
    
    
    
    def get_singleton_with_selfloops_node_ids(self):
        """Returns vector of singleton_with_selfloops node IDs of the graph."""
    
    
    
    def get_singleton_with_selfloops_node_names(self):
        """Returns vector of singleton_with_selfloops node names of the graph."""
    
    
    
    def get_source_names(self, directed: bool):
        """Return vector of the non-unique source nodes names.
        
        Parameters
        ----------
        directed: bool,
            Whether to filter out the undirected edges."""
    
    
    
    def get_source_node_id_from_edge_id(self, edge_id: int):
        """Returns source node ID corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source node ID is to be retrieved.
        
        
        Raises
        -------
        ValueError
            If the given edge ID does not exist in the current graph."""
    
    
    
    def get_source_node_ids(self, directed: bool):
        """Return vector of the non-unique source nodes.
        
        Parameters
        ----------
        directed: bool,
            Whether to filter out the undirected edges."""
    
    
    
    def get_source_node_name_from_edge_id(self, edge_id: int):
        """Returns source node name corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source node name is to be retrieved.
        
        
        Raises
        -------"""
    
    
    
    def get_sparse_edge_weighting_methods(self):
        """Return list of the supported sparse edge weighting methods"""
    
    
    
    def get_star_edge_names(self, central_node: str, removed_existing_edges: Optional[bool], star_points_nodes_set: Optional[Set[str]], star_points_node_types_set: Optional[Set[str]]):
        """Return vector of tuple of Node names that form the edges of the required star.
        
        Parameters
        ----------
        central_node: str,
            Name of the node to use as center of the star.
        removed_existing_edges: Optional[bool],
            Whether to filter out the existing edges. By default, true.
        star_points_nodes_set: Optional[Set[str]],
            Optional set of nodes to use to create the set of star points.
        star_points_node_types_set: Optional[Set[str]],
            Optional set of node types to create the set of star points."""
    
    
    
    def get_star_edges(self, central_node: str, removed_existing_edges: Optional[bool], star_points_nodes_set: Optional[Set[str]], star_points_node_types_set: Optional[Set[str]]):
        """Return vector of tuple of Node IDs that form the edges of the required star.
        
        Parameters
        ----------
        central_node: str,
            Name of the node to use as center of the star.
        removed_existing_edges: Optional[bool],
            Whether to filter out the existing edges. By default, true.
        star_points_nodes_set: Optional[Set[str]],
            Optional set of nodes to use to create the set of star points.
        star_points_node_types_set: Optional[Set[str]],
            Optional set of node types to create the set of star points."""
    
    
    
    def get_stress_centrality(self, normalize: Optional[bool], verbose: Optional[bool]):
        """Returns vector of stress centrality for all nodes.
        
        Parameters
        ----------
        normalize: Optional[bool],
            Whether to normalize the values. By default, it is false.
        verbose: Optional[bool],
            Whether to show a loading bar. By default, it is true."""
    
    
    
    def get_subsampled_nodes(self, number_of_nodes_to_sample: int, random_state: int, root_node: Optional[int], node_sampling_method: str, unique: Optional[bool]):
        """Return subsampled nodes according to the given method and parameters.
        
        Parameters
        ----------
        number_of_nodes_to_sample: int,
            The number of nodes to sample.
        random_state: int,
            The random state to reproduce the sampling.
        root_node: Optional[int],
            The (optional) root node to use to sample. In not provided, a random one is sampled.
        node_sampling_method: str,
            The method to use to sample the nodes. Can either be random nodes, breath first search-based or uniform random walk-based.
        unique: Optional[bool],
            Whether to make the sampled nodes unique.
        
        
        Raises
        -------
        ValueError
            If the given node sampling method is not supported."""
    
    
    
    def get_symmetric_normalized_laplacian_transformed_graph(self):
        """Returns unweighted symmetric normalized laplacian transformation of the graph.
        
        Raises
        -------
        ValueError
            The graph must be undirected, as we do not currently support this transformation for directed graphs."""
    
    
    
    def get_symmetric_normalized_transformed_graph(self):
        """Returns unweighted symmetric normalized transformation of the graph.
        
        Raises
        -------
        ValueError
            The graph must be undirected, as we do not currently support this transformation for directed graphs."""
    
    
    
    def get_top_k_central_node_ids(self, k: int):
        """Return vector with unweighted top k central node Ids.
        
        If the k passed is bigger than the number of nodes this method will return
        all the nodes in the graph.
        
        Parameters
        ----------
        k: int,
            Number of central nodes to extract.
        
        
        Raises
        -------
        ValueError
            If the given value k is zero.
        ValueError
            If the graph has no nodes."""
    
    
    
    def get_top_k_central_node_names(self, k: int):
        """Return vector with top k central node names.
        
        Parameters
        ----------
        k: int,
            Number of central nodes to extract."""
    
    
    
    def get_total_edge_weights(self):
        """Return total edge weights, if graph has weights.
        
        Raises
        -------
        ValueError
            If the graph does not contain edge weights."""
    
    
    
    def get_total_memory_used(self):
        """Returns how many bytes are currently used to store the given graph"""
    
    
    
    def get_transitive_closure(self, iterations: Optional[int], verbose: Optional[bool]):
        """Returns graph to the i-th transitivity closure iteration.
        
        Parameters
        ----------
        iterations: Optional[int],
            The number of iterations of the transitive closure to execute. If None, the complete transitive closure is computed.
        verbose: Optional[bool],
            Whether to show a loading bar while building the graph."""
    
    
    
    def get_transitivity(self, low_centrality: Optional[int], verbose: Optional[bool]):
        """Returns transitivity of the graph without taking into account weights.
        
        Parameters
        ----------
        low_centrality: Optional[int],
            The threshold over which to switch to parallel matryoshka. By default 50.
        verbose: Optional[bool],
            Whether to show a loading bar."""
    
    
    
    def get_trap_nodes_number(self):
        """Return the number of traps (nodes without any outgoing edges that are not singletons)
        This also includes nodes with only a self-loops, therefore singletons with
        only a self-loops are not considered traps because you could make a walk on them."""
    
    
    
    def get_trap_nodes_rate(self):
        """Returns the traps rate of the graph.
        
        THIS IS EXPERIMENTAL AND MUST BE PROVEN!"""
    
    
    
    def get_triads_number(self):
        """Returns total number of triads in the graph without taking into account weights"""
    
    
    
    def get_unchecked_adamic_adar_index_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the Adamic/Adar Index for the given pair of nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Safety
        ------
        If either of the provided one and two node IDs are higher than the
         number of nodes in the graph."""
    
    
    
    def get_unchecked_all_edge_metrics_from_node_ids(self, source_node_id: int, destination_node_id: int, normalize: bool):
        """Returns all the implemented edge metrics for the two given node IDs.
        
        Specifically, the returned values are:
        * Adamic Adar
        * Jaccard coefficient
        * Resource allocation index
        * Preferential attachment
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        normalize: bool,
            Whether to normalize within 0 to 1.
        
        
        Safety
        ------
        If the given node IDs do not exist in the graph this method will panic."""
    
    
    
    def get_unchecked_breadth_first_search_from_node_ids(self, src_node_id: int, compute_predecessors: Optional[bool], maximal_depth: Optional[int]):
        """Returns vector of minimum paths distances and vector of nodes predecessors, if requested.
        
        Parameters
        ----------
        src_node_id: int,
            Root of the tree of minimum paths.
        maybe_dst_node_id: Optional[int],
            Optional target destination. If provided, Dijkstra will stop upon reaching this node.
        maybe_dst_node_ids: Optional[List[int]],
            Optional target destinations. If provided, Dijkstra will stop upon reaching all of these nodes.
        compute_distances: Optional[bool],
            Whether to compute the vector of distances.
        compute_predecessors: Optional[bool],
            Whether to compute the vector of predecessors.
        compute_visited: Optional[bool],
            Whether to compute the vector of visited nodes.
        maximal_depth: Optional[int],
            The maximal depth to execute the DFS for.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic.
        
         TODO! Explore chains accelerations!"""
    
    
    
    def get_unchecked_closeness_centrality_from_node_id(self, node_id: int):
        """Return closeness centrality of the requested node.
        
        If the given node ID does not exist in the current graph the method
        will panic.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose closeness centrality is to be computed.
        verbose: Optional[bool],
            Whether to show an indicative progress bar.
        
        
        Safety
        ------
        If the given node ID does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_comulative_node_degree_from_node_id(self, node_id: int):
        """Returns the comulative node degree up to the given node.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node.
        
        
        Safety
        ------
        If the given node ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_destination_node_id_from_edge_id(self, edge_id: int):
        """Returns the destination of given edge id without making any boundary check.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose destination is to be retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will cause an out of bounds."""
    
    
    
    def get_unchecked_destination_node_name_from_edge_id(self, edge_id: int):
        """Returns destination node name corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose destination node name is to be retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_dijkstra_from_node_ids(self, src_node_id: int, maybe_dst_node_id: Optional[int], maybe_dst_node_ids: Optional[List[int]], compute_predecessors: bool, maximal_depth: Optional[int], use_edge_weights_as_probabilities: Optional[bool]):
        """Returns vector of minimum paths distances and vector of nodes predecessors, if requested.
        
        Parameters
        ----------
        src_node_id: int,
            Root of the tree of minimum paths.
        maybe_dst_node_id: Optional[int],
            Optional target destination. If provided, Dijkstra will stop upon reaching this node.
        maybe_dst_node_ids: Optional[List[int]],
            Optional target destinations. If provided, Dijkstra will stop upon reaching all of these nodes.
        compute_predecessors: bool,
            Whether to compute the vector of predecessors.
        maximal_depth: Optional[int],
            The maximal number of iterations to execute Dijkstra for.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_eccentricity_from_node_id(self, node_id: int):
        """Returns unweighted eccentricity of the given node.
        
        This method will panic if the given node ID does not exists in the graph.
        
        Parameters
        ----------
        node_id: int,
            Node for which to compute the eccentricity.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_edge_count_from_edge_type_id(self, edge_type: Optional[int]):
        """Return number of edges of the given edge type without checks.
        
        Parameters
        ----------
        edge_type: Optional[int],
            The edge type to retrieve count of.
        
        
        Safety
        ------
        If the given edge type ID does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_edge_id_from_node_ids(self, src: int, dst: int):
        """Returns edge ID corresponding to given source and destination node IDs.
        
        The method will panic if the given source and destination node IDs do
        not correspond to an edge in this graph instance.
        
        Parameters
        ----------
        src: int,
            The source node ID.
        dst: int,
            The destination node ID.
        
        
        Safety
        ------
        If any of the given node IDs do not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_edge_id_from_node_ids_and_edge_type_id(self, src: int, dst: int, edge_type: Optional[int]):
        """Return edge ID without any checks for given tuple of nodes and edge type.
        
        Parameters
        ----------
        src: int,
            Source node of the edge.
        dst: int,
            Destination node of the edge.
        edge_type: Optional[int],
            Edge Type of the edge.
        
        
        Safety
        ------
        If the given node IDs or edge type does not exists in the graph this method will panic."""
    
    
    
    def get_unchecked_edge_type_id_from_edge_id(self, edge_id: int):
        """Returns edge type of given edge.
        
        This method will panic if the given edge ID is greater than
        the number of edges in the graph.
        Furthermore, if the graph does NOT have edge types, it will NOT
        return neither an error or a panic.
        
        Parameters
        ----------
        edge_id: int,
            edge whose edge type is to be returned.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_edge_type_id_from_edge_type_name(self, edge_type_name: str):
        """Return edge type ID corresponding to the given edge type name.
        
        Parameters
        ----------
        edge_type_name: str,
            The edge type name whose edge type ID is to be returned.
        
        
        Safety
        ------
        If the given edge type name does not exists in the considered graph the method will panic."""
    
    
    
    def get_unchecked_edge_type_name_from_edge_type_id(self, edge_type_id: Optional[int]):
        """Return edge type ID corresponding to the given edge type name
        raising panic if edge type ID does not exists in current graph.
        
        Parameters
        ----------
        edge_type_id: Optional[int],
            The edge type naIDme whose edge type name is to be returned.
        
        
        Safety
        ------
        If the given edge type ID does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_edge_weight_from_edge_id(self, edge_id: int):
        """Returns option with the weight of the given edge id.
        
        This method will raise a panic if the given edge ID is higher than
        the number of edges in the graph. Additionally, it will simply
        return None if there are no graph weights.
        
        Parameters
        ----------
        edge_id: int,
            The edge whose edge weight is to be returned.
        
        
        Safety
        ------
        If the given edge ID does not exists in the graph this method will panic."""
    
    
    
    def get_unchecked_edge_weight_from_node_ids(self, src: int, dst: int):
        """Returns option with the weight of the given node ids.
        
        This method will raise a panic if the given node IDs are higher than
        the number of nodes in the graph.
        
        Parameters
        ----------
        src: int,
            The source node ID.
        dst: int,
            The destination node ID.
        
        
        Safety
        ------
        If either of the two given node IDs does not exists in the graph."""
    
    
    
    def get_unchecked_harmonic_centrality_from_node_id(self, node_id: int):
        """Return harmonic centrality of the requested node.
        
        If the given node ID does not exist in the current graph the method
        will panic.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose harmonic centrality is to be computed.
        
        
        Safety
        ------
        If the given node ID does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_jaccard_coefficient_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the Jaccard index for the two given nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Safety
        ------
        If either of the provided one and two node IDs are higher than the
         number of nodes in the graph."""
    
    
    
    def get_unchecked_k_shortest_path_node_ids_from_node_ids(self, src_node_id: int, dst_node_id: int, k: int):
        """Return vector of the k minimum paths node IDs between given source node and destination node ID.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        k: int,
            Number of paths to find.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_maximum_node_degree(self):
        """Return the maximum node degree.
        
        Safety
        ------
        The method will return an undefined value (0) when the graph
        does not contain nodes. In those cases the value is not properly
        defined."""
    
    
    
    def get_unchecked_maximum_preferential_attachment(self):
        """Returns the maximum unweighted preferential attachment score.
        
        Safety
        ------
        If the graph does not contain nodes, the return value will be undefined."""
    
    
    
    def get_unchecked_minimum_node_degree(self):
        """Return the minimum node degree.
        
        Safety
        ------
        The method will return an undefined value (0) when the graph
        does not contain nodes. In those cases the value is not properly
        defined."""
    
    
    
    def get_unchecked_minimum_preferential_attachment(self):
        """Returns the minumum unweighted preferential attachment score.
        
        Safety
        ------
        If the graph does not contain nodes, the return value will be undefined."""
    
    
    
    def get_unchecked_minmax_edge_ids_from_node_ids(self, src: int, dst: int):
        """Return range of outbound edges IDs for all the edges bewteen the given
        source and destination nodes.
        This operation is meaningfull only in a multigraph.
        
        Parameters
        ----------
        src: int,
            Source node.
        dst: int,
            Destination node.
        
        
        Safety
        ------
        If the given node type IDs do not exist in the graph this method will panic."""
    
    
    
    def get_unchecked_minmax_edge_ids_from_source_node_id(self, src: int):
        """Return range of outbound edges IDs which have as source the given Node.
        
        The method will panic if the given source node ID is higher than
        the number of nodes in the graph.
        
        Parameters
        ----------
        src: int,
            Node for which we need to compute the cumulative_node_degrees range.
        
        
        Safety
        ------
        If the given node ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_most_central_node_id(self):
        """Returns maximum node degree of the graph.
        
        Safety
        ------
        This method fails with a panic if the graph does not have any node."""
    
    
    
    def get_unchecked_node_degree_from_node_id(self, node_id: int):
        """Returns the number of outbound neighbours of given node.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node.
        
        
        Safety
        ------
        If the given node ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_node_id_from_node_name(self, node_name: str):
        """Returns node id from given node name raising a panic if used unproperly.
        
        Parameters
        ----------
        node_name: str,
            The node name whose node ID is to be returned.
        
        
        Safety
        ------
        If the given node name does not exists in the considered graph the method will panic."""
    
    
    
    def get_unchecked_node_ids_and_edge_type_id_and_edge_weight_from_edge_id(self, edge_id: int):
        """Return the src, dst, edge type and weight of a given edge ID.
        
        This method will raise a panic when an improper configuration is used.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source, destination, edge type and weight are to be retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_node_ids_and_edge_type_id_from_edge_id(self, edge_id: int):
        """Return the src, dst, edge type of a given edge ID.
        
        This method will raise a panic when an improper configuration is used.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source, destination and edge type are to be retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_node_ids_from_edge_id(self, edge_id: int):
        """Returns node IDs corresponding to given edge ID.
        
        The method will panic if the given edge ID does not exists in the
        current graph instance.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source and destination node IDs are to e retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_node_name_from_node_id(self, node_id: int):
        """Returns result with the node name.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose name is to be returned.
        
        
        Safety
        ------
        If the given node ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_node_names_from_edge_id(self, edge_id: int):
        """Returns node names corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source and destination node IDs are to e retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_node_type_id_from_node_id(self, node_id: int):
        """Returns option with vector of node types of given node.
        
        This method will panic if the given node ID is greater than
        the number of nodes in the graph.
        Furthermore, if the graph does NOT have node types, it will NOT
        return neither an error or a panic.
        
        Parameters
        ----------
        node_id: int,
            node whose node type is to be returned.
        
        
        Safety
        ------
        Even though the method will return an option when the node types are
         not available for the current graph, the behaviour is undefined."""
    
    
    
    def get_unchecked_node_type_names_from_node_id(self, node_id: int):
        """Returns result of option with the node type of the given node id.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose node types are to be returned.
        
        
        Safety
        ------
        This method will return an iterator of None values when the graph
         does not contain node types."""
    
    
    
    def get_unchecked_node_type_names_from_node_type_ids(self, node_type_ids: List[int]):
        """Return node type name of given node type.
        
        Parameters
        ----------
        node_type_ids: List[int],
            Id of the node type.
        
        
        Safety
        ------
        The method will panic if the graph does not contain node types."""
    
    
    
    def get_unchecked_preferential_attachment_from_node_ids(self, source_node_id: int, destination_node_id: int, normalize: bool):
        """Returns the unweighted preferential attachment from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        normalize: bool,
            Whether to normalize within 0 to 1.
        
        
        Safety
        ------
        If either of the provided one and two node IDs are higher than the
         number of nodes in the graph."""
    
    
    
    def get_unchecked_resource_allocation_index_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the unweighted Resource Allocation Index for the given pair of nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Safety
        ------
        If either of the provided one and two node IDs are higher than the
         number of nodes in the graph."""
    
    
    
    def get_unchecked_shortest_path_node_ids_from_node_ids(self, src_node_id: int, dst_node_id: int, maximal_depth: Optional[int]):
        """Returns minimum path node IDs and distance from given node ids.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic.
        
        Raises
        -------
        ValueError
            If the given node is a selfloop.
        ValueError
            If there is no path between the two given nodes."""
    
    
    
    def get_unchecked_shortest_path_node_names_from_node_ids(self, src_node_id: int, dst_node_id: int, maximal_depth: Optional[int]):
        """Returns minimum path node names from given node ids.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_source_node_id_from_edge_id(self, edge_id: int):
        """Returns the source of given edge id without making any boundary check.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source is to be retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will cause an out of bounds."""
    
    
    
    def get_unchecked_source_node_name_from_edge_id(self, edge_id: int):
        """Returns source node name corresponding to given edge ID.
        
        Parameters
        ----------
        edge_id: int,
            The edge ID whose source node name is to be retrieved.
        
        
        Safety
        ------
        If the given edge ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_unique_source_node_id(self, source_id: int):
        """Returns edge ID corresponding to given source and destination node IDs.
        
        Parameters
        ----------
        source_id: int,
            The source node ID.
        
        
        Safety
        ------
        If the given source node ID does not exist in the current graph the method will panic."""
    
    
    
    def get_unchecked_weighted_closeness_centrality_from_node_id(self, node_id: int, use_edge_weights_as_probabilities: bool):
        """Return closeness centrality of the requested node.
        
        If the given node ID does not exist in the current graph the method
        will panic.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose closeness centrality is to be computed.
        use_edge_weights_as_probabilities: bool,
            Whether to treat the edge weights as probabilities.
        
        
        Safety
        ------
        If the given node ID does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_weighted_eccentricity_from_node_id(self, node_id: int, use_edge_weights_as_probabilities: Optional[bool]):
        """Returns weighted eccentricity of the given node.
        
        This method will panic if the given node ID does not exists in the graph.
        
        Parameters
        ----------
        node_id: int,
            Node for which to compute the eccentricity.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_weighted_harmonic_centrality_from_node_id(self, node_id: int, use_edge_weights_as_probabilities: bool):
        """Return harmonic centrality of the requested node.
        
        If the given node ID does not exist in the current graph the method
        will panic.
        
        Parameters
        ----------
        node_id: int,
            The node ID whose harmonic centrality is to be computed.
        use_edge_weights_as_probabilities: bool,
            Whether to treat the edge weights as probabilities.
        
        
        Safety
        ------
        If the given node ID does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_weighted_maximum_preferential_attachment(self):
        """Returns the maximum weighted preferential attachment score.
        
        Safety
        ------
        If the graph does not contain nodes, the return value will be undefined."""
    
    
    
    def get_unchecked_weighted_minimum_preferential_attachment(self):
        """Returns the minumum weighted preferential attachment score.
        
        Safety
        ------
        If the graph does not contain nodes, the return value will be undefined."""
    
    
    
    def get_unchecked_weighted_node_degree_from_node_id(self, node_id: int):
        """Returns the weighted sum of outbound neighbours of given node.
        
        The method will panic if the given node id is higher than the number of
        nodes in the graph.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node.
        
        
        Safety
        ------
        If the given node ID does not exist in the current graph the method will raise a panic."""
    
    
    
    def get_unchecked_weighted_preferential_attachment_from_node_ids(self, source_node_id: int, destination_node_id: int, normalize: bool):
        """Returns the weighted preferential attachment from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        normalize: bool,
            Whether to normalize within 0 to 1.
        
        
        Safety
        ------
        If either of the provided one and two node IDs are higher than the
         number of nodes in the graph."""
    
    
    
    def get_unchecked_weighted_resource_allocation_index_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the weighted Resource Allocation Index for the given pair of nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Safety
        ------
        If either of the provided one and two node IDs are higher than the
         number of nodes in the graph."""
    
    
    
    def get_unchecked_weighted_shortest_path_node_ids_from_node_ids(self, src_node_id: int, dst_node_id: int, maximal_depth: Optional[int], use_edge_weights_as_probabilities: Optional[bool], maximal_depth: Optional[int]):
        """Returns minimum path node IDs and distance from given node ids.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        maximal_depth: Optional[int],
            The maximal number of iterations to execute Dijkstra for.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic."""
    
    
    
    def get_unchecked_weighted_shortest_path_node_names_from_node_ids(self, src_node_id: int, dst_node_id: int, maximal_depth: Optional[int], use_edge_weights_as_probabilities: Optional[bool], maximal_depth: Optional[int]):
        """Returns minimum path node names from given node ids.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        maximal_depth: Optional[int],
            The maximal number of iterations to execute Dijkstra for.
        
        
        Safety
        ------
        If any of the given node IDs does not exist in the graph the method will panic."""
    
    
    
    def get_undirected_edges_number(self):
        """Returns number of undirected edges of the graph."""
    
    
    
    def get_undirected_louvain_community_detection(self, recursion_minimum_improvement: Optional[float], first_phase_minimum_improvement: Optional[float], patience: Optional[int], random_state: Optional[int]):
        """Returns vector of vectors of communities for each layer of hierarchy minimizing undirected modularity.
        
        Parameters
        ----------
        recursion_minimum_improvement: Optional[float],
            The minimum improvement to warrant another resursion round. By default, zero.
        first_phase_minimum_improvement: Optional[float],
            The minimum improvement to warrant another first phase iteration. By default, `0.00001` (not zero because of numerical instability).
        patience: Optional[int],
            How many iterations of the first phase to wait for before stopping. By default, `5`.
        random_state: Optional[int],
            The random state to use to reproduce this modularity computation. By default, 42.
        
        
        Raises
        -------
        ValueError
            If the graph is not directed.
        ValueError
            If the `recursion_minimum_improvement` has an invalid value, i.e. NaN or infinity.
        ValueError
            If the `first_phase_minimum_improvement` has an invalid value, i.e. NaN or infinity."""
    
    
    
    def get_undirected_modularity_from_node_community_memberships(self):
        """Returns the undirected modularity of the graph from the given memberships.
        
        Parameters
        ----------
        
        
        Raises
        -------
        ValueError
            If the number of provided memberships does not match the number of nodes of the graph."""
    
    
    
    def get_uniform_random_walk_random_nodes(self, node: int, random_state: int, walk_length: int, unique: Optional[bool]):
        """Returns unique nodes sampled from uniform random walk.
        
        Parameters
        ----------
        node: int,
            Node from where to start the random walks.
        random_state: int,
            the random_state to use for extracting the nodes and edges.
        walk_length: int,
            Length of the random walk.
        unique: Optional[bool],
            Whether to make the sampled nodes unique.
        
        
        Raises
        -------
        ValueError
            If the given node does not exist in the current slack."""
    
    
    
    def get_unique_directed_edges_number(self):
        """Return number of the unique edges in the graph"""
    
    
    
    def get_unique_edge_type_ids(self):
        """Return the unique edge type IDs of the graph edges."""
    
    
    
    def get_unique_edge_type_names(self):
        """Return the edge types names"""
    
    
    
    def get_unique_edges_number(self):
        """Returns number of unique edges of the graph."""
    
    
    
    def get_unique_node_type_ids(self):
        """Return the unique node type IDs of the graph nodes."""
    
    
    
    def get_unique_node_type_names(self):
        """Return the unique node types names."""
    
    
    
    def get_unique_selfloops_number(self):
        """Returns number of unique self-loops, excluding those in eventual multi-edges."""
    
    
    
    def get_unique_source_nodes_number(self):
        """Returns number of the source nodes."""
    
    
    
    def get_unique_undirected_edges_number(self):
        """Returns number of undirected edges of the graph."""
    
    
    
    def get_unknown_edge_types_number(self):
        """Returns number of unknown edge types.
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_unknown_edge_types_rate(self):
        """Returns rate of unknown edge types over total edges number.
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def get_unknown_node_types_mask(self):
        """Returns boolean mask of unknown node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def get_unknown_node_types_number(self):
        """Returns number of nodes with unknown node type.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_unknown_node_types_rate(self):
        """Returns rate of unknown node types over total nodes number.
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    
    
    def get_weighted_all_shortest_paths(self, iterations: Optional[int], use_edge_weights_as_probabilities: Optional[bool], verbose: Optional[bool]):
        """Returns graph with weighted shortest paths computed up to the given depth.
        
        The returned graph will have no selfloops.
        
        Parameters
        ----------
        iterations: Optional[int],
            The number of iterations of the transitive closure to execute. If None, the complete transitive closure is computed.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        verbose: Optional[bool],
            Whether to show a loading bar while building the graph.
        
        
        Raises
        -------
        ValueError
            If the graph does not have weights.
        ValueError
            If the graph contains negative weights.
        ValueError
            If the user has asked for the weights to be treated as probabilities but the weights are not between 0 and 1."""
    
    
    
    def get_weighted_closeness_centrality(self, use_edge_weights_as_probabilities: bool, verbose: Optional[bool]):
        """Return closeness centrality for all nodes.
        
        Parameters
        ----------
        use_edge_weights_as_probabilities: bool,
            Whether to treat the edge weights as probabilities.
        verbose: Optional[bool],
            Whether to show an indicative progress bar.
        
        
        Raises
        -------
        ValueError
            If the graph does not have weights.
        ValueError
            If the graph contains negative weights.
        ValueError
            If the user has asked for the weights to be treated as probabilities but the weights are not between 0 and 1."""
    
    
    
    def get_weighted_degree_centrality(self):
        """Returns vector of weighted degree centrality for all nodes"""
    
    
    
    def get_weighted_diameter_naive(self, ignore_infinity: Optional[bool], use_edge_weights_as_probabilities: Optional[bool], verbose: Optional[bool]):
        """Returns diameter of the graph using naive method.
        
        Note that there exists the non-naive method for undirected graphs
        and it is possible to implement a faster method for directed graphs
        but we still need to get to it, as it will require an updated
        succinct data structure.
        
        Parameters
        ----------
        ignore_infinity: Optional[bool],
            Whether to ignore infinite distances, which are present when in the graph exist multiple components.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        verbose: Optional[bool],
            Whether to show a loading bar.
        
        
        Raises
        -------
        ValueError
            If the graph does not contain nodes.
        ValueError
            If the graph does not have weights.
        ValueError
            If the graph contains negative weights.
        ValueError
            If the user has asked for the weights to be treated as probabilities but the weights are not between 0 and 1."""
    
    
    
    def get_weighted_eccentricity_from_node_id(self, node_id: int, use_edge_weights_as_probabilities: Optional[bool]):
        """Returns weighted eccentricity of the given node ID.
        
        Parameters
        ----------
        node_id: int,
            Node for which to compute the eccentricity.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        
        
        Raises
        -------
        ValueError
            If the given node ID does not exist in the graph.
        ValueError
            If weights are requested to be treated as probabilities but are not between 0 and 1.
        ValueError
            If the graph contains negative weights."""
    
    
    
    def get_weighted_eccentricity_from_node_name(self, node_name: str, use_edge_weights_as_probabilities: Optional[bool]):
        """Returns weighted eccentricity of the given node name.
        
        Parameters
        ----------
        node_name: str,
            Node for which to compute the eccentricity.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        
        
        Raises
        -------
        ValueError
            If the given node name does not exist in the graph.
        ValueError
            If weights are requested to be treated as probabilities but are not between 0 and 1.
        ValueError
            If the graph contains negative weights."""
    
    
    
    def get_weighted_eigenvector_centrality(self, maximum_iterations_number: Optional[int], tollerance: Optional[float]):
        """Returns vector with unweighted eigenvector centrality.
        
        Parameters
        ----------
        maximum_iterations_number: Optional[int],
            The maximum number of iterations to consider.
        tollerance: Optional[float],
            The maximum error tollerance for convergence."""
    
    
    
    def get_weighted_harmonic_centrality(self, use_edge_weights_as_probabilities: Optional[bool], verbose: Optional[bool]):
        """Return harmonic centrality for all nodes.
        
        Parameters
        ----------
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        verbose: Optional[bool],
            Whether to show an indicative progress bar."""
    
    
    
    def get_weighted_maximum_node_degree(self):
        """Return the maximum weighted node degree"""
    
    
    
    def get_weighted_minimum_node_degree(self):
        """Return the minimum weighted node degree"""
    
    
    
    def get_weighted_node_degree_from_node_id(self, node_id: int):
        """Returns the weighted sum of outbound neighbours of given node ID.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node."""
    
    
    
    def get_weighted_node_degrees(self):
        """Returns the weighted degree of every node in the graph"""
    
    
    
    def get_weighted_node_degrees_mean(self):
        """Returns weighted mean node degree of the graph."""
    
    
    
    def get_weighted_node_degrees_median(self):
        """Returns weighted median node degree of the graph"""
    
    
    
    def get_weighted_node_indegrees(self):
        """Return the weighted indegree (total weighted inbound edge weights) for each node."""
    
    
    
    def get_weighted_preferential_attachment_from_node_ids(self, source_node_id: int, destination_node_id: int, normalize: bool):
        """Returns the weighted preferential attachment from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        normalize: bool,
            Whether to normalize by the square of maximum degree.
        
        
        Raises
        -------
        ValueError
            If either of the node IDs are higher than the number of nodes in the graph."""
    
    
    
    def get_weighted_preferential_attachment_from_node_names(self, first_node_name: str, second_node_name: str, normalize: bool):
        """Returns the weighted preferential attachment from the given node names.
        
        Parameters
        ----------
        first_node_name: str,
            Node name of the first node.
        second_node_name: str,
            Node name of the second node.
        normalize: bool,
            Whether to normalize by the square of maximum degree.
        
        
        Raises
        -------
        ValueError
            If either of the given node names do not exist in the current graph."""
    
    
    
    def get_weighted_resource_allocation_index_from_node_ids(self, source_node_id: int, destination_node_id: int):
        """Returns the weighted Resource Allocation Index for the given pair of nodes from the given node IDs.
        
        Parameters
        ----------
        source_node_id: int,
            Node ID of the first node.
        destination_node_id: int,
            Node ID of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the node IDs are higher than the number of nodes in the graph."""
    
    
    
    def get_weighted_resource_allocation_index_from_node_names(self, first_node_name: str, second_node_name: str):
        """Returns the weighted Resource Allocation Index for the given pair of nodes from the given node names.
        
        Parameters
        ----------
        first_node_name: str,
            Node name of the first node.
        second_node_name: str,
            Node name of the second node.
        
        
        Raises
        -------
        ValueError
            If either of the given node names do not exist in the current graph."""
    
    
    
    def get_weighted_shortest_path_node_ids_from_node_ids(self, src_node_id: int, dst_node_id: int, maximal_depth: Optional[int], use_edge_weights_as_probabilities: Optional[bool], maximal_depth: Optional[int]):
        """Returns minimum path node names from given node ids.
        
        Parameters
        ----------
        src_node_id: int,
            Source node ID.
        dst_node_id: int,
            Destination node ID.
        maximal_depth: Optional[int],
            The maximal depth to execute the BFS for.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        maximal_depth: Optional[int],
            The maximal number of iterations to execute Dijkstra for.
        
        
        Raises
        -------
        ValueError
            If any of the given node IDs do not exist in the current graph."""
    
    
    
    def get_weighted_shortest_path_node_ids_from_node_names(self, src_node_name: str, dst_node_name: str, use_edge_weights_as_probabilities: Optional[bool], maximal_depth: Optional[int]):
        """Returns minimum path node names from given node names.
        
        Parameters
        ----------
        src_node_name: str,
            Source node name.
        dst_node_name: str,
            Destination node name.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        maximal_depth: Optional[int],
            The maximal number of iterations to execute Dijkstra for.
        
        
        Raises
        -------
        ValueError
            If any of the given node names do not exist in the current graph."""
    
    
    
    def get_weighted_shortest_path_node_names_from_node_names(self, src_node_name: str, dst_node_name: str, use_edge_weights_as_probabilities: Optional[bool], maximal_depth: Optional[int]):
        """Returns minimum path node names from given node names.
        
        Parameters
        ----------
        src_node_name: str,
            Source node name.
        dst_node_name: str,
            Destination node name.
        use_edge_weights_as_probabilities: Optional[bool],
            Whether to treat the edge weights as probabilities.
        maximal_depth: Optional[int],
            The maximal number of iterations to execute Dijkstra for.
        
        
        Raises
        -------
        ValueError
            If any of the given node names do not exist in the current graph."""
    
    
    
    def get_weighted_singleton_nodes_number(self):
        """Return the number of weighted singleton nodes, i.e. nodes with weighted node degree equal to zero"""
    
    
    
    def get_weighted_top_k_central_node_ids(self, k: int):
        """Return vector with weighted top k central node Ids.
        
        If the k passed is bigger than the number of nodes this method will return
        all the nodes in the graph.
        
        Parameters
        ----------
        k: int,
            Number of central nodes to extract.
        
        
        Raises
        -------
        ValueError
            If the current graph instance does not contain edge weights.
        ValueError
            If the given value k is zero."""
    
    
    
    def get_weighted_triads_number(self):
        """Returns total number of triads in the weighted graph"""
    
    
    
    def has_constant_edge_weights(self):
        """Returns whether the graph has constant weights.
        
        Raises
        -------
        ValueError
            If the graph does not contain edge weights."""
    
    
    
    def has_default_graph_name(self):
        """Return if graph has name that is not the default one.
        
        TODO: use a default for the default graph name"""
    
    
    
    def has_disconnected_nodes(self):
        """Returns boolean representing if nodes which are nor singletons nor
        singletons with selfloops."""
    
    
    
    def has_edge_from_node_ids(self, src: int, dst: int):
        """Returns whether edge passing between given node ids exists.
        
        Parameters
        ----------
        src: int,
            Source node id.
        dst: int,
            Destination node id."""
    
    
    
    def has_edge_from_node_ids_and_edge_type_id(self, src: int, dst: int, edge_type: Optional[int]):
        """Returns whether edge with the given type passing between given nodes exists.
        
        Parameters
        ----------
        src: int,
            The source node of the edge.
        dst: int,
            The destination node of the edge.
        edge_type: Optional[int],
            The (optional) edge type."""
    
    
    
    def has_edge_from_node_names(self, src_name: str, dst_name: str):
        """Returns whether if edge passing between given nodes exists.
        
        Parameters
        ----------
        src_name: str,
            The source node name of the edge.
        dst_name: str,
            The destination node name of the edge."""
    
    
    
    def has_edge_from_node_names_and_edge_type_name(self, src_name: str, dst_name: str, edge_type_name: Optional[str]):
        """Returns whether if edge with type passing between given nodes exists.
        
        Parameters
        ----------
        src_name: str,
            The source node name of the edge.
        dst_name: str,
            The destination node name of the edge.
        edge_type_name: Optional[str],
            The (optional) edge type name."""
    
    
    
    def has_edge_type_id(self, edge_type_id: int):
        """Returns whether the graph has the given edge type id.
        
        Parameters
        ----------
        edge_type_id: int,
            id of the edge."""
    
    
    
    def has_edge_type_name(self, edge_type_name: str):
        """Returns whether the graph has the given edge type name.
        
        Parameters
        ----------
        edge_type_name: str,
            Name of the edge."""
    
    
    
    def has_edge_types(self):
        """Returns boolean representing whether graph has edge types."""
    
    
    
    def has_edge_types_oddities(self):
        """Return whether the graph has any known edge type-related graph oddities.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def has_edge_weights(self):
        """Returns boolean representing whether graph has weights."""
    
    
    
    def has_edge_weights_representing_probabilities(self):
        """Returns whether graph has weights that can represent probabilities"""
    
    
    
    def has_edges(self):
        """Return if the graph has any edges."""
    
    
    
    def has_homogeneous_edge_types(self):
        """Returns whether the edges have an homogenous edge type.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def has_homogeneous_node_types(self):
        """Returns whether the nodes have an homogenous node type.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def has_known_edge_types(self):
        """Returns whether there are known edge types.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def has_known_node_types(self):
        """Returns whether there are known node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def has_multilabel_node_types(self):
        """Returns boolean representing if graph has multilabel node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def has_negative_edge_weights(self):
        """Returns boolean representing whether graph has negative weights.
        
        Raises
        -------
        ValueError
            If the graph does not contain weights."""
    
    
    
    def has_node_name(self, node_name: str):
        """Returns whether the graph has the given node name.
        
        Parameters
        ----------
        node_name: str,
            Name of the node."""
    
    
    
    def has_node_name_and_node_type_name(self, node_name: str, node_type_name: Optional[List[str]]):
        """Returns whether the given node name and node type name exist in current graph.
        
        Parameters
        ----------
        node_name: str,
            The node name.
        node_type_name: Optional[List[str]],
            The node types name."""
    
    
    
    def has_node_oddities(self):
        """Return whether the graph has any known node-related graph oddities"""
    
    
    
    def has_node_type_id(self, node_type_id: int):
        """Returns whether the graph has the given node type id.
        
        Parameters
        ----------
        node_type_id: int,
            id of the node."""
    
    
    
    def has_node_type_name(self, node_type_name: str):
        """Returns whether the graph has the given node type name.
        
        Parameters
        ----------
        node_type_name: str,
            Name of the node."""
    
    
    
    def has_node_types(self):
        """Returns boolean representing if graph has node types"""
    
    
    
    def has_node_types_oddities(self):
        """Return whether the graph has any known node type-related graph oddities.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def has_nodes(self):
        """Return if the graph has any nodes."""
    
    
    
    def has_nodes_sorted_by_decreasing_outbound_node_degree(self):
        """Returns whether the node IDs are sorted by decreasing outbound node degree."""
    
    
    
    def has_nodes_sorted_by_increasing_outbound_node_degree(self):
        """Returns whether the node IDs are sorted by increasing outbound node degree."""
    
    
    
    def has_nodes_sorted_by_lexicographic_order(self):
        """Returns whether the node IDs are sorted by decreasing outbound node degree."""
    
    
    
    def has_same_adjacency_matrix(self, other: Graph):
        """Return true if the graphs share the same adjacency matrix.
        
        Parameters
        ----------
        other: Graph,
            The other graph."""
    
    
    
    def has_selfloop_from_node_id(self, node_id: int):
        """Returns whether the given node ID has a selfloop.
        
        Parameters
        ----------
        node_id: int,
            Source node id."""
    
    
    
    def has_selfloops(self):
        """Returns boolean representing if graph has self-loops."""
    
    
    
    def has_singleton_edge_types(self):
        """Returns whether there is at least singleton edge type, that is a edge type that only appears once.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def has_singleton_node_types(self):
        """Returns whether there is at least singleton node type, that is a node type that only appears once.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def has_singleton_nodes(self):
        """Returns boolean representing if graph has singletons."""
    
    
    
    def has_singleton_nodes_with_selfloops(self):
        """Returns boolean representing if graph has singletons"""
    
    
    
    def has_trap_nodes(self):
        """Return whether the graph has trap nodes."""
    
    
    
    def has_unknown_edge_types(self):
        """Returns whether there are unknown edge types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def has_unknown_node_types(self):
        """Returns whether there are unknown node types.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def has_weighted_singleton_nodes(self):
        """Returns whether a graph has one or more weighted singleton nodes.
        
        A weighted singleton node is a node whose weighted node degree is 0.
        
        Raises
        -------
        ValueError
            If the graph does not contain edge weights."""
    
    
    
    def is_compatible(self, other: Graph):
        """Return true if the graphs are compatible.
        
        Parameters
        ----------
        other: Graph,
            The other graph.
        
        
        Raises
        -------
        ValueError
            If a graph is directed and the other is undirected.
        ValueError
            If one of the two graphs has edge weights and the other does not.
        ValueError
            If one of the two graphs has node types and the other does not.
        ValueError
            If one of the two graphs has edge types and the other does not."""
    
    
    
    def is_connected(self, verbose: Optional[bool]):
        """Returns whether the graph is connected.
        
        Parameters
        ----------
        verbose: Optional[bool],
            Whether to show the loading bar while computing the connected components, if necessary."""
    
    
    
    def is_directed(self):
        """Returns boolean representing if graph is directed."""
    
    
    
    def is_multigraph(self):
        """Return if there are multiple edges between two node"""
    
    
    
    def is_singleton_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is a singleton.
        
        Parameters
        ----------
        node_id: int,
            The node to be checked for."""
    
    
    
    def is_singleton_from_node_name(self, node_name: str):
        """Returns boolean representing if given node is a singleton.
        
        Parameters
        ----------
        node_name: str,
            The node name to be checked for."""
    
    
    
    def is_singleton_with_selfloops_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is a singleton with self-loops.
        
        Parameters
        ----------
        node_id: int,
            The node to be checked for."""
    
    
    
    def is_trap_node_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is a trap.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node, if this is bigger that the number of nodes it will panic."""
    
    
    
    def is_unchecked_connected_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is not a singleton nor a singleton with selfloop.
        
        Parameters
        ----------
        node_id: int,
            The node to be checked for.
        
        
        Safety
        ------
        If the given node ID does not exists in the graph this method will panic."""
    
    
    
    def is_unchecked_disconnected_node_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is a singleton or a singleton with selfloop.
        
        Parameters
        ----------
        node_id: int,
            The node to be checked for.
        
        
        Safety
        ------
        If the given node ID does not exists in the graph this method will panic."""
    
    
    
    def is_unchecked_singleton_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is a singleton.
        
        Parameters
        ----------
        node_id: int,
            The node to be checked for.
        
        
        Safety
        ------
        If the given node ID does not exists in the graph this method will panic."""
    
    
    
    def is_unchecked_singleton_from_node_name(self, node_name: str):
        """Returns boolean representing if given node is a singleton.
        
        Nota that this method will raise a panic if caled with unproper
        parametrization.
        
        Parameters
        ----------
        node_name: str,
            The node name to be checked for.
        
        
        Safety
        ------
        If the given node name does not exist in the graph this method will panic."""
    
    
    
    def is_unchecked_singleton_with_selfloops_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is a singleton with self-loops.
        
        Parameters
        ----------
        node_id: int,
            The node to be checked for."""
    
    
    
    def is_unchecked_trap_node_from_node_id(self, node_id: int):
        """Returns boolean representing if given node is a trap.
        
        If the provided node_id is higher than the number of nodes in the graph,
        the method will panic.
        
        Parameters
        ----------
        node_id: int,
            Integer ID of the node, if this is bigger that the number of nodes it will panic.
        
        
        Safety
        ------
        If the given node ID does not exists in the graph this method will panic."""
    
    
    
    def must_be_connected(self):
        """Raises an error if the graph is not connected.
        
        Raises
        -------
        ValueError
            If the graph is not connected."""
    
    
    
    def must_be_multigraph(self):
        """Raises an error if the graph does not have edge types.
        
        Raises
        -------
        ValueError
            If the graph is not a multigraph."""
    
    
    
    def must_be_undirected(self):
        """Raises an error if the graph does not have edge types.
        
        Raises
        -------
        ValueError
            If the graph is directed."""
    
    
    
    def must_have_edges(self):
        """Raises an error if the graph has a maximal weighted
        
        Raises
        -------
        ValueError
            If the graph does not have edges."""
    
    
    
    def must_have_nodes(self):
        """Raises an error if the graph does not have any node.
        
        Raises
        -------
        ValueError
            If the graph does not have nodes."""
    
    
    
    def must_not_be_multigraph(self):
        """Raises an error if the graph does not have edge types.
        
        Raises
        -------
        ValueError
            If the graph is a multigraph."""
    
    
    
    def must_not_contain_unknown_edge_types(self):
        """Raises an error if the graph contains unknown edge types.
        
        Raises
        -------
        ValueError
            If the graph does not contain edge types.
        ValueError
            If the graph contains unknown edge types."""
    
    
    
    def must_not_contain_unknown_node_types(self):
        """Raises an error if the graph contains unknown node types.
        
        Raises
        -------
        ValueError
            If the graph does not contain node types.
        ValueError
            If the graph contains unknown node types."""
    
    
    
    def must_not_contain_weighted_singleton_nodes(self):
        """Raises an error if the graph contains zero weighted degree.
        
        Raises
        -------
        ValueError
            If the graph does not have edges."""
    
    
    
    def overlap_textual_report(self, other: Graph, verbose: Optional[bool]):
        """Return rendered textual report about the graph overlaps.
        
        Parameters
        ----------
        other: Graph,
            graph to create overlap report with.
        verbose: Optional[bool],
            Whether to shor the loading bars."""
    
    
    
    def overlaps(self, other: Graph):
        """Return whether given graph has any edge overlapping with current graph.
        
        Parameters
        ----------
        other: Graph,
            The graph to check against.
        
        
        Raises
        -------
        ValueError
            If a graph is directed and the other is undirected.
        ValueError
            If one of the two graphs has edge weights and the other does not.
        ValueError
            If one of the two graphs has node types and the other does not.
        ValueError
            If one of the two graphs has edge types and the other does not."""
    
    
    
    def random_holdout(self, train_size: float, random_state: Optional[int], include_all_edge_types: Optional[bool], edge_types: Optional[List[Optional[str]]], min_number_overlaps: Optional[int], verbose: Optional[bool]):
        """Returns random holdout for training ML algorithms on the graph edges.
        
        The holdouts returned are a tuple of graphs. In neither holdouts the
        graph connectivity is necessarily preserved. To maintain that, use
        the method `connected_holdout`.
        
        Parameters
        ----------
        train_size: float,
            rate target to reserve for training
        random_state: Optional[int],
            The random_state to use for the holdout,
        include_all_edge_types: Optional[bool],
            Whether to include all the edges between two nodes.
        edge_types: Optional[List[Optional[str]]],
            The edges to include in validation set.
        min_number_overlaps: Optional[int],
            The minimum number of overlaps to include the edge into the validation set.
        verbose: Optional[bool],
            Whether to show the loading bar.
        
        
        Raises
        -------
        ValueError
            If the edge types have been specified but the graph does not have edge types.
        ValueError
            If the minimum number of overlaps have been specified but the graph is not a multigraph.
        ValueError
            If one or more of the given edge type names is not present in the graph."""
    
    
    
    def random_spanning_arborescence_kruskal(self, random_state: Optional[int], undesired_edge_types: Optional[Set[Optional[int]]], verbose: Optional[bool]):
        """Returns set of edges composing a spanning tree and connected components.
        
        The spanning tree is NOT minimal.
        The given random_state is NOT the root of the tree.
        
        This method, additionally, allows for undesired edge types to be
        used to build the spanning tree only in extremis when it is utterly
        necessary in order to complete the spanning arborescence.
        
        The quintuple returned contains:
        - Set of the edges used in order to build the spanning arborescence.
        - Vector of the connected component of each node.
        - Number of connected components.
        - Minimum component size.
        - Maximum component size.
        
        Parameters
        ----------
        random_state: Optional[int],
            The random_state to use for the holdout,
        undesired_edge_types: Optional[Set[Optional[int]]],
            Which edge types id to try to avoid.
        verbose: Optional[bool],
            Whether to show a loading bar or not."""
    
    
    
    def remap_from_graph(self, other: Graph):
        """Return graph remapped towards nodes of the given graph.
        
        Parameters
        ----------
        other: Graph,
            The graph to remap towards."""
    
    
    
    def remap_from_node_ids(self, node_ids: List[int]):
        """Returns graph remapped using given node IDs ordering.
        
        Parameters
        ----------
        node_ids: List[int],
            The node Ids to remap the graph to.
        
        
        Raises
        -------
        ValueError
            If the given node IDs are not unique.
        ValueError
            If the given node IDs are not available for all the values in the graph."""
    
    
    
    def remap_from_node_names(self, node_names: List[str]):
        """Returns graph remapped using given node names ordering.
        
        Parameters
        ----------
        node_names: List[str],
            The node names to remap the graph to.
        
        
        Raises
        -------
        ValueError
            If the given node names are not unique.
        ValueError
            If the given node names are not available for all the values in the graph."""
    
    
    
    def remap_unchecked_from_node_ids(self, node_ids: List[int]):
        """Returns graph remapped using given node IDs ordering.
        
        Parameters
        ----------
        node_ids: List[int],
            The node Ids to remap the graph to.
        
        
        Safety
        ------
        This method will cause a panic if the node IDs are either:
         * Not unique
         * Not available for each of the node IDs of the graph."""
    
    
    
    def remove_components(self, node_names: Optional[List[str]], node_types: Optional[List[Optional[str]]], edge_types: Optional[List[Optional[str]]], minimum_component_size: Optional[int], top_k_components: Optional[int], verbose: Optional[bool]):
        """remove all the components that are not connected to interesting
        nodes and edges.
        
        Parameters
        ----------
        node_names: Optional[List[str]],
            The name of the nodes of which components to keep.
        node_types: Optional[List[Optional[str]]],
            The types of the nodes of which components to keep.
        edge_types: Optional[List[Optional[str]]],
            The types of the edges of which components to keep.
        minimum_component_size: Optional[int],
            Optional, Minimum size of the components to keep.
        top_k_components: Optional[int],
            Optional, number of components to keep sorted by number of nodes.
        verbose: Optional[bool],
            Whether to show the loading bar."""
    
    
    
    def remove_edge_type_id(self, edge_type_id: int):
        """Remove given edge type ID from all edges.
        
        If any given edge remains with no edge type, that edge is labeled
        with edge type None. Note that the modification DOES NOT happen inplace.
        
        Parameters
        ----------
        edge_type_id: int,
            The edge type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph does not have edge types.
        ValueError
            If the given edge type ID does not exists in the graph."""
    
    
    
    def remove_edge_type_name(self, edge_type_name: str):
        """Remove given edge type name from all edges.
        
        If any given edge remains with no edge type, that edge is labeled
        with edge type None. Note that the modification DOES NOT happen inplace.
        
        Parameters
        ----------
        edge_type_name: str,
            The edge type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph does not have edge types.
        ValueError
            If the given edge type name does not exists in the graph."""
    
    
    
    def remove_edge_types(self):
        """Remove edge types from the graph.
        
        Note that the modification does not happen inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def remove_edge_weights(self):
        """Remove edge weights from the graph.
        
        Note that the modification does not happen inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have edge weights."""
    
    
    
    def remove_inplace_edge_type_ids(self):
        """Remove given edge type ID from all edges.
        
        Parameters
        ----------
        edge_type_id: int,
            The edge type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph is a multigraph.
        ValueError
            If the graph does not have edge types.
        ValueError
            If the given edge type ID does not exists in the graph."""
    
    
    
    def remove_inplace_edge_type_name(self, edge_type_name: str):
        """Remove given edge type name from all edges.
        
        If any given edge remains with no edge type, that edge is labeled
        with edge type None. Note that the modification happens inplace.
        
        Parameters
        ----------
        edge_type_name: str,
            The edge type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph does not have edge types.
        ValueError
            If the given edge type name does not exists in the graph."""
    
    
    
    def remove_inplace_edge_types(self):
        """Remove edge types from the graph.
        
        Note that the modification happens inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types.
        ValueError
            If the graph is a multigraph."""
    
    
    
    def remove_inplace_edge_weights(self):
        """Remove edge weights from the graph.
        
        Note that the modification happens inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have edge weights."""
    
    
    
    def remove_inplace_node_type_ids(self):
        """Remove given node type ID from all nodes.
        
        If any given node remains with no node type, that node is labeled
        with node type None. Note that the modification happens inplace.
        
        Parameters
        ----------
        node_type_id_to_remove: int,
            The node type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If the given node type ID does not exists in the graph."""
    
    
    
    def remove_inplace_node_type_name(self, node_type_name: str):
        """Remove given node type name from all nodes.
        
        If any given node remains with no node type, that node is labeled
        with node type None. Note that the modification happens inplace.
        
        Parameters
        ----------
        node_type_name: str,
            The node type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If the given node type name does not exists in the graph."""
    
    
    
    def remove_inplace_node_types(self):
        """Remove node types from the graph.
        
        Note that the modification happens inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def remove_inplace_singleton_edge_types(self):
        """Remove singleton edge types from all edges.
        
        If any given edge remains with no edge type, that edge is labeled
        with edge type None. Note that the modification happens inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def remove_inplace_singleton_node_types(self):
        """Remove singleton node types from all nodes.
        
        If any given node remains with no node type, that node is labeled
        with node type None. Note that the modification happens inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def remove_node_type_id(self, node_type_id: int):
        """Remove given node type ID from all nodes.
        
        If any given node remains with no node type, that node is labeled
        with node type None. Note that the modification DOES NOT happen inplace.
        
        Parameters
        ----------
        node_type_id: int,
            The node type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If the given node type ID does not exists in the graph."""
    
    
    
    def remove_node_type_name(self, node_type_name: str):
        """Remove given node type name from all nodes.
        
        If any given node remains with no node type, that node is labeled
        with node type None. Note that the modification DOES NOT happen inplace.
        
        Parameters
        ----------
        node_type_name: str,
            The node type ID to remove.
        
        
        Raises
        -------
        ValueError
            If the graph does not have node types.
        ValueError
            If the given node type name does not exists in the graph."""
    
    
    
    def remove_node_types(self):
        """Remove node types from the graph.
        
        Note that the modification does not happen inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def remove_singleton_edge_types(self):
        """Remove singleton edge types from all edges.
        
        If any given edge remains with no edge type, that edge is labeled
        with edge type None. Note that the modification DOES NOT happen inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have edge types."""
    
    
    
    def remove_singleton_node_types(self):
        """Remove singleton node types from all nodes.
        
        If any given node remains with no node type, that node is labeled
        with node type None. Note that the modification DOES NOT happen inplace.
        
        Raises
        -------
        ValueError
            If the graph does not have node types."""
    
    
    
    def replace(self, node_name_mapping: Optional[Dict[str, str]], node_type_name_mapping: Optional[Dict[str, str]], edge_type_name_mapping: Optional[Dict[str, str]]):
        """Replace given node, node type and edge type names.
        
        Parameters
        ----------
        node_name_mapping: Optional[Dict[str, str]],
            The node names to replace.
        node_type_name_mapping: Optional[Dict[str, str]],
            The node type names to replace.
        edge_type_name_mapping: Optional[Dict[str, str]],
            The edge type names to replace.
        
        
        Raises
        -------
        ValueError
            If the given node names mapping would lead to nodes duplication."""
    
    
    
    def report(self):
        """Returns report relative to the graph metrics
        
        The report includes the following metrics by default:
        * Name of the graph
        * Whether the graph is directed or undirected
        * Number of singleton nodes
        * Number of nodes
        - If the graph has nodes, we also compute:
        * Minimum unweighted node degree
        * Maximum unweighted node degree
        * Unweighted node degree mean
        * Number of edges
        * Number of self-loops
        * Number of singleton with self-loops
        * Whether the graph is a multigraph
        * Number of parallel edges
        * Number of directed edges
        - If the graph has edges, we also compute:
        * Rate of self-loops
        * Whether the graph has weighted edges
        - If the graph has weights, we also compute:
        * Minimum weighted node degree
        * Maximum weighted node degree
        * Weighted node degree mean
        * The total edge weights
        * Whether the graph has node types
        - If the graph has node types, we also compute:
        * Whether the graph has singleton node types
        * The number of node types
        * The number of nodes with unknown node types
        * The number of nodes with known node types
        * Whether the graph has edge types
        - If the graph has edge types, we also compute:
        * Whether the graph has singleton edge types
        * The number of edge types
        * The number of edges with unknown edge types
        * The number of edges with known edge types
        
        On request, since it takes more time to compute it, the method also provides:"""
    
    
    
    def sample_negatives(self, negatives_number: int, random_state: Optional[int], seed_graph: Optional[Graph], only_from_same_component: Optional[bool], verbose: Optional[bool]):
        """Returns Graph with given amount of negative edges as positive edges.
        
        The graph generated may be used as a testing negatives partition to be
        fed into the argument "graph_to_avoid" of the link_prediction or the
        skipgrams algorithm
        
        Parameters
        ----------
        negatives_number: int,
            Number of negatives edges to include.
        random_state: Optional[int],
            random_state to use to reproduce negative edge set.
        seed_graph: Optional[Graph],
            Optional graph to use to filter the negative edges. The negative edges generated when this variable is provided will always have a node within this graph.
        only_from_same_component: Optional[bool],
            Whether to sample negative edges only from nodes that are from the same component.
        verbose: Optional[bool],
            Whether to show the loading bar."""
    
    
    
    def set_all_edge_types(self, edge_type: str):
        """Replace all edge types (if present) and set all the edge to edge_type.
        
        This DOES NOT happen inplace, but created a new instance of the graph.
        
        Parameters
        ----------
        edge_type: str,
            The edge type to assing to all the edges."""
    
    
    
    def set_all_node_types(self, node_type: str):
        """Replace all node types (if present) and set all the node to node_type.
        
        This DOES NOT happen inplace, but created a new instance of the graph.
        
        Parameters
        ----------
        node_type: str,
            The node type to assing to all the nodes."""
    
    
    
    def set_inplace_all_edge_types(self, edge_type: str):
        """Replace all edge types (if present) and set all the edge to edge_type.
        
        This happens INPLACE, that is edits the current graph instance.
        
        Parameters
        ----------
        edge_type: str,
            The edge type to assing to all the edges.
        
        
        Raises
        -------
        ValueError
            If the graph does not have edges.
        ValueError
            If the graph is a multigraph."""
    
    
    
    def set_inplace_all_node_types(self, node_type: str):
        """Replace all node types (if present) and set all the node to node_type.
        
        Parameters
        ----------
        node_type: str,
            The node type to assing to all the nodes."""
    
    
    
    def set_name(self, name: str):
        """Set the name of the graph.
        
        Parameters
        ----------
        name: str,
            Name of the graph."""
    
    
    
    def sort_by_bfs_topological_sorting_from_node_id(self, root_node_id: int):
        """Returns graph with node IDs sorted using a BFS
        
        Parameters
        ----------
        root_node_id: int,
            Node ID of node to be used as root of BFS
        
        
        Raises
        -------
        ValueError
            If the given root node ID does not exist in the graph"""
    
    
    
    def sort_by_decreasing_outbound_node_degree(self):
        """Returns graph with node IDs sorted by decreasing outbound node degree"""
    
    
    
    def sort_by_increasing_outbound_node_degree(self):
        """Returns graph with node IDs sorted by increasing outbound node degree"""
    
    
    
    def sort_by_node_lexicographic_order(self):
        """Returns graph with node IDs sorted by lexicographic order"""
    
    
    
    def spanning_arborescence_kruskal(self, verbose: Optional[bool]):
        """Returns consistent spanning arborescence using Kruskal.
        
        The spanning tree is NOT minimal.
        
        The quintuple returned contains:
        - Set of the edges used in order to build the spanning arborescence.
        - Vector of the connected component of each node.
        - Number of connected components.
        - Minimum component size.
        - Maximum component size.
        
        Parameters
        ----------
        verbose: Optional[bool],
            Whether to show a loading bar or not."""
    
    
    
    def strongly_connected_components(self):
        """Returns list of nodes of the various strongly connected components.
        
        This is an implementation of Tarjan algorithm."""
    
    
    
    def textual_report(self):
        """Return html short textual report of the graph.
        
        TODO! Add reports on triangles
        TODO! Add reports on connected components
        TODO! Add reports on various node metrics
        TODO! Add reports on various edge metrics
        NOTE! Most of the above TODOs will require first to implement the
        support for the fast computation of the inbound edges in a directed
        graphs"""
    
    
    
    def to_anti_diagonal(self):
        """Return the graph from the anti-diagonal adjacency matrix."""
    
    
    
    def to_arrowhead(self):
        """Return the graph from the arrowhead adjacency matrix."""
    
    
    
    def to_bidiagonal(self):
        """Return the graph from the bidiagonal adjacency matrix."""
    
    
    
    def to_complementary(self):
        """Return the complementary graph."""
    
    
    
    def to_directed(self):
        """Return a new instance of the current graph as directed"""
    
    
    
    def to_directed_inplace(self):
        """Convert inplace the graph to directed."""
    
    
    
    def to_dot(self):
        """Print the current graph in a format compatible with Graphviz dot's format"""
    
    
    
    def to_lower_triangular(self):
        """Return the directed graph from the lower triangular adjacency matrix."""
    
    
    
    def to_main_diagonal(self):
        """Return the graph from the main diagonal adjacency matrix."""
    
    
    
    def to_transposed(self):
        """Return the graph from the transposed adjacency matrix."""
    
    
    
    def to_upper_triangular(self):
        """Return the directed graph from the upper triangular adjacency matrix."""
    
    
    
    def validate_edge_id(self, edge_id: int):
        """Validates provided edge ID.
        
        Parameters
        ----------
        edge_id: int,
            Edge ID to validate.
        
        
        Raises
        -------
        ValueError
            If the given edge ID does not exists in the graph."""
    
    
    
    def validate_edge_ids(self, edge_ids: List[int]):
        """Validates provided edge IDs.
        
        Parameters
        ----------
        edge_ids: List[int],
            Edge IDs to validate.
        
        
        Raises
        -------
        ValueError
            If any of the given edge ID does not exists in the graph."""
    
    
    
    def validate_edge_type_id(self, edge_type_id: Optional[int]):
        """Validates provided edge type ID.
        
        Parameters
        ----------
        edge_type_id: Optional[int],
            edge type ID to validate.
        
        
        Raises
        -------
        ValueError
            If the given edge type ID does not exists in the graph."""
    
    
    
    def validate_edge_type_ids(self, edge_type_ids: List[Optional[int]]):
        """Validates provided edge type IDs.
        
        Parameters
        ----------
        edge_type_ids: List[Optional[int]],
            Vector of edge type IDs to validate.
        
        
        Raises
        -------
        ValueError
            If there are no edge types in the graph."""
    
    
    
    def validate_node_id(self, node_id: int):
        """Validates provided node ID.
        
        Parameters
        ----------
        node_id: int,
            node ID to validate.
        
        
        Raises
        -------
        ValueError
            If the given node ID does not exists in the graph."""
    
    
    
    def validate_node_ids(self, node_ids: List[int]):
        """Validates all provided node IDs.
        
        Parameters
        ----------
        node_ids: List[int],
            node IDs to validate.
        
        
        Raises
        -------
        ValueError
            If any of the given node ID does not exists in the graph."""
    
    
    
    def validate_node_type_id(self, node_type_id: Optional[int]):
        """Validates provided node type ID.
        
        Parameters
        ----------
        node_type_id: Optional[int],
            Node type ID to validate.
        
        
        Raises
        -------
        ValueError
            If the given node type ID does not exists in the graph."""
    
    
    
    def validate_node_type_ids(self, node_type_ids: List[Optional[int]]):
        """Validates provided node type IDs.
        
        Parameters
        ----------
        node_type_ids: List[Optional[int]],
            Vector of node type IDs to validate.
        
        
        Raises
        -------
        ValueError
            If there are no node types in the graph."""
    
    