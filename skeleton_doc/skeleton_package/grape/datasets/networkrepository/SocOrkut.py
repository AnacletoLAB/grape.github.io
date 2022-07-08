import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def SocOrkut(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return soc-orkut graph	

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
	
	@inproceedings{mislove-2007-socialnetworks,
	        author = {Alan Mislove and Massimiliano Marcon and Krishna P. Gummadi and Peter Druschel and Bobby Bhattacharjee},
	        title = {{Measurement and Analysis of Online Social Networks}},
	        booktitle = {Proceedings of the 5th ACM/Usenix Internet Measurement Conference (IMC'07)},
	        address = {San Diego, CA},
	        month = {October},
	        year = {2007}}
	```
    """
