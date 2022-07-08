import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def BNMouseRetina(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return bn-mouse_retina_1 graph	

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
	
	@article {bigbrain,
	     author = {Amunts, Katrin and Lepage, Claude and Borgeat, Louis and Mohlberg, Hartmut and Dickscheid, Timo and Rousseau, Marc-{'E}tienne and Bludau,
	Sebastian and Bazin, Pierre-Louis and Lewis, Lindsay B. and Oros-Peusquens, Ana-Maria and Shah, Nadim J. and Lippert, Thomas and Zilles, Karl and Evans, Alan C.},
	     title = {BigBrain: An Ultrahigh-Resolution 3D Human Brain Model},
	     volume = {340},
	     number = {6139},
	     pages = {1472--1475},
	     year = {2013},
	     publisher = {AAAS},
	     journal = {Science}
	}
	```
    """
