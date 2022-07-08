import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas
import numpy
import embiggen


def classification_evaluation_pipeline(evaluation_schema: str, holdouts_kwargs: typing.Dict[str, typing.Any], graphs: typing.Union[str, Graph, typing.List[Graph], typing.List[str]], models: typing.Union[typing.Type[embiggen.utils.abstract_models.abstract_classifier_model.AbstractClassifierModel], typing.List[typing.Type[embiggen.utils.abstract_models.abstract_classifier_model.AbstractClassifierModel]]], expected_parent_class: typing.Type[embiggen.utils.abstract_models.abstract_classifier_model.AbstractClassifierModel], node_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]]], None], node_type_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]]], None], edge_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray]], None], library_names: typing.Union[str, typing.List[str], None], graph_callback: typing.Optional[typing.Callable[[Graph], Graph]], subgraph_of_interest: typing.Optional[Graph], number_of_holdouts: int, random_state: int, repositories: typing.Union[str, typing.List[str], None], versions: typing.Union[str, typing.List[str], None], enable_cache: bool, precompute_constant_automatic_stocastic_features: bool, smoke_test: bool) -> pandas.DataFrame:
    """Execute classification pipeline for all provided models and graphs.
    
    Parameters
    ---------------------
    evaluation_schema: str
        The evaluation schema to follow.
    holdouts_kwargs: Dict[str, Any]
        The parameters for the selected holdouts method.
    graphs: Union[str, Graph, List[Graph], List[str]]
        The graphs or graph names to run this evaluation on.
    models: Union[Type[AbstractClassifierModel], List[Type[AbstractClassifierModel]]]
        The models to evaluate.
    expected_parent_class: Type[AbstractClassifierModel]
        The expected parent class of the models, necessary to validate that the models are what we expect.
    node_features: Optional[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel], List[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]]]]] = None
        The node features to use.
    edge_features: Optional[Union[str, pd.DataFrame, np.ndarray, List[Union[str, pd.DataFrame, np.ndarray]]]] = None
        The edge features to use.
    library_names: Optional[Union[str, List[str]]] = None
        Library names from where to retrieve the provided model names.
    graph_callback: Optional[Callable[[Graph], Graph]] = None
        Callback to use for graph normalization and sanitization, must be
        a function that receives and returns a graph object.
        For instance this may be used for filtering the uncertain edges
        in graphs such as STRING PPIs.
    subgraph_of_interest: Optional[Graph] = None
        The subgraph of interest to focus the task on.
    number_of_holdouts: int = 10
        The number of holdouts to execute.
    random_state: int = 42
        Random state to reproduce this evaluation.
    repositories: Optional[Union[str, List[str]]] = None
        Repositories from where to retrieve the provided graph names
        from the Ensmallen automatic retrieval.
    versions: Optional[Union[str, List[str]]] = None
        Graph versions to retrieve.
    enable_cache: bool = False
        Whether to enable the cache.
    precompute_constant_automatic_stocastic_features: bool = False
        Whether to precompute once the constant automatic stocastic
        features before starting the embedding loop. This means that,
        when left set to false, while the features will be computed
        using the same input data, the random state between runs will
        be different and therefore the experiment performance will
        capture more of the variance derived from the stocastic aspect
        of the considered method. When set to true, they are only computed
        once and therefore the experiment will be overall faster.
    smoke_test: bool = False
        Whether this run should be considered a smoke test
        and therefore use the smoke test configurations for
        the provided model names and feature names.
        This parameter will also turn off the cache.
    **evaluation_kwargs: Dict
        Keyword arguments to forward to evaluation.
    """
