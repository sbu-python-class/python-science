# Hidden Layers


 We can get better performance from a neural network by adding a hidden layer:

![hidden layers](nn_fig_hidden.png)

The size of the hidden layer is independent of the size of the input and output
layers.  In this case, we have a hidden layer that is larger
than either the input or output layers.

Now we have an additional matrix ${\bf B}$ to train.  The matrix sizes are:

* ${\bf A}$ : $N_\mathrm{out} \times N_\mathrm{hidden}$
* ${\bf B}$ : $N_\mathrm{hidden} \times N_\mathrm{in}$


```{note}
Neglecting the activation functions, the action of the network
is to do ${\bf z} = {\bf A B x}$ which has size $N_\mathrm{out}$.
```

The derivation of the corrections to matrices ${\bf A}$ and ${\bf B}$ can be done
via the chain rule.

```{note}
We'll consider the case of a single hidden layer, but the derivation we
do here generalizes to multiple hidden layers.
```

\begin{equation}
f(A_{lm}, B_{ij}) = \sum_{l=1}^{N_\mathrm{out}} (z_l - y^k_l)^2
\end{equation}                  

$$\tilde{z}_i = g \biggl ( \underbrace{\sum_{j=1}^{N_\mathrm{in}} B_{ij} x^k_j}_{\equiv \beta_i} \biggr )$$

$$z_l = g \biggl ( \underbrace{\sum_{m=1}^{N_\mathrm{hidden}} A_{lm} \tilde{z}_m}_{\equiv \alpha_l} \biggr )$$

Note that we are assuming here that the same activation function, $g(\xi)$
is used on each layer.

## Updates to ${\bf A}$

Matrix ${\bf A}$ is trained based on the output layer, we know the error there
directly, ${\bf e}^k = {\bf z} - {\bf y}^k$.  As a result, we can just use
the result that we got for a single layer, but now the input is $\tilde{\bf z}$
instead of ${\bf x}$:

$$\frac{\partial f}{\partial {\bf A}} = 2 {\bf e}^k \circ {\bf z} \circ (1 - {\bf z}) \cdot \tilde{\bf z}^\intercal$$

## Updates to ${\bf B}$

To find the corrections to matrix ${\bf B}$, we essentially need to know what the
error is on the hidden layer.  But we only know the error on the output layer, so
by applying the chainrule on our cost function, we will work out this correction,
and in the process see how the error on the output layer informs the error on the
hidden layer&mdash;a process called _backpropagation_.

Let's start with our cost function:

\begin{align*}
f(A_{lm}, B_{ij}) &= \sum_{l=1}^{N_\mathrm{out}} (z_l - y^k_l)^2 \\
                  &= \sum_{l=1}^{N_\mathrm{out}} \Biggl [ g \biggl ( \sum_{m=1}^{N_\mathrm{hidden}} A_{lm} \tilde{z}_m \biggr ) - y_l^k \Biggr ]^2 \\
                  &= \sum_{l=1}^{N_\mathrm{out}} \Biggl [ g \biggl ( \sum_{m=1}^{N_\mathrm{hidden}} A_{lm} \,g \biggl ( \sum_{j=1}^{N_\mathrm{in}} B_{mj} x_j^k \biggr ) \biggr ) - y_l^k \Biggr ]^2
\end{align*}                  

Differentiating with respect to an element in matrix ${\bf B}$, we apply the chain rule over and over,
giving:

$$\frac{\partial f}{\partial B_{pq}} = 2 \sum_{l=1}^{N_\mathrm{out}} (z_l - y_l^k)
    \left .\frac{\partial g}{\partial \xi} \right |_{\xi = \alpha_l}
    \sum_{m=1}^{N_\mathrm{hidden}} A_{lm}\, \left . \frac{\partial g}{\partial \xi} \right |_{\xi = \beta_m}
    \sum_{j=1}^{N_\mathrm{in}} \frac{\partial B_{mj}}{\partial B_{pq}} x_j^k $$
    
     
Now we have 3 derivatives left, which are straightforward:

$$\left .\frac{\partial g}{\partial \xi} \right |_{\xi = \alpha_l} = g(\alpha_l)\left [ 1 - g(\alpha_l)\right ]
   = z_l (1 - z_l)$$

$$\left .\frac{\partial g}{\partial \xi} \right |_{\xi = \beta_m} = g(\beta_m)\left [ 1 - g(\beta_m)\right ]
   = \tilde{z}_m (1 - \tilde{z}_m)$$

$$\frac{\partial B_{mj}}{\partial B_{pq}} = \delta_{mp} \delta_{jq}$$

Inserting these dervatives and using the $\delta$'s, we are left with:

$$\frac{\partial f}{\partial B_{pq}} = 2 \sum_{l=1}^{N_\mathrm{out}}
   \underbrace{(z_l - y_l^k)}_{ = e_l^k} z_l (1 - z_l) A_{lp} \tilde{z}_p (1 - \tilde{z}_p) x^k_q$$
   
Now, that remaining sum is contracting on the first of the indices of
the matrix ${\bf A}$, indicating a matrix vector product involving
${\bf A}^\intercal$.  This allows us to define the error _backpropagated_ to the hidden layer:

$$\tilde{e}_p^k = \sum_{l=1}^{N_\mathrm{out}} e_l^k z_l (1 - z_l) A_{lp} 
   = \left [ {\bf A}^\intercal  \cdot ({\bf e}^k \circ {\bf z} \circ (1 - {\bf z})) \right ]_p$$

and we can write

$$\frac{\partial f}{\partial {\bf B}} = 2 \tilde{\bf e}^k \circ \tilde{\bf z} \circ (1 - \tilde{\bf z}) \cdot ({\bf x}^k)^\intercal$$


Notice the symmetry in the update of each matrix:

\begin{align*}
\frac{\partial f}{\partial {\bf A}} &= 2 {\bf e}^k \circ {\bf z} \circ (1 - {\bf z}) \cdot \tilde{\bf z}^\intercal \\
\frac{\partial f}{\partial {\bf B}} &= 2 \tilde{\bf e}^k \circ \tilde{\bf z} \circ (1 - \tilde{\bf z}) \cdot ({\bf x}^k)^\intercal
\end{align*}

Adding additional hidden layers would continue the trend, with each hidden layer's matrix update depending
on the error backpropagated to that layer.
