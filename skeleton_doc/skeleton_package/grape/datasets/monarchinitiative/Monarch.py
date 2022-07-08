import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def Monarch(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return Monarch graph	

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
    version = "2022-06-30"
        Version to retrieve	
		The available versions are:
			- 202012
			- 202103
			- 2022-02-10
			- 2022-03-07
			- 2022-03-15
			- 2022-03-30
			- 2022-04-11
			- 2022-04-13
			- 2022-04-20
			- 2022-04-29
			- 2022-05-05
			- 2022-05-07
			- 2022-05-10
			- 2022-05-17
			- 2022-05-23
			- 2022-05-24
			- 2022-05-26
			- 2022-05-27
			- 2022-06-02
			- 2022-06-07
			- 2022-06-08
			- 2022-06-28
			- 2022-06-30
    """
