import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

class ShortestPathsResultBFS:
    """TODO!: document this"""
    
    def get_distance_from_node_id(self):
        """TODO!: document this"""
    
    
    
    def get_distances(self):
        """TODO!: document this"""
    
    
    
    def get_eccentricity(self):
        """TODO!: document this"""
    
    
    
    def get_kth_point_on_shortest_path(self, dst_node_id: int, k: int):
        """Returns node at the `len - k` position on minimum path to given destination node.
        
        Parameters
        ----------
        dst_node_id: int,
            The node to start computing predecessors from.
        k: int,
            Steps to go back.
        
        
        Raises
        -------
        ValueError
            If the predecessors vector was not requested."""
    
    
    
    def get_median_point(self):
        """TODO!: document this"""
    
    
    
    def get_most_distant_node(self):
        """TODO!: document this"""
    
    
    
    def get_parent_from_node_id(self):
        """TODO!: document this"""
    
    
    
    def has_path_to_node_id(self):
        """TODO!: document this"""
    
    