import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

class ShortestPathsDjkstra:
    """TODO!: document this"""
    
    def get_distance_from_node_id(self):
        """TODO!: document this"""
    
    
    
    def get_eccentricity(self):
        """TODO!: document this"""
    
    
    
    def get_median_point(self):
        """TODO!: document this"""
    
    
    
    def get_most_distant_node(self):
        """TODO!: document this"""
    
    
    
    def get_parent_from_node_id(self):
        """TODO!: document this"""
    
    
    
    def get_point_at_given_distance_on_shortest_path(self, dst_node_id: int, distance: float):
        """Returns node at just before given distance on minimum path to given destination node.
        
        Parameters
        ----------
        dst_node_id: int,
            The node to start computing predecessors from.
        distance: float,
            The distance to aim for.
        
        
        Raises
        -------
        ValueError
            If the predecessors vector was not requested."""
    
    
    
    def has_path_to_node_id(self):
        """TODO!: document this"""
    
    