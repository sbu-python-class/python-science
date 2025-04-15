# Diving Deeper into Machine Learning

We've focused on neural networks, using labeled data that we
can use to learn the trends in our data.  This is an example
of _supervised learning_.  

Broadly speaking there are
3 main [approaches to machine learning](https://en.wikipedia.org/wiki/Machine_learning#Approaches)

* [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning) 

  This uses labeled pairs (input and output) to train the model
  to learn how to predict the outputs from the inputs.

* [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning)

  No labeled data is provided.  Instead the machine learning
  algorithm seeks to find the structure on its own.  The goal
  is to learn patterns and features to be able to produce
  new data.
  
* [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)

  As with unsupervised learning, no labeled data is used,
  but the model is "rewarded"  when it does something right,
  and the model tries to maximize rewards (think: self-driving
  cars).
  
## Libraries

There are a number of popular libraries that implement machine learning algorithms.
Their features and performance vary quite a bit.  An comparison of their
features is provided by Wikipedia: [Comparison of deep learning software](https://en.wikipedia.org/wiki/Comparison_of_deep_learning_software).

Some additional comparisons are provided here: https://ritza.co/articles/scikit-learn-vs-tensorflow-vs-pytorch-vs-keras/

* [TensorFlow](https://www.tensorflow.org/)

  This is an open source machine learning library released by Google.  It has support
  for CPUs, GPUs, and [TPUs](https://en.wikipedia.org/wiki/Tensor_Processing_Unit),
  and provides all the features you need to build deep learning workflows:
  [TensorFlow feactures](https://en.wikipedia.org/wiki/TensorFlow#Features).
  
* [PyTorch](https://pytorch.org/)

  This is a machine learning library build off of the Torch library, originally
  developed by Facebook.
  
* [scikit-learn](https://scikit-learn.org/stable/)

  This is a python library developed for machine learning.  It has a lot of
  sample datasets that provide a nice means to learn how different methods work.
  It is designed to work with NumPy and SciPy.
  
  General recommendations on the web seem to be to use Scikit-learn to get
  started with machine learning and to explore ideas, but to switch to
  one of the other packages for computationally-intensive work.
  
  Scikit-learn provides some nice sample datasets: 

  https://scikit-learn.org/stable/datasets/toy_dataset.html
  
  as well as generators for
  datasets:
  
  https://scikit-learn.org/stable/datasets/sample_generators.html
  
There are also tools that provide higher-level interfaces to these

* [Keras](https://keras.io/)

  Keras is built on top of TensorFlow and provides a nice python interface that
  hides a lot of the implementation details in TensorFlow.

## Keras / TensorFlow

We'll focus on Keras and TensorFlow.

There are a large number of examples provided by Keras:

https://keras.io/examples/

You should be able to install keras via pip or conda.