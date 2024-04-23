# Example Extension

Let's rewrite our Mandelbrot generator using different languages
to see how the performance differs.

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

We can install Numba simply by doing:

```bash
pip install numba
```

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

```{tip}
We run it twice in our driver, since the first call will have the overhead
of the jit compilation.  
```

```{literalinclude} ../../examples/extensions/numba/test_mandel.py
:language: python
```


## Fortran implementation

If we want to write the code in Fortran, we need to [compile it into a shared
object library](https://numpy.org/doc/stable/f2py/usage.html) that python can import.  
This is where `f2py` comes in---it is part of the numpy project, so you probably
already have it installed.

Support for this is in transition at the moment.  The old official way to do this
was to use `distutils`, but this is removed in python 3.12.  

Instead, we will use the [meson build system](https://mesonbuild.com/).  This requires
use to install `meson` and `ninja`:

```bash
pip install meson ninja
```

Here's our Fortran implementation for the Mandelbrot generator:

```{literalinclude} ../../examples/extensions/f2py/mandel.f90
:language: fortran
```

To build the extension, we can do:

```bash
f2py -c mandel.f90 -m mandel_f2py
```

This will create a library (on my machine, it is called `mandel_f2py.cpython-312-x86_64-linux-gnu.so`)
which we can import as `import mandel_f2py`.

Here's a driver:

```{literalinclude} ../../examples/extensions/f2py/test_mandel.py
:language: python
```

```{note}
   Even though our Fortran subroutine takes the array `m` as an
   argument, since it is marked as `intent(out)`, the python module
   will use this as the return value.
```

## C++ / pybind11 implementation

pybind11 allows you to construct a numpy-compatible array in C++
and return it.  There are different constructors for this---here
we use on that allows us to specify the shape and stride.

We can install pybind11 via pip:

```bash
pip install pybind11
```

Here's the implementation of our Mandelbrot generator:


```{literalinclude} ../../examples/extensions/pybind11/mandel.cpp
:language: c++
```

We build the shared library as:

```bash
g++ -O3  -Wall -Wextra -shared -std=c++17 -fPIC $(python3 -m pybind11 --includes) mandel.cpp -o mandel$(python3-config --extension-suffix)
```

Our driver is essentially the same as the Fortran one.


```{literalinclude} ../../examples/extensions/pybind11/test_mandel.py
:language: python
```


## Timings

On my machine, here are some timings:


|   technique                |   timings (s)  |
| -------------------------- | -------------- |
| python w/ explicit loops   |     72.4
| python / numpy             |      0.268
| Numba(*)                   |      0.0943
| C++ + pybind11             |      0.105
| Fortran + f2py             |      0.0878


(*) timing for the second invocation, which excludes JIT overhead.
