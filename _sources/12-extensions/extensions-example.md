# Example Extension

Let's rewrite our Mandelbrot generator using different languages
to see how the performance differs.

Recall the Mandelbrot set is defined as the set such that $z_{k+1} = z_k^2 + c$
remains bounded, defined as $|z_{k+1}| \le 2$, where $c$ is a complex number,
$c = x + iy$, in the complex plane, and $z_0 = 0$ is the starting condition.

We'll do a fixed number of iterations, and store the iteration for which $|z_{k+1}|$
first becomes larger than 2.



## NumPy array syntax

Here's an example of a python implementation using NumPy array operations:


```{literalinclude} ../../examples/extensions/python/mandel.py
:language: python
```

We can test this as:

```{literalinclude} ../../examples/extensions/python/test_mandel.py
:language: python
```

Here's the resulting image

```{image} test.png
:align: center
```

## Python with explicit loops

Here's a version where the loops are explicitly written out in python:

```{literalinclude} ../../examples/extensions/python-slow/mandel.py
:language: python
```

This can be run using the same driver as the numpy vectorized version.


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
of the JIT compilation.  
```

```{literalinclude} ../../examples/extensions/numba/test_mandel.py
:language: python
```

## Cython version

We can install Cython by doing

```bash
pip install Cython
```

For Cython, we mainly need to specify the datatypes of the different
variables.  We use the extension `.pyx` for a cython file.

Here's the full code:

```{literalinclude} ../../examples/extensions/cython/mandel.pyx
:language: python
```

To build it, we can use a `setup.py` file:

```{literalinclude} ../../examples/extensions/cython/setup.py
:language: python
```

and make the extension as:

```bash
python setup.py build_ext --inplace
```

```{note}
This build process will likely change in the near future, as
the community is transitioning away from `setup.py`, but the 
docs don't seem to be fully up to date on the new way to build.
```

````{tip}
To help understand where the slow parts of your Cython code are, you
can do
```
cythonize -a mandel.pyx
```
This will produce an HTML file with the parts of the code that interact
with python highlighted.  (Make sure there are no `.c` files hanging around).
These highlighted lines are places you should try to optimize.

For our example, if we do
```
np.abs(z[i,j])
```
instead of
```
abs(z[i,j])
```
we get a dramatic slowdown!

Thanks to Eric Johnson for pointing this out.

````


## Fortran implementation

If we want to write the code in Fortran, we need to [compile it into a shared
object library](https://numpy.org/doc/stable/f2py/usage.html) that python can import.  
This is where `f2py` comes in---it is part of the numpy project, so you probably
already have it installed.

```{note}
Support for this is in transition at the moment.  The old official way to do this
was to use `distutils`, but this is removed in python 3.12.  

Instead, we will use the [meson build system](https://mesonbuild.com/).
```

We need to install `meson` and `ninja`:

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

````{note}
If the `f2py` command-line tool is not available, you can try running it as a module instead:
```bash
python -m numpy.f2py -c mandel.f90 -m mandel_f2py
```
````

````{tip}
The build doesn't show you the compilation commands used to make the library.  But if you look
at the output, it will say something like:
```
The Meson build system
Version: 1.4.0
Source dir: /tmp/tmp0sbl86zt
Build dir: /tmp/tmp0sbl86zt/bbdir
Build type: native build
Project name: mandel_f2py
```
If you then look in the build directory, there will be a file `compile_commands.json` that
lists the commands that meson + f2py use to compile the extension.  In our case,
it is using the optimization flag `-O3`.
````

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

```{note}
The numpy array returned to python will have Fortran ordering (column-major) instead
of the usual row-major ordering (take a look at the ``.flags`` attributes).
```

## C++ / pybind11 implementation

pybind11 allows you to construct a numpy-compatible array in C++
and return it.  There are different constructors for this---here
we use on that allows us to specify the shape and stride.

We can install pybind11 via pip:

```bash
pip install pybind11
```

Inside of the `mandelbrot()` function, we need temporary
two-dimensional arrays to store $z$ and $c$.  With C++23
we could use `std::mdspan` to give us nice multidimensional
indexing.  For now, we need to do something different.
Our first attempt will use `std::vector<std::vector<std::complex<double>>>`.

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

A slightly more complicated version that creates a contiguous `Array` class
that can be indexed with `()` runs faster.  That code is here:

```{literalinclude} ../../examples/extensions/pybind11/contiguous/mandel.cpp
:language: C++
```

It uses the same driver.


## Timings

On my machine, (python 3.12, Cython 3.0.10, GCC 14, numba 0.59.1) here
are some timings (average of 3 runs):


|   technique                                  |   timings (s)  |
| -------------------------------------------- | -------------- |
| python / numpy                               |      0.254     |
| python w/ explicit loops                     |     71.8       |
| Numba(*)                                     |      0.0972    |
| Cython                                       |      0.272     |
| Fortran + f2py                               |      0.0914    |
| C++ + pybind11 (vector of vector)            |      0.166     |
| C++ + pybind11 (contiguous `Array`)          |      0.105     |


(*) timing for the second invocation, which excludes JIT overhead.

```{note}
The timings seem very sensitive to the versions of the library used,
it seems like I got better performance with GCC 13 and Cython < 3
```

We see that Numba, C++, and Fortran are all quite close in performance
and much faster than the other implementations.  It may be possible to
further optimize the numpy version, but it is so much easier to just
use Numba in this situation.
