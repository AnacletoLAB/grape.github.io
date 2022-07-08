import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

def build_string_cluster_graph_node_and_edge_list(cluster_info_path: str, cluster_tree_path: str, cluster_to_proteins_path: str, sequence_path: str, enrichment_path: str, info_path: str, node_list_path: str, edge_list_path: str):
    """Build labeled edge and node list for cluster graphs.
    
    Parameters
    -----------------------
    cluster_info_path: str
        Path from where to load the cluster node list informations.
    cluster_tree_path: str
        Path from where to load the cluster to cluster edge list.
    cluster_to_proteins_path: str
        Path from where to load the cluster to protein edge list.
    sequence_path: str
        File from where to load sequence data.
    enrichment_path: str
        File from where to load enrichment data.
    info_path: str
        File from where to load info data.
    target_path: str
        Path where to write the resulting node list TSV.
    """
