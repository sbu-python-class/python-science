# Deriving the Learning Correction

For gradient descent, we need to derive the update to the matrix
${\bf A}$ based on training on a set of our data, $({\bf x}^k, {\bf y}^k)$.

Let's start with our cost function:

$$f(A_{ij}) = \sum_{i=1}^{N_\mathrm{out}} (z_i - y_i^k)^2 = \sum_{i=1}^{N_\mathrm{out}} 
  \Biggl [ g\biggl (\underbrace{\sum_{j=1}^{N_\mathrm{in}} A_{ij} x^k_j}_{\equiv \alpha_i} \biggr ) - y^k_i \Biggr ]^2$$

where we'll refer to the product ${\boldsymbol \alpha} \equiv {\bf Ax}$ to help simplify notation.

We can compute the derivative with respect to a single matrix
element, $A_{pq}$ by applying the chain rule:

$$\frac{\partial f}{\partial A_{pq}} =
  2 \sum_{i=1}^{N_\mathrm{out}} (z_i - y^k_i) \left . \frac{\partial g}{\partial \xi} \right |_{\xi=\alpha_i} \frac{\partial \alpha_i}{\partial A_{pq}}$$
  

with

$$\frac{\partial \alpha_i}{\partial A_{pq}} = \sum_{j=1}^{N_\mathrm{in}} \frac{\partial A_{ij}}{\partial A_{pq}} x^k_j = \sum_{j=1}^{N_\mathrm{in}} \delta_{ip} \delta_{jq} x^k_j = \delta_{ip} x^k_q$$

and for $g(\xi)$, we will assume the sigmoid function,so

$$\frac{\partial g}{\partial \xi} 
  = \frac{\partial}{\partial \xi} \frac{1}{1 + e^{-\xi}} 
  =- (1 + e^{-\xi})^{-2} (- e^{-\xi})
  = g(\xi) \frac{e^{-\xi}}{1+ e^{-\xi}} = g(\xi) (1 - g(\xi))$$

which gives us:

\begin{align*}
\frac{\partial f}{\partial A_{pq}} &= 2 \sum_{i=1}^{N_\mathrm{out}}
   (z_i - y^k_i) z_i (1 - z_i) \delta_{ip} x^k_q \\
   &= 2 (z_p - y^k_p) z_p (1- z_p) x^k_q
\end{align*}
   
where we used the fact that the $\delta_{ip}$ means that only a single term contributes to the sum.

Note that:

* $e_p^k \equiv (z_p - y_p^k)$ is the error on the output layer,
  and the correction is proportional to the error (as we would
  expect).

* The $k$ superscripts here remind us that this is the result of
  only a single pair of data from the training set.
  
Now ${\bf z}$ and ${\bf y}^k$ are all vectors of size $N_\mathrm{out} \times 1$ and ${\bf x}^k$ is a vector of size $N_\mathrm{in} \times 1$, so we can write this expression for the matrix as a whole as:

$$\frac{\partial f}{\partial {\bf A}} = 2 ({\bf z} - {\bf y}^k) \circ {\bf z} \circ (1 - {\bf z}) \cdot ({\bf x}^k)^\intercal$$

where the operator $\circ$ represents _element-by-element_ multiplication (the [Hadamard product](https://en.wikipedia.org/wiki/Hadamard_product_(matrices))).

## Performing the update

We could do the update like we just saw with our gradient descent
example: take a single data point, $({\bf x}^k, {\bf y}^k)$ and
do the full minimization, continually estimating the correction,
$\partial f/\partial {\bf A}$ and updating ${\bf A}$ until we
reach a minimum.  The problem with this is that $({\bf x}^k, {\bf y}^k)$ is only one point in our training data, and there is no
guarantee that if we minimize completely with point $k$ that we will
also be a minimum with point $k+1$.

Instead we take multiple passes through the training data (called _epochs_) and apply only a single push in the direction that gradient
descent suggests, scaled by a _learning rate_ $\eta$.

The overall minimization appears as:

<div style="border: solid; padding: 10px; width: 80%; margin: 0 auto; background: #eeeeee">
* Loop over epochs

  * Loop over the training data, $\{ ({\bf x}^0, {\bf y}^0), ({\bf x}^1, {\bf y}^1), \ldots \}$.  We'll refer to the current training
    pair as $({\bf x}^k, {\bf y}^k)$
    
    * Propagate ${\bf x}^k$ through the network, getting the output
      ${\bf z} = g({\bf A x}^k)$
      
    * Compute the error on the output layer, ${\bf e}^k = {\bf z} - {\bf y}^k$
    
    * Update the matrix ${\bf A}$ according to:
    
      $${\bf A} \leftarrow {\bf A} - 2 \,\eta\, {\bf e}^k \circ {\bf z} \circ (1 - {\bf z}) \cdot ({\bf x}^k)^\intercal$$
</div>

