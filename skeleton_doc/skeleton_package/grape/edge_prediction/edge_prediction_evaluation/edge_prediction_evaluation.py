import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas
import numpy
import embiggen


def edge_prediction_evaluation(holdouts_kwargs: typing.Dict[str, typing.Any], graphs: typing.Union[str, Graph, typing.List[Graph], typing.List[str]], models, evaluation_schema: str, node_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]]], None], node_type_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]]], None], library_names: typing.Union[str, typing.List[str], None], graph_callback: typing.Optional[typing.Callable[[Graph], Graph]], subgraph_of_interest: typing.Optional[Graph], number_of_holdouts: int, random_state: int, repositories: typing.Union[str, typing.List[str], None], versions: typing.Union[str, typing.List[str], None], validation_sample_only_edges_with_heterogeneous_node_types: bool, validation_unbalance_rates: typing.Tuple[float], use_scale_free_distribution: bool, enable_cache: bool, precompute_constant_automatic_stocastic_features: bool, smoke_test: bool, verbose: bool) -> pandas.DataFrame:
    """Execute edge prediction evaluation pipeline for all provided models and graphs.

    Parameters
    ---------------------
    holdouts_kwargs: Dict[str, Any]
        The parameters for the selected holdouts method.
    graphs: Union[str, Graph, List[Graph], List[str]]
        The graphs or graph names to run this evaluation on.
    models: Union[Type[AbstractEdgePredictionModel], List[Type[AbstractEdgePredictionModel]]]
        The models to evaluate.
    evaluation_schema: str = "Connected Monte Carlo"
        The evaluation schema to follow.
        There are a number of supported evaluation schemas, specifically:
        - Connected Monte Carlo
            A random holdout with repeated sampling of the edges across the different
            repetitions, that assures that there will be exactly the same connected components
            in the training set. This is the ideal evaluation schema when making a closed
            world assumption, that is when you do not want to evaluate the edge prediction performance
            of a model for edges between distinct connected components.
            This is generally used expecially when you do not have additional node features that may
            help the model learn that two different components are connected.
        - Monte Carlo
            A random holdout with repeated sampling of the edges across the different 
            repetitions which DOES NOT HAVE any assurance about creating new connected components.
            This is a correct evaluation schema when you want to evaluate the edge prediction
            performance of a model across different connected components, which you may want to
            do when you have additional node features that may
            help the model learn that two different components are connected.
        - Kfold
            A k-fold holdout which will split the set of edges into k different `folds`, where
            k is the total number of holdouts that will be executed.
            Do note that this procedure DOES NOT HAVE any assurance about creating new connected components.
            This is a correct evaluation schema when you want to evaluate the edge prediction
            performance of a model across different connected components, which you may want to
            do when you have additional node features that may
            help the model learn that two different components are connected.
    node_features: Optional[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel], List[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]]]]] = None
        The node features to use.
    node_type_features: Optional[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel], List[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]]]]] = None
        The node type features to use.
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
    validation_sample_only_edges_with_heterogeneous_node_types: bool = False
        Whether to sample negative edges exclusively between nodes with different node types.
        This can be useful when executing a bipartite edge prediction task.
    validation_unbalance_rates: Tuple[float] = (1.0, )
        Unbalance rate for the non-existent graphs generation.
    use_scale_free_distribution: bool = True
        Whether to use the scale free sampling of the NEGATIVE edges for the EVALUATION
        of the edge prediction performance of the provided models.
        Please DO BE ADVISED that not using a scale free sampling for the negative
        edges is a poor choice and will cause a significant positive bias
        in the model performance.
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
    verbose: bool = True
        Whether to show loading bars
    """
