import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def AffAmazonCopurchases(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return aff-amazon-copurchases graph	

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
	
	@article{leskovec2007dynamics,
	        title={The dynamics of viral marketing},
	        author={Leskovec, Jure and Adamic, Lada A and Huberman, Bernardo A},
	        journal={ACM Transactions on the Web (TWEB)},
	        volume={1},
	        number={1},
	        pages={5},
	        year={2007},
	        publisher={ACM}
	}
	```
    """
