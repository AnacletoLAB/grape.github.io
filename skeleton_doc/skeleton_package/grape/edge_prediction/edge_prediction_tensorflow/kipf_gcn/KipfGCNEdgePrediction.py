import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import pandas
import numpy
import embiggen

class KipfGCNEdgePrediction:
    """Kipf GCN model for edge prediction."""
    
    
    def can_use_edge_types(cls: None) -> bool:
        """Returns whether the model can optionally use edge types."""
    
    
    
    def can_use_edge_weights(cls: None) -> bool:
        """Returns whether the model can optionally use edge weights."""
    
    
    
    def can_use_node_types(cls: None) -> bool:
        """Returns whether the model can optionally use node types."""
    
    
    
    def evaluate_cached() -> pandas.DataFrame:
        """Execute evaluation on the provided graph.
    
            Parameters
            --------------------
            models: Union[Type["AbstractClassifierModel"], List[Type["AbstractClassifierModel"]]]
                The model(s) to be evaluated.
            graph: Graph
                The graph to run predictions on.
            evaluation_schema: str
                The schema for the evaluation to follow.
            holdouts_kwargs: Dict[str, Any]
                Parameters to forward to the desired evaluation schema.
            library_names: Optional[Union[str, List[str]]] = None
                The library names of the models, needed when a desired model is implemented in multiple
                libraries and it is unclear which one to use.
            node_features: Optional[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel], List[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]]]]] = None
                The node features to use.
            node_type_features: Optional[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel], List[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]]]]] = None
                The node features to use.
            edge_features: Optional[Union[str, pd.DataFrame, np.ndarray, List[Union[str, pd.DataFrame, np.ndarray]]]] = None
                The edge features to use.
            subgraph_of_interest: Optional[Graph] = None
                Optional subgraph where to focus the task.
            skip_evaluation_biased_feature: bool = False
                Whether to skip feature names that are known to be biased
                when running an holdout. These features should be computed
                exclusively on the training graph and not the entire graph.
            number_of_holdouts: int = 10
                The number of holdouts to execute.
            random_state: int = 42
                The random state to use for the holdouts.
            verbose: bool = True
                Whether to show a loading bar while computing holdouts.
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
            **validation_kwargs: Dict
                kwargs to be forwarded to the model `_evaluate` method.
            """
    
    
    
    def get_available_edge_embedding_methods(cls: None) -> List:
        """Returns a list of the available edge embedding methods."""
    
    
    
    def get_available_evaluation_schemas(cls: None) -> List:
        """Returns available evaluation schemas for this task."""
    
    
    
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
        """TODO!: document this"""
    
    
    
    def iterate_classifier_models(cls: None, models: typing.Union[str, typing.Type[ForwardRef('AbstractClassifierModel')], typing.List[typing.Type[ForwardRef('AbstractClassifierModel')]]], library_names: typing.Union[str, typing.List[str], None], smoke_test: bool) -> Iterator:
        """Return iterator over the provided models after validation.
    
            Parameters
            -------------------
            models: Union[Type[AbstractClassifierModel], List[Type[AbstractClassifierModel]]]
                The models to validate and iterate on.
            expected_parent_class: Type[AbstractClassifierModel]
                The parent class to check the model against.
            library_names: Optional[Union[str, List[str]]] = None
                Library names from where to retrieve the provided model names.
            smoke_test: bool = False
                Whether this run should be considered a smoke test
                and therefore use the smoke test configurations for
                the provided model names and feature names.
            """
    
    
    
    def library_name(cls: None) -> str:
        """Return name of the model."""
    
    
    
    def model_name(cls: None) -> str:
        """TODO!: document this"""
    
    
    
    def normalize_edge_feature(cls: None, graph: Graph, random_state: int, edge_feature: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, embiggen.utils.abstract_models.embedding_result.EmbeddingResult, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], None], allow_automatic_feature: bool, skip_evaluation_biased_feature: bool, smoke_test: bool, precompute_constant_automatic_stocastic_features: bool) -> List:
        """Normalizes the provided edge features and validates them.
    
            Parameters
            ------------------
            graph: Graph
                The graph to check for.
            random_state: int
                The random state to use for the stochastic automatic features.
            edge_feature: Optional[Union[str, pd.DataFrame, np.ndarray]] = None
                The edge feature to normalize.
            allow_automatic_feature: bool = True
                Whether to allow feature names creation based on the
                provided feature name, using the default settings,
                or based on a provided abstract embedding model that
                will be called on the provided graph.
            skip_evaluation_biased_feature: bool = False
                Whether to skip feature names that are known to be biased
                when running an holdout. These features should be computed
                exclusively on the training graph and not the entire graph.
            smoke_test: bool = False
                Whether this run should be considered a smoke test
                and therefore use the smoke test configurations for
                the provided model names and feature names.
            precompute_constant_automatic_stocastic_features: bool = False
                Whether to precompute once the constant automatic stocastic
                features before starting the embedding loop. This means that,
                when left set to false, while the features will be computed
                using the same input data, the random state between runs will
                be different and therefore the experiment performance will
                capture more of the variance derived from the stocastic aspect
                of the considered method. When set to true, they are only computed
                once and therefore the experiment will be overall faster.
            """
    
    
    
    def normalize_edge_features(cls: None, graph: Graph, random_state: int, edge_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]]], None], allow_automatic_feature: bool, skip_evaluation_biased_feature: bool, smoke_test: bool, precompute_constant_automatic_stocastic_features: bool) -> List:
        """Normalizes the provided edge features and validates them.
    
            Parameters
            ------------------
            graph: Graph
                The graph to check for.
            random_state: int
                The random state to use for the stochastic automatic features.
            edge_features: Optional[Union[str, pd.DataFrame, np.ndarray, List[Union[str, pd.DataFrame, np.ndarray]]]] = None
                The edge features to normalize.
            allow_automatic_feature: bool = True
                Whether to allow feature names creation based on the
                provided feature name, using the default settings,
                or based on a provided abstract embedding model that
                will be called on the provided graph.
            skip_evaluation_biased_feature: bool = False
                Whether to skip feature names that are known to be biased
                when running an holdout. These features should be computed
                exclusively on the training graph and not the entire graph.
            smoke_test: bool = False
                Whether this run should be considered a smoke test
                and therefore use the smoke test configurations for
                the provided model names and feature names.
            precompute_constant_automatic_stocastic_features: bool = False
                Whether to precompute once the constant automatic stocastic
                features before starting the embedding loop. This means that,
                when left set to false, while the features will be computed
                using the same input data, the random state between runs will
                be different and therefore the experiment performance will
                capture more of the variance derived from the stocastic aspect
                of the considered method. When set to true, they are only computed
                once and therefore the experiment will be overall faster.
            """
    
    
    
    def normalize_node_feature(cls: None, graph: Graph, random_state: int, node_feature: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]], allow_automatic_feature: bool, skip_evaluation_biased_feature: bool, smoke_test: bool, precompute_constant_automatic_stocastic_features: bool) -> List:
        """Normalizes the provided node features and validates them.
    
            Parameters
            ------------------
            graph: Graph
                The graph to check for.
            random_state: int
                The random state to use for the stochastic automatic features.
            node_feature: Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]],
                The node feature to normalize.
            allow_automatic_feature: bool = True
                Whether to allow feature names creation based on the
                provided feature name, using the default settings,
                or based on a provided abstract embedding model that
                will be called on the provided graph.
            skip_evaluation_biased_feature: bool = False
                Whether to skip feature names that are known to be biased
                when running an holdout. These features should be computed
                exclusively on the training graph and not the entire graph.
            smoke_test: bool = False
                Whether this run should be considered a smoke test
                and therefore use the smoke test configurations for
                the provided model names and feature names.
            precompute_constant_automatic_stocastic_features: bool = False
                Whether to precompute once the constant automatic stocastic
                features before starting the embedding loop. This means that,
                when left set to false, while the features will be computed
                using the same input data, the random state between runs will
                be different and therefore the experiment performance will
                capture more of the variance derived from the stocastic aspect
                of the considered method. When set to true, they are only computed
                once and therefore the experiment will be overall faster.
            """
    
    
    
    def normalize_node_features(cls: None, graph: Graph, random_state: int, node_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]]], None], allow_automatic_feature: bool, skip_evaluation_biased_feature: bool, smoke_test: bool, precompute_constant_automatic_stocastic_features: bool) -> List:
        """Normalizes the provided node features and validates them.
    
            Parameters
            ------------------
            graph: Graph
                The graph to check for.
            random_state: int
                The random state to use for the stochastic automatic features.
            node_features: Optional[Union[str, pd.DataFrame, np.ndarray, List[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]]]]] = None
                The node features to normalize.
            allow_automatic_feature: bool = True
                Whether to allow feature names creation based on the
                provided feature name, using the default settings,
                or based on a provided abstract embedding model that
                will be called on the provided graph.
            skip_evaluation_biased_feature: bool = False
                Whether to skip feature names that are known to be biased
                when running an holdout. These features should be computed
                exclusively on the training graph and not the entire graph.
            smoke_test: bool = False
                Whether this run should be considered a smoke test
                and therefore use the smoke test configurations for
                the provided model names and feature names.
            precompute_constant_automatic_stocastic_features: bool = False
                Whether to precompute once the constant automatic stocastic
                features before starting the embedding loop. This means that,
                when left set to false, while the features will be computed
                using the same input data, the random state between runs will
                be different and therefore the experiment performance will
                capture more of the variance derived from the stocastic aspect
                of the considered method. When set to true, they are only computed
                once and therefore the experiment will be overall faster.
            """
    
    
    
    def normalize_node_type_feature(cls: None, graph: Graph, random_state: int, node_type_feature: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]], allow_automatic_feature: bool, skip_evaluation_biased_feature: bool, smoke_test: bool, precompute_constant_automatic_stocastic_features: bool) -> List:
        """Normalizes the provided node type features and validates them.
    
            Parameters
            ------------------
            graph: Graph
                The graph to check for.
            random_state: int
                The random state to use for the stochastic automatic features.
            node_type_feature: Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]],
                The node type feature to normalize.
            allow_automatic_feature: bool = True
                Whether to allow feature names creation based on the
                provided feature name, using the default settings,
                or based on a provided abstract embedding model that
                will be called on the provided graph.
            skip_evaluation_biased_feature: bool = False
                Whether to skip feature names that are known to be biased
                when running an holdout. These features should be computed
                exclusively on the training graph and not the entire graph.
            smoke_test: bool = False
                Whether this run should be considered a smoke test
                and therefore use the smoke test configurations for
                the provided model names and feature names.
            precompute_constant_automatic_stocastic_features: bool = False
                Whether to precompute once the constant automatic stocastic
                features before starting the embedding loop. This means that,
                when left set to false, while the features will be computed
                using the same input data, the random state between runs will
                be different and therefore the experiment performance will
                capture more of the variance derived from the stocastic aspect
                of the considered method. When set to true, they are only computed
                once and therefore the experiment will be overall faster.
            """
    
    
    
    def normalize_node_type_features(cls: None, graph: Graph, random_state: int, node_type_features: typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel], typing.List[typing.Union[str, pandas.core.frame.DataFrame, numpy.ndarray, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]]], None], allow_automatic_feature: bool, skip_evaluation_biased_feature: bool, smoke_test: bool, precompute_constant_automatic_stocastic_features: bool) -> List:
        """Normalizes the provided node type features and validates them.
    
            Parameters
            ------------------
            graph: Graph
                The graph to check for.
            random_state: int
                The random state to use for the stochastic automatic features.
            node_type_features: Optional[Union[str, pd.DataFrame, np.ndarray, List[Union[str, pd.DataFrame, np.ndarray, Type[AbstractEmbeddingModel]]]]] = None
                The node features to normalize.
            allow_automatic_feature: bool = True
                Whether to allow feature names creation based on the
                provided feature name, using the default settings,
                or based on a provided abstract embedding model that
                will be called on the provided graph.
            skip_evaluation_biased_feature: bool = False
                Whether to skip feature names that are known to be biased
                when running an holdout. These features should be computed
                exclusively on the training graph and not the entire graph.
            smoke_test: bool = False
                Whether this run should be considered a smoke test
                and therefore use the smoke test configurations for
                the provided model names and feature names.
            precompute_constant_automatic_stocastic_features: bool = False
                Whether to precompute once the constant automatic stocastic
                features before starting the embedding loop. This means that,
                when left set to false, while the features will be computed
                using the same input data, the random state between runs will
                be different and therefore the experiment performance will
                capture more of the variance derived from the stocastic aspect
                of the considered method. When set to true, they are only computed
                once and therefore the experiment will be overall faster.
            """
    
    
    
    def requires_edge_types(cls: None) -> bool:
        """Returns whether the model requires edge types."""
    
    
    
    def requires_edge_weights(cls: None) -> bool:
        """TODO!: document this"""
    
    
    
    def requires_node_types(cls: None) -> bool:
        """TODO!: document this"""
    
    
    
    def requires_positive_edge_weights(cls: None) -> bool:
        """TODO!: document this"""
    
    
    
    def smoke_test_parameters(cls: None) -> Dict:
        """Returns parameters for smoke test."""
    
    
    
    def split_graph_following_evaluation_schema(cls: None, graph: Graph, evaluation_schema: str, random_state: int, holdout_number: int, number_of_holdouts: int) -> Tuple:
        """Return train and test graphs tuple following the provided evaluation schema.
    
            Parameters
            ----------------------
            graph: Graph
                The graph to split.
            evaluation_schema: str
                The evaluation schema to follow.
            random_state: int
                The random state for the evaluation
            holdout_number: int
                The current holdout number.
            number_of_holdouts: int
                The total number of holdouts.
            holdouts_kwargs: Dict[str, Any]
                The kwargs to be forwarded to the holdout method.
            """
    
    
    
    def task_involves_edge_types(cls: None) -> bool:
        """Returns whether the model task involves edge types."""
    
    
    
    def task_involves_edge_weights(cls: None) -> bool:
        """Returns whether the model task involves edge weights."""
    
    
    
    def task_involves_node_types(cls: None) -> bool:
        """Returns whether the model task involves node types."""
    
    
    
    def task_involves_topology(cls: None) -> bool:
        """Returns whether the model task involves topology."""
    
    
    
    def task_name(cls: None) -> str:
        """Returns name of the task this model is used for."""
    
    