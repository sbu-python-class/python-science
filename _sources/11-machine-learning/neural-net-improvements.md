# Improvements

There are many ways we could improve the performance of our network, but these will add
a lot of complexity to the simple class that we wrote.  Fortunately there are a lot of
machine learning libraries that provide these features, and work efficiently, so for
real applications we would want to use one of those libraries (we'll explore these next).

## Batching

Right now, we did our training as:

* Loop over the $T$ pairs $({\bf x}^k, {\bf y}^k)$ for $k = 1, \ldots, T$

  * Propagate $({\bf x}^k, {\bf y}^k)$ through the network
  * Compute the corrections $\partial f/\partial {\bf A}$, $\partial f/\partial {\bf B}$
  * Update the matrices:
  
    $${\bf A} \leftarrow {\bf A} + \eta \frac{\partial f}{\partial {\bf A}}$$

    $${\bf B} \leftarrow {\bf B} + \eta \frac{\partial f}{\partial {\bf B}}$$

In this manner, each training pair sees slightly different
matrices ${\bf A}$ and ${\bf B}$, as each previous pair
updates it immediately.

We could instead divide our training set into $N$ batches,
each with $\tau = T/N$ training pairs and do our update as:

* Loop over $N$ batches

  * Loop over the $\tau$ pairs $({\bf x}^k, {\bf y}^k)$ for $k = 1, \ldots, \tau$ in the current batch 

    * Propagate $({\bf x}^k, {\bf y}^k)$ through the network
    * Compute the corrections $\partial f/\partial {\bf A}^k$, $\partial f/\partial {\bf B}^k$ from the current pair
    
    * Accumulate the corrections:
  
      $$\frac{\partial f}{\partial {\bf A}} = \frac{\partial f}{\partial {\bf A}} + \frac{\partial f}{\partial {\bf A}^k}$$
      
      $$\frac{\partial f}{\partial {\bf B}} = \frac{\partial f}{\partial {\bf B}} + \frac{\partial f}{\partial {\bf B}^k}$$
      
  * Apply a single update to the matrices for this batch:

    $${\bf A} \leftarrow {\bf A} + \eta \frac{\partial f}{\partial {\bf A}}$$

    $${\bf B} \leftarrow {\bf B} + \eta \frac{\partial f}{\partial {\bf B}}$$

The advantage of this is that the $\tau$ trainings in a batch
can all be done in parallel now, spread across many CPU cores
or GPU cores.  This greatly accelerates the training time.
  

## Different activation or cost functions

We used a simple cost function: the sum of the square of the errors.  This is analogous to the $L_2$ norm we discussed previously.  But there are a lot of other cost functions
we could explore.  Changing the cost function will require
us to recompute our derivatives.

Likewise, there are a wide number of activation functions,
some of which are not differentiable.  The choice of activation
function can depend on what type of data you are using.  You
might also want to use a different activation function
on each layer.  Again, this would require us to redo
our derivatives.


## Use a different minimization technique

We only explored gradient descent.  But there are improvements
to this (like momentum that we mentioned previously) as well
as alternate minimization techniques we could use (some of 
which don't need the gradient at all).


## Different types of layers / connections

We only considered a dense network: every node on one
layer was connected to every node on the adjacent layer.
But there are alternatives.

For example, a [convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network) performs a convolution on a layer with some kernel.  This
helps identifying features.

## More hidden layers

There is no restriction on the number of hidden layers we
can use.  Each additional hidden layer means an additional
matrix is added to our network.  For our code, we'd simply need to backpropagate
the error to each hidden layer and compute the update to
the new matrix.

## Auto-differentiation libraries

At some point, with all of these options, doing all of the
differentiation / chain-rule by hand becomes burdensome and
prone to errors.  For this reason, libraries often use
automatic differentiation libraries, like [JAX](https://jax.readthedocs.io/en/latest/) which can take
the derivatives of our python functions themselves.