import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def PheKnowLator(directed: None, preprocess: None, load_nodes: None, load_node_types: None, load_edge_weights: None, auto_enable_tradeoffs: None, sort_tmp_dir: None, verbose: None, cache: None, cache_path: None, cache_sys_var: None, version: None) -> Graph:
    """Return PheKnowLator graph	

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
    version = "v3.0.2-2021-10-18.subclass-relationsOnly-owlnets-purified"
        Version to retrieve	
		The available versions are:
			- v2.0.0-2020-5-10.instance-inverseRelations-owl
			- v2.0.0-2020-5-10.instance-inverseRelations-owlnets
			- v2.0.0-2020-5-10.instance-relationsOnly-owl
			- v2.0.0-2020-5-10.instance-relationsOnly-owlnets
			- v2.0.0-2020-5-10.subclass-inverseRelations-owl
			- v2.0.0-2020-5-10.subclass-inverseRelations-owlnets
			- v2.0.0-2020-5-10.subclass-relationsOnly-owl
			- v2.0.0-2020-5-10.subclass-relationsOnly-owlnets
			- v2.0.0-2021-1-25.instance-inverseRelations-owl
			- v2.0.0-2021-1-25.instance-inverseRelations-owlnets
			- v2.0.0-2021-1-25.instance-inverseRelations-owlnets-purified
			- v2.0.0-2021-1-25.instance-relationsOnly-owl
			- v2.0.0-2021-1-25.instance-relationsOnly-owlnets
			- v2.0.0-2021-1-25.instance-relationsOnly-owlnets-purified
			- v2.0.0-2021-1-25.subclass-inverseRelations-owl
			- v2.0.0-2021-1-25.subclass-inverseRelations-owlnets
			- v2.0.0-2021-1-25.subclass-inverseRelations-owlnets-purified
			- v2.0.0-2021-1-25.subclass-relationsOnly-owl
			- v2.0.0-2021-1-25.subclass-relationsOnly-owlnets
			- v2.0.0-2021-1-25.subclass-relationsOnly-owlnets-purified
			- v2.0.0-2021-2-11.instance-inverseRelations-owl
			- v2.0.0-2021-2-11.instance-inverseRelations-owlnets
			- v2.0.0-2021-2-11.instance-inverseRelations-owlnets-purified
			- v2.0.0-2021-2-11.instance-relationsOnly-owl
			- v2.0.0-2021-2-11.instance-relationsOnly-owlnets
			- v2.0.0-2021-2-11.instance-relationsOnly-owlnets-purified
			- v2.0.0-2021-2-11.subclass-inverseRelations-owl
			- v2.0.0-2021-2-11.subclass-inverseRelations-owlnets
			- v2.0.0-2021-2-11.subclass-inverseRelations-owlnets-purified
			- v2.0.0-2021-2-11.subclass-relationsOnly-owl
			- v2.0.0-2021-2-11.subclass-relationsOnly-owlnets
			- v2.0.0-2021-2-11.subclass-relationsOnly-owlnets-purified
			- v2.1.0-2021-5-01.instance-inverseRelations-owl
			- v2.1.0-2021-5-01.instance-inverseRelations-owlnets
			- v2.1.0-2021-5-01.instance-inverseRelations-owlnets-purified
			- v2.1.0-2021-5-01.instance-relationsOnly-owl
			- v2.1.0-2021-5-01.instance-relationsOnly-owlnets
			- v2.1.0-2021-5-01.instance-relationsOnly-owlnets-purified
			- v2.1.0-2021-5-01.subclass-inverseRelations-owl
			- v2.1.0-2021-5-01.subclass-inverseRelations-owlnets
			- v2.1.0-2021-5-01.subclass-inverseRelations-owlnets-purified
			- v2.1.0-2021-5-01.subclass-relationsOnly-owl
			- v2.1.0-2021-5-01.subclass-relationsOnly-owlnets
			- v2.1.0-2021-5-01.subclass-relationsOnly-owlnets-purified
			- v2.1.0-2021-6-01.instance-inverseRelations-owl
			- v2.1.0-2021-6-01.instance-inverseRelations-owlnets
			- v2.1.0-2021-6-01.instance-inverseRelations-owlnets-purified
			- v2.1.0-2021-6-01.instance-relationsOnly-owl
			- v2.1.0-2021-6-01.instance-relationsOnly-owlnets
			- v2.1.0-2021-6-01.instance-relationsOnly-owlnets-purified
			- v2.1.0-2021-6-01.subclass-inverseRelations-owl
			- v2.1.0-2021-6-01.subclass-inverseRelations-owlnets
			- v2.1.0-2021-6-01.subclass-inverseRelations-owlnets-purified
			- v2.1.0-2021-6-01.subclass-relationsOnly-owl
			- v2.1.0-2021-6-01.subclass-relationsOnly-owlnets
			- v2.1.0-2021-6-01.subclass-relationsOnly-owlnets-purified
			- v2.1.0-2021-7-06.instance-inverseRelations-owl
			- v2.1.0-2021-7-06.instance-inverseRelations-owlnets
			- v2.1.0-2021-7-06.instance-inverseRelations-owlnets-purified
			- v2.1.0-2021-7-06.instance-relationsOnly-owl
			- v2.1.0-2021-7-06.instance-relationsOnly-owlnets
			- v2.1.0-2021-7-06.instance-relationsOnly-owlnets-purified
			- v2.1.0-2021-7-06.subclass-inverseRelations-owl
			- v2.1.0-2021-7-06.subclass-inverseRelations-owlnets
			- v2.1.0-2021-7-06.subclass-inverseRelations-owlnets-purified
			- v2.1.0-2021-7-06.subclass-relationsOnly-owl
			- v2.1.0-2021-7-06.subclass-relationsOnly-owlnets
			- v2.1.0-2021-7-06.subclass-relationsOnly-owlnets-purified
			- v2.1.0-2021-8-01.instance-inverseRelations-owl
			- v2.1.0-2021-8-01.instance-inverseRelations-owlnets
			- v2.1.0-2021-8-01.instance-inverseRelations-owlnets-purified
			- v2.1.0-2021-8-01.instance-relationsOnly-owl
			- v2.1.0-2021-8-01.instance-relationsOnly-owlnets
			- v2.1.0-2021-8-01.instance-relationsOnly-owlnets-purified
			- v2.1.0-2021-8-01.subclass-inverseRelations-owl
			- v2.1.0-2021-8-01.subclass-inverseRelations-owlnets
			- v2.1.0-2021-8-01.subclass-inverseRelations-owlnets-purified
			- v2.1.0-2021-8-01.subclass-relationsOnly-owl
			- v2.1.0-2021-8-01.subclass-relationsOnly-owlnets
			- v2.1.0-2021-8-01.subclass-relationsOnly-owlnets-purified
			- v2.1.0-2021-9-01.instance-inverseRelations-owl
			- v2.1.0-2021-9-01.instance-inverseRelations-owlnets
			- v2.1.0-2021-9-01.instance-inverseRelations-owlnets-purified
			- v2.1.0-2021-9-01.instance-relationsOnly-owl
			- v2.1.0-2021-9-01.instance-relationsOnly-owlnets
			- v2.1.0-2021-9-01.instance-relationsOnly-owlnets-purified
			- v2.1.0-2021-9-01.subclass-inverseRelations-owl
			- v2.1.0-2021-9-01.subclass-inverseRelations-owlnets
			- v2.1.0-2021-9-01.subclass-inverseRelations-owlnets-purified
			- v2.1.0-2021-9-01.subclass-relationsOnly-owl
			- v2.1.0-2021-9-01.subclass-relationsOnly-owlnets
			- v2.1.0-2021-9-01.subclass-relationsOnly-owlnets-purified
			- v3.0.2-2021-1-01.instance-inverseRelations-owl
			- v3.0.2-2021-1-01.instance-inverseRelations-owlnets
			- v3.0.2-2021-1-01.instance-inverseRelations-owlnets-purified
			- v3.0.2-2021-1-01.instance-relationsOnly-owl
			- v3.0.2-2021-1-01.instance-relationsOnly-owlnets
			- v3.0.2-2021-1-01.instance-relationsOnly-owlnets-purified
			- v3.0.2-2021-1-01.subclass-inverseRelations-owl
			- v3.0.2-2021-1-01.subclass-inverseRelations-owlnets
			- v3.0.2-2021-1-01.subclass-inverseRelations-owlnets-purified
			- v3.0.2-2021-1-01.subclass-relationsOnly-owl
			- v3.0.2-2021-1-01.subclass-relationsOnly-owlnets
			- v3.0.2-2021-1-01.subclass-relationsOnly-owlnets-purified
			- v3.0.2-2021-10-18.instance-inverseRelations-owl
			- v3.0.2-2021-10-18.instance-inverseRelations-owlnets
			- v3.0.2-2021-10-18.instance-inverseRelations-owlnets-purified
			- v3.0.2-2021-10-18.instance-relationsOnly-owl
			- v3.0.2-2021-10-18.instance-relationsOnly-owlnets
			- v3.0.2-2021-10-18.instance-relationsOnly-owlnets-purified
			- v3.0.2-2021-10-18.subclass-inverseRelations-owl
			- v3.0.2-2021-10-18.subclass-inverseRelations-owlnets
			- v3.0.2-2021-10-18.subclass-inverseRelations-owlnets-purified
			- v3.0.2-2021-10-18.subclass-relationsOnly-owl
			- v3.0.2-2021-10-18.subclass-relationsOnly-owlnets
			- v3.0.2-2021-10-18.subclass-relationsOnly-owlnets-purified
    """
