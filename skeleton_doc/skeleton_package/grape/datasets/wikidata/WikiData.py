import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def WikiData(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return Wikidata graph	

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
    version = "latest-truthy"
        Version to retrieve	
		The available versions are:
			- wikidata-20220518-truthy-BETA
			- wikidata-20220520-lexemes-BETA
			- wikidata-20220523-all-BETA
			- wikidata-20220525-truthy-BETA
			- wikidata-20220527-lexemes-BETA
			- wikidata-20220530-all-BETA
			- wikidata-20220601-truthy-BETA
			- wikidata-20220603-lexemes-BETA
			- wikidata-20220606-all-BETA
			- wikidata-20220608-truthy-BETA
			- wikidata-20220610-lexemes-BETA
			- wikidata-20220613-all-BETA
			- wikidata-20220615-truthy-BETA
			- wikidata-20220617-lexemes-BETA
			- wikidata-20220620-all-BETA
			- wikidata-20220622-truthy-BETA
			- wikidata-20220624-lexemes-BETA
			- wikidata-20220627-all-BETA
			- wikidata-20220629-truthy-BETA
			- wikidata-20220701-lexemes-BETA
			- latest-all
			- latest-lexemes
			- latest-truthy
    """
