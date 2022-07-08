import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def GiantTN(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return GIANT-TN graph	

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
    version = "latest"
        Version to retrieve		
	
	References
	----------
	Please cite:
	
	```bib
	@article{liu2020supervised,
	  title={Supervised learning is an accurate method for network-based gene classification},
	  author={Liu, Renming and Mancuso, Christopher A and Yannakopoulos, Anna and Johnson, Kayla A and Krishnan, Arjun},
	  journal={Bioinformatics},
	  volume={36},
	  number={11},
	  pages={3457--3465},
	  year={2020},
	  publisher={Oxford University Press}
	}
	```
    """
