import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def SocEpinions(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return soc-epinions graph	

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
	
	@incollection{richardson2003trust,
	        title={Trust management for the semantic web},
	        author={Richardson, Matthew and Agrawal, Rakesh and Domingos, Pedro},
	        booktitle={The Semantic Web-ISWC 2003},
	        pages={351--368},
	        year={2003},
	        publisher={Springer}
	}
	
	@inproceedings{nr:massa05,
	        title = {Controversial Users Demand Local Trust Metrics: An Experimental Study on epinions.com Community},
	        author = {Paolo Massa and Paolo Avesani},
	        booktitle = {AAAI},
	        year = {2005},
	        pages = {121--126},
	}
	```
    """
