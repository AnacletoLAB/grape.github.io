import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def KGPhenio(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return kg-phenio graph	

    Parameters
    ----------
    directed = False
    preprocess = "auto"
        Preprocess for optimal load time & memory peak.
        Will preprocess in Linux/macOS but not Windows.
    load_nodes = True
        Load node names or use numeric range
    auto_enable_tradeoffs = True
        Enable when graph has < 50M edges
    cache_path = None
        Path to store graphs
        Defaults either to `GRAPH_CACHE_DIR` sys var or `graphs`
    cache_sys_var = "GRAPH_CACHE_DIR"
    version = "current"
        Version to retrieve	
		The available versions are:
			- 20220304
			- 20220414
			- 20220428
			- 20220429
			- 20220504
			- 20220506
			- 20220511
			- 20220513
			- 20220516
			- 20220525
			- 20220601
			- 20220606
			- 20220607
			- 20220623
			- current	
	
	
    """
