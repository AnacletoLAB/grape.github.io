import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def BioDiseasome(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return bio-diseasome graph	

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
	@inproceedings{nr,
	    title = {The Network Data Repository with Interactive Graph Analytics and Visualization},
	    author={Ryan A. Rossi and Nesreen K. Ahmed},
	    booktitle = {AAAI},
	    url={http://networkrepository.com},
	    year={2015}
	}
	
	@article{goh2007human,
	        title={The human disease network},
	        author={Goh, Kwang-Il and Cusick, Michael E and Valle, David and Childs, Barton and Vidal, Marc and Barab{'a}si,
	Albert-L{'a}szl{'o}
	},
	        journal={Proceedings of the National Academy of Sciences},
	        volume={104},
	        number={21},
	        pages={8685--8690},
	        year={2007},
	        publisher={National Acad Sciences}
	}
	```
    """
