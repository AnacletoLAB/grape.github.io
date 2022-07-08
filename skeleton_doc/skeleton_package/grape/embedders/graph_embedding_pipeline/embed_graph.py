import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph
import embiggen

def embed_graph(graph: typing.Union[Graph, str], embedding_model: typing.Union[str, typing.Type[embiggen.utils.abstract_models.abstract_embedding_model.AbstractEmbeddingModel]], repository: typing.Optional[str], version: typing.Optional[str], library_name: typing.Optional[str], smoke_test: bool, return_dataframe: bool, verbose: bool) -> embiggen.EmbeddingResult:
    """Return embedding of the provided graph.

    Parameters
    ---------------------
    graph: Union[Graph, str]
        The graph or graph name to embed.
        If a graph name is provided, it will be retrieved from Ensmallen's automatic retrieval.
    embedding_model: Union[str, Type[AbstractEmbeddingModel]]
        Model or model name to use.
        If a model name is provided, it will be retrieved from the models' library.
    repository: Optional[str] = None
        Repository from where to retrieve the provided graph names
        from the Ensmallen automatic retrieval.
    version: Optional[str] = None
        Graph version to retrieve.
    library_name: Optional[str] = None
        The library from where to retrieve the embedding model.
    enable_cache: bool = False
        Whether to enable the cache.
    smoke_test: bool = False
        Whether this run should be considered a smoke test
        and therefore use the smoke test configurations for
        the provided model names and feature names.
    cache_directory: str = "embedding"
        Path where to store the cache if it is enabled.
    return_dataframe: bool = True
        Whether to return a pandas DataFrame with the embedding.
    verbose: bool
        Whether to show loading bars.
    **kwargs: Dict
        Kwargs to forward to the embedding model creation.
        If a model name was NOT provided, an exception will
        be raised as it is unclear how to behave.
    """
