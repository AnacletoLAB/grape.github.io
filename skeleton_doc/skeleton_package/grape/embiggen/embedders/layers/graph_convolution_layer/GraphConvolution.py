import typing
from typing import *
from tensorflow import Tensor, SparseTensor
from ensmallen import Graph

class GraphConvolution:
    """Layer implementing graph convolution layer."""
    
    @property
    def activity_regularizer(self):
        """Optional regularizer function for the output of this layer."""
    
    
    
    @property
    def compute_dtype(self):
        """The dtype of the layer's computations.
    
        This is equivalent to `Layer.dtype_policy.compute_dtype`. Unless
        mixed precision is used, this is the same as `Layer.dtype`, the dtype of
        the weights.
    
        Layers automatically cast their inputs to the compute dtype, which causes
        computations and the output to be in the compute dtype as well. This is done
        by the base Layer class in `Layer.__call__`, so you do not have to insert
        these casts if implementing your own layer.
    
        Layers often perform certain internal computations in higher precision when
        `compute_dtype` is float16 or bfloat16 for numeric stability. The output
        will still typically be float16 or bfloat16 in such cases.
    
        Returns:
          The layer's compute dtype.
        """
    
    
    
    @property
    def dtype(self):
        """The dtype of the layer weights.
    
        This is equivalent to `Layer.dtype_policy.variable_dtype`. Unless
        mixed precision is used, this is the same as `Layer.compute_dtype`, the
        dtype of the layer's computations.
        """
    
    
    
    @property
    def dtype_policy(self):
        """The dtype policy associated with this layer.
    
        This is an instance of a `tf.keras.mixed_precision.Policy`.
        """
    
    
    
    @property
    def dynamic(self):
        """Whether the layer is dynamic (eager-only); set in the constructor."""
    
    
    
    @property
    def inbound_nodes(self):
        """Deprecated, do NOT use! Only for compatibility with external Keras."""
    
    
    
    @property
    def input(self):
        """Retrieves the input tensor(s) of a layer.
    
        Only applicable if the layer has exactly one input,
        i.e. if it is connected to one incoming layer.
    
        Returns:
            Input tensor or list of input tensors.
    
        Raises:
          RuntimeError: If called in Eager mode.
          AttributeError: If no inbound nodes are found.
        """
    
    
    
    @property
    def input_mask(self):
        """Retrieves the input mask tensor(s) of a layer.
    
        Only applicable if the layer has exactly one inbound node,
        i.e. if it is connected to one incoming layer.
    
        Returns:
            Input mask tensor (potentially None) or list of input
            mask tensors.
    
        Raises:
            AttributeError: if the layer is connected to
            more than one incoming layers.
        """
    
    
    
    @property
    def input_shape(self):
        """Retrieves the input shape(s) of a layer.
    
        Only applicable if the layer has exactly one input,
        i.e. if it is connected to one incoming layer, or if all inputs
        have the same shape.
    
        Returns:
            Input shape, as an integer shape tuple
            (or list of shape tuples, one tuple per input tensor).
    
        Raises:
            AttributeError: if the layer has no defined input_shape.
            RuntimeError: if called in Eager mode.
        """
    
    
    
    @property
    def input_spec(self):
        """`InputSpec` instance(s) describing the input format for this layer.
    
        When you create a layer subclass, you can set `self.input_spec` to enable
        the layer to run input compatibility checks when it is called.
        Consider a `Conv2D` layer: it can only be called on a single input tensor
        of rank 4. As such, you can set, in `__init__()`:
    
        ```python
        self.input_spec = tf.keras.layers.InputSpec(ndim=4)
        ```
    
        Now, if you try to call the layer on an input that isn't rank 4
        (for instance, an input of shape `(2,)`, it will raise a nicely-formatted
        error:
    
        ```
        ValueError: Input 0 of layer conv2d is incompatible with the layer:
        expected ndim=4, found ndim=1. Full shape received: [2]
        ```
    
        Input checks that can be specified via `input_spec` include:
        - Structure (e.g. a single input, a list of 2 inputs, etc)
        - Shape
        - Rank (ndim)
        - Dtype
    
        For more information, see `tf.keras.layers.InputSpec`.
    
        Returns:
          A `tf.keras.layers.InputSpec` instance, or nested structure thereof.
        """
    
    
    
    @property
    def losses(self):
        """List of losses added using the `add_loss()` API.
    
        Variable regularization tensors are created when this property is accessed,
        so it is eager safe: accessing `losses` under a `tf.GradientTape` will
        propagate gradients back to the corresponding variables.
    
        Examples:
    
        >>> class MyLayer(tf.keras.layers.Layer):
        ...   def call(self, inputs):
        ...     self.add_loss(tf.abs(tf.reduce_mean(inputs)))
        ...     return inputs
        >>> l = MyLayer()
        >>> l(np.ones((10, 1)))
        >>> l.losses
        [1.0]
    
        >>> inputs = tf.keras.Input(shape=(10,))
        >>> x = tf.keras.layers.Dense(10)(inputs)
        >>> outputs = tf.keras.layers.Dense(1)(x)
        >>> model = tf.keras.Model(inputs, outputs)
        >>> # Activity regularization.
        >>> len(model.losses)
        0
        >>> model.add_loss(tf.abs(tf.reduce_mean(x)))
        >>> len(model.losses)
        1
    
        >>> inputs = tf.keras.Input(shape=(10,))
        >>> d = tf.keras.layers.Dense(10, kernel_initializer='ones')
        >>> x = d(inputs)
        >>> outputs = tf.keras.layers.Dense(1)(x)
        >>> model = tf.keras.Model(inputs, outputs)
        >>> # Weight regularization.
        >>> model.add_loss(lambda: tf.reduce_mean(d.kernel))
        >>> model.losses
        [<tf.Tensor: shape=(), dtype=float32, numpy=1.0>]
    
        Returns:
          A list of tensors.
        """
    
    
    
    @property
    def metrics(self):
        """List of metrics added using the `add_metric()` API.
    
        Example:
    
        >>> input = tf.keras.layers.Input(shape=(3,))
        >>> d = tf.keras.layers.Dense(2)
        >>> output = d(input)
        >>> d.add_metric(tf.reduce_max(output), name='max')
        >>> d.add_metric(tf.reduce_min(output), name='min')
        >>> [m.name for m in d.metrics]
        ['max', 'min']
    
        Returns:
          A list of `Metric` objects.
        """
    
    
    
    @property
    def name(self):
        """Name of the layer (string), set in the constructor."""
    
    
    
    @property
    def name_scope(self):
        """Returns a `tf.name_scope` instance for this class."""
    
    
    
    @property
    def non_trainable_variables(self):
        """TODO!: document this"""
    
    
    
    @property
    def non_trainable_weights(self):
        """List of all non-trainable weights tracked by this layer.
    
        Non-trainable weights are *not* updated during training. They are expected
        to be updated manually in `call()`.
    
        Note: This will not track the weights of nested `tf.Modules` that are not
        themselves Keras layers.
    
        Returns:
          A list of non-trainable variables.
        """
    
    
    
    @property
    def outbound_nodes(self):
        """Deprecated, do NOT use! Only for compatibility with external Keras."""
    
    
    
    @property
    def output(self):
        """Retrieves the output tensor(s) of a layer.
    
        Only applicable if the layer has exactly one output,
        i.e. if it is connected to one incoming layer.
    
        Returns:
          Output tensor or list of output tensors.
    
        Raises:
          AttributeError: if the layer is connected to more than one incoming
            layers.
          RuntimeError: if called in Eager mode.
        """
    
    
    
    @property
    def output_mask(self):
        """Retrieves the output mask tensor(s) of a layer.
    
        Only applicable if the layer has exactly one inbound node,
        i.e. if it is connected to one incoming layer.
    
        Returns:
            Output mask tensor (potentially None) or list of output
            mask tensors.
    
        Raises:
            AttributeError: if the layer is connected to
            more than one incoming layers.
        """
    
    
    
    @property
    def output_shape(self):
        """Retrieves the output shape(s) of a layer.
    
        Only applicable if the layer has one output,
        or if all outputs have the same shape.
    
        Returns:
            Output shape, as an integer shape tuple
            (or list of shape tuples, one tuple per output tensor).
    
        Raises:
            AttributeError: if the layer has no defined output shape.
            RuntimeError: if called in Eager mode.
        """
    
    
    
    @property
    def stateful(self):
        """TODO!: document this"""
    
    
    
    @property
    def submodules(self):
        """Sequence of all sub-modules.
    
        Submodules are modules which are properties of this module, or found as
        properties of modules which are properties of this module (and so on).
    
        >>> a = tf.Module()
        >>> b = tf.Module()
        >>> c = tf.Module()
        >>> a.b = b
        >>> b.c = c
        >>> list(a.submodules) == [b, c]
        True
        >>> list(b.submodules) == [c]
        True
        >>> list(c.submodules) == []
        True
    
        Returns:
          A sequence of all submodules.
        """
    
    
    
    @property
    def supports_masking(self):
        """Whether this layer supports computing a mask using `compute_mask`."""
    
    
    
    @property
    def trainable(self):
        """TODO!: document this"""
    
    
    
    @property
    def trainable_variables(self):
        """TODO!: document this"""
    
    
    
    @property
    def trainable_weights(self):
        """List of all trainable weights tracked by this layer.
    
        Trainable weights are updated via gradient descent during training.
    
        Note: This will not track the weights of nested `tf.Modules` that are not
        themselves Keras layers.
    
        Returns:
          A list of trainable variables.
        """
    
    
    
    @property
    def updates(self):
        """TODO!: document this"""
    
    
    
    @property
    def variable_dtype(self):
        """Alias of `Layer.dtype`, the dtype of the weights."""
    
    
    
    @property
    def variables(self):
        """Returns the list of all layer variables/weights.
    
        Alias of `self.weights`.
    
        Note: This will not track the weights of nested `tf.Modules` that are not
        themselves Keras layers.
    
        Returns:
          A list of variables.
        """
    
    
    
    @property
    def weights(self):
        """Returns the list of all layer variables/weights.
    
        Note: This will not track the weights of nested `tf.Modules` that are not
        themselves Keras layers.
    
        Returns:
          A list of variables.
        """
    
    
    def from_config(cls: None, config: None):
        """Creates a layer from its config.
    
        This method is the reverse of `get_config`,
        capable of instantiating the same layer from the config
        dictionary. It does not handle layer connectivity
        (handled by Network), nor weights (handled by `set_weights`).
    
        Arguments:
            config: A Python dictionary, typically the
                output of get_config.
    
        Returns:
            A layer instance.
        """
    
    
    
    def with_name_scope(cls: None, method: None):
        """Decorator to automatically enter the module name scope.
    
        >>> class MyModule(tf.Module):
        ...   @tf.Module.with_name_scope
        ...   def __call__(self, x):
        ...     if not hasattr(self, 'w'):
        ...       self.w = tf.Variable(tf.random.normal([x.shape[1], 3]))
        ...     return tf.matmul(x, self.w)
    
        Using the above module would produce `tf.Variable`s and `tf.Tensor`s whose
        names included the module name:
    
        >>> mod = MyModule()
        >>> mod(tf.ones([1, 2]))
        <tf.Tensor: shape=(1, 3), dtype=float32, numpy=..., dtype=float32)>
        >>> mod.w
        <tf.Variable 'my_module/Variable:0' shape=(2, 3) dtype=float32,
        numpy=..., dtype=float32)>
    
        Args:
          method: The method to wrap.
    
        Returns:
          The original method wrapped such that it enters the module's name scope.
        """
    
    