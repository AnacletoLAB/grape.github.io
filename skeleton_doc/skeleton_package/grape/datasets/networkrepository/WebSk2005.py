import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def WebSk2005(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return web-sk-2005 graph	

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
	
	@ARTICLE{boldi2004-ubicrawler,
	        author = {Paolo Boldi and Bruno Codenotti and Massimo Santini and Sebastiano Vigna},
	        title = {{UbiCrawler}: A Scalable Fully Distributed Web Crawler},
	        journal = {Software: Practice \& Experience},
	        year = {2004},
	        volume = {34},
	        pages = {711--726},
	        number = {8}}
	
	@INPROCEEDINGS{Boldi-2011-layered,
	        author = {Paolo Boldi and Marco Rosa and Massimo Santini and Sebastiano Vigna},
	        title = {Layered Label Propagation: A MultiResolution Coordinate-Free Ordering	for Compressing Social Networks},
	        booktitle = {WWW},
	        year = {2011},
	        pages = {587--596}
	}
	```
    """
