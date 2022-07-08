import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

class DeepWalkSkipGramEnsmallen:
    """Class providing DeepWalk SkipGram implemeted in Rust from Ensmallen."""
    
    
    def can_use_edge_types(cls: None) -> bool:
        """Returns whether the model can optionally use edge types."""
    
    
    
    def can_use_edge_weights(cls: None) -> bool:
        """Returns whether the model can optionally use edge weights."""
    
    
    
    def can_use_node_types(cls: None) -> bool:
        """Returns whether the model can optionally use node types."""
    
    
    
    def get_model_from_library(cls: None, model_name: str, task_name: typing.Optional[str], library_name: typing.Optional[str]) -> Type:
        """Returns list of models implementations available for given task and model.
    
            Parameters
            -------------------
            model_name: str
                The name of the model to retrieve.
            task_name: Optional[str] = None
                The task that this implementation of the model should be able to do.
                If not provided, it will be returned the model if it has only a single
                possible task. If multiple tasks are available, an exception will
                be raised.
            library_name: Optional[str] = None
                The library from which to get the implementation of this model.
                If not provided, it will be returned the model if it has only a single
                possible library. If multiple librarys are available, an exception will
                be raised.
            """
    
    
    
    def is_stocastic(cls: None) -> bool:
        """Returns whether the model is stocastic and has therefore a random state."""
    
    
    
    def library_name(cls: None) -> str:
        """TODO!: document this"""
    
    
    
    def model_name(cls: None) -> str:
        """Returns name of the model."""
    
    
    
    def requires_edge_types(cls: None) -> bool:
        """TODO!: document this"""
    
    
    
    def requires_edge_weights(cls: None) -> bool:
        """TODO!: document this"""
    
    
    
    def requires_node_types(cls: None) -> bool:
        """TODO!: document this"""
    
    
    
    def requires_positive_edge_weights(cls: None) -> bool:
        """TODO!: document this"""
    
    
    
    def smoke_test_parameters(cls: None) -> Dict:
        """Returns parameters for smoke test."""
    
    
    
    def task_involves_edge_types(cls: None) -> bool:
        """Returns whether the model task involves edge types."""
    
    
    
    def task_involves_edge_weights(cls: None) -> bool:
        """Returns whether the model task involves edge weights."""
    
    
    
    def task_involves_node_types(cls: None) -> bool:
        """Returns whether the model task involves node types."""
    
    
    
    def task_involves_topology(cls: None) -> bool:
        """Returns whether the model task involves topology."""
    
    
    
    def task_name(cls: None) -> str:
        """TODO!: document this"""
    
    