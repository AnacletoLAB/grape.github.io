import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def MS(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return MS graph	

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
    version = "4.1.89"
        Version to retrieve	
		The available versions are:
			- 4.1.91
			- 4.1.35
			- 4.1.62
			- 4.1.64
			- 4.1.65
			- 4.1.67
			- 4.1.69
			- 4.1.70
			- 4.1.71
			- 4.1.78
			- 4.1.82
			- 4.1.83
			- 4.1.84
			- 4.1.86
			- 4.1.88
			- 4.1.89
    """
