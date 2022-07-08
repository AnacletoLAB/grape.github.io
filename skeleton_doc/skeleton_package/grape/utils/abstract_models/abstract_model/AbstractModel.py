import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas
import numpy
import embiggen


class AbstractModel:
    """Class defining properties of a generic abstract model."""
    
    
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
    
    
    
    def is_topological(cls: None) -> bool:
        """Returns whether this embedding is based on graph topology."""
    
    
    
    def library_name(cls: None) -> str:
        """Returns library name of the model."""
    
    
    
    def model_name(cls: None) -> str:
        """Returns model name of the model."""
    
    
    
    def requires_edge_types(cls: None) -> bool:
        """Returns whether the model requires edge types."""
    
    
    
    def requires_edge_weights(cls: None) -> bool:
        """Returns whether the model requires edge weights."""
    
    
    
    def requires_node_types(cls: None) -> bool:
        """Returns whether the model requires node types."""
    
    
    
    def requires_positive_edge_weights(cls: None) -> bool:
        """Returns whether the model requires positive edge weights."""
    
    
    
    def smoke_test_parameters(cls: None) -> Dict:
        """Return parameters to create a model with minimal configuration to test execution."""
    
    
    
    def task_involves_edge_types(cls: None) -> bool:
        """Returns whether the model task involves edge types."""
    
    
    
    def task_involves_edge_weights(cls: None) -> bool:
        """Returns whether the model task involves edge weights."""
    
    
    
    def task_involves_node_types(cls: None) -> bool:
        """Returns whether the model task involves node types."""
    
    
    
    def task_involves_topology(cls: None) -> bool:
        """Returns whether the model task involves topology."""
    
    
    
    def task_name(cls: None) -> str:
        """Returns the task for which this model is being used."""
    
    