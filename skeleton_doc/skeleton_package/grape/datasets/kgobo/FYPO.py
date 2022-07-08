import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def FYPO(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return FYPO graph	

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
    version = "2022-05-16"
        Version to retrieve	
		The available versions are:
			- 2022-06-20
			- 2021-10-05
			- 2021-11-08
			- 2021-11-18
			- 2021-12-07
			- 2022-01-18
			- 2022-01-27
			- 2022-04-22
			- 2022-04-28
			- 2022-05-11
			- 2022-05-16
    """
