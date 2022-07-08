import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def SocAcademia(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return soc-academia graph	

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
	
	@inproceedings{Fire2011,
	        title={Link Prediction in Social Networks using Computationally Efficient Topological Features},
	        author={Fire, M. and Tenenboim, L. and Lesser, O. and Puzis, R. and Rokach, L. and Elovici, Y.},
	        booktitle={ IEEE Third International Confernece on Social Computing (SocialCom)},
	        pages={73--80},
	        year={2011},
	        organization={IEEE}
	}
	```
    """
