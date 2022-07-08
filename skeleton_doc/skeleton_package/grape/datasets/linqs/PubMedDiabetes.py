import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def PubMedDiabetes(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return PubMedDiabetes graph	The Pubmed Diabetes dataset consists of 19717 scientific publications from
	PubMed database pertaining to diabetes classified into one of three classes.
	The citation network consists of 44338 links. Each publication in the dataset
	is described by a TF/IDF weighted word vector from a dictionary which consists
	of 500 unique words.

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
	@inproceedings{namata2012query,
	  title={Query-driven active surveying for collective classification},
	  author={Namata, Galileo and London, Ben and Getoor, Lise and Huang, Bert and EDU, UMD},
	  booktitle={10th International Workshop on Mining and Learning with Graphs},
	  volume={8},
	  year={2012}
	}
	```
    """
