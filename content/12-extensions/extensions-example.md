# Example Extension

Let's rewrite our Mandelbrot generator using Numba to see how it differs.

## NumPy array syntax

Here's an example of a python implementation using NumPy array operations:


```{literalinclude} ../../examples/extensions/python/mandel.py
:language: python
```

We can test this as:

```{literalinclude} ../../examples/extensions/python/test_mandel.py
:language: python
```

## Python with explicit loops

Here's a version where the loops are explicitly written out in python:

```{literalinclude} ../../examples/extensions/python-slow/mandel.py
:language: python
```

This can be run in the same way.


## Numba version

To get a Numba optimized version of the python with explicit loops we just add:

```python
from numba import njit
```

and then right before the function definition:

```python
@njit()
```

Here's the full code:

```{literalinclude} ../../examples/extensions/numba/mandel.py
:language: python
```

Again, this uses the same driver.


```{note}
We didn't need to do anything special to *compile* the numba code.
This is done for us when we first encounter it.
```

## Fortran implementation

If we want to write the code in Fortran, we need to [compile it into a shared
object library](https://numpy.org/doc/stable/f2py/usage.html) that python can import.  

Support for this is in transition at the moment.  The old official way to do this
was to use `distutils`, but this is removed in python 3.12.  

Instead, we will use the [meson build system](https://mesonbuild.com/).  This requires
use to install `meson` and `ninja`:

.. prompt:: bash

   pip install meson ninja
   
Here's our Fortran implementation for the Mandelbrot generator:

```{literalinclude} ../../examples/extensions/f2py/mandel.f90
:language: fortran
```



