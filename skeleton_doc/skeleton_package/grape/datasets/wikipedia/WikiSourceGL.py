import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def WikiSourceGL(directed: bool, load_nodes: bool, load_node_types: bool, keep_nodes_without_descriptions: bool, keep_nodes_without_categories: bool, keep_interwikipedia_nodes: bool, keep_external_nodes: bool, compute_node_description: bool, auto_enable_tradeoffs: bool, sort_tmp_dir: str, verbose: int, cache: bool, cache_path: str, cache_sys_var: str, version: str) -> Graph:
    """Return new instance of the WikiSourceGL graph.

    The graph is automatically retrieved from the Wikipedia repository.	

    Parameters
    -------------------
    directed: bool = False
        Wether to load the graph as directed or undirected.
        By default false.
    load_nodes: bool = True
        Whether to load the nodes vocabulary or treat the nodes
        simply as a numeric range.
    load_node_types: bool = True
        Whether to load the node types or skip them entirely.
        This feature is only available when the preprocessing is enabled.
    keep_nodes_without_descriptions: bool = True
        Whether to keep the nodes laking a description
    keep_nodes_without_categories: bool = True
        Whether to keep the nodes laking a category
    keep_interwikipedia_nodes: bool = True
        Whether to keep nodes from external wikipedia websites
    keep_external_nodes: bool = True
        Whether to keep nodes from external websites (non wikipedia ones).
    compute_node_description: bool = False
        Whether to compute the node descriptions.
        Note that this will significantly increase the side of the node lists!
    auto_enable_tradeoffs: bool = True
        Whether to enable the Ensmallen time-memory tradeoffs in small graphs
        automatically. By default True, that is, if a graph has less than
        50 million edges. In such use cases the memory expenditure is minimal.
    sort_tmp_dir: str = None
        Which folder to use to store the temporary files needed to sort in 
        parallel the edge list when building the optimal preprocessed file.
        This defaults to the same folder of the edge list when no value is 
        provided.
    verbose: int = 2
        Wether to show loading bars during the retrieval and building
        of the graph.
    cache: bool = True
        Whether to use cache, i.e. download files only once
        and preprocess them only once.
    cache_path: str = None
        Where to store the downloaded graphs.
        If no path is provided, first we check the system variable
        provided below is set, otherwise we use the directory `graphs`.
    cache_sys_var: str = "GRAPH_CACHE_DIR"
        The system variable with the default graph cache directory.
    version: str = "latest"
        The version of the graph to retrieve.	
		The available versions are:
			- 20220220
			- 20220301
			- 20220320
			- 20220401
			- 20220420
			- 20220501
			- 20220520
			- 20220601
			- 20220620
			- 20220701
			- latest
    graph_kwargs
        Additional graph kwargs.	
	
	
    """
