import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def FBBT(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return FBBT graph	

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
    version = "2022-04-13"
        Version to retrieve	
		The available versions are:
			- 2022-06-09
			- 2021-09-01
			- 2021-10-14
			- 2021-12-09
			- 2022-01-27
			- 2022-02-24
			- 2022-04-13
    """
