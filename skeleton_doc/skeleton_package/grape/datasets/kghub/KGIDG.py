import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def KGIDG(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return KG-IDG graph	

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
			- 20211029
			- 20211101
			- 20211112
			- 20211123
			- 20211201
			- 20211202
			- 20211207
			- 20211210
			- 20211213
			- 20211215
			- 20211221
			- 20211223
			- 20220101
			- 20220106
			- 20220107
			- 20220119
			- 20220201
			- 20220203
			- 20220204
			- 20220216
			- 20220223
			- 20220303
			- 20220325
			- 20220329
			- 20220401
			- 20220501
			- 20220512
			- 20220525
			- 20220601
			- 20220606
			- 20220701
			- current	
	
	
    """
