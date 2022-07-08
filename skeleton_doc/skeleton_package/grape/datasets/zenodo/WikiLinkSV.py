import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def WikiLinkSV(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return WikiLinkSV2001 graph	

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
    version = "2018"
        Version to retrieve	
		The available versions are:
			- 2001
			- 2002
			- 2003
			- 2004
			- 2005
			- 2006
			- 2007
			- 2008
			- 2009
			- 2010
			- 2011
			- 2012
			- 2013
			- 2014
			- 2015
			- 2016
			- 2017
			- 2018	
	
	References
	----------
	Please cite:
	
	```bib
	@inproceedings{consonni2019wikilinkgraphs,
	  title={WikiLinkGraphs: a complete, longitudinal and multi-language dataset of the Wikipedia link networks},
	  author={Consonni, Cristian and Laniado, David and Montresor, Alberto},
	  booktitle={Proceedings of the International AAAI Conference on Web and Social Media},
	  volume={13},
	  pages={598--607},
	  year={2019}
	}
	```
    """
