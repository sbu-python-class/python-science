# Extensions

Python code can be slow, so we sometimes turn to _extension modules_ to
get performance in critical parts of our algorithms There are a number
of ways to write extension modules in python -- these can be in
another language like C or Fortran or use a library that converts
python into compiled code (with some restrictions) like Cython or
Numba.

We'll look at some examples of these and talk about their strengths
and weaknesses.


## Methods

* C

  * [C-API](https://docs.python.org/3/c-api/index.html) : the
    standard python interpreter (cpython) is written in C, so it is
    natural that we can write C code to interact with our python code.
    This is the python C-API.  Since NumPy is also written in C, we
    can work with NumPy arrays in C code as well.

    This will give us the performance of C compiled code, but the
    downside is that we lose a lot of what makes python great.  We
    need to pass data into C as pointers and cast them into types that
    represent the arrays we use.  This means writing a lot of
    boilerplate code just to deal with some simple operations.

    This underlies most of the techniques that we'll see here.

    These days, there are better methods for most applications.

  * [ctypes](https://docs.python.org/3/library/ctypes.html) : this
    is a module that allows you to call functions in shared libraries.
    This is part of standard python.

    With ctypes, you don't need to modify your C code -- you just need to
    define an interface to the C function in python.  However, the calling
    mechanism can be slow.

    There is support for NumPy through numpy.ctypeslib.

* Fortran

  * [f2py](https://numpy.org/doc/stable/f2py/) : this is part of
    NumPy.  It allows for easy calling of Fortran from python.

    You essentially just need to add some comments to your Fortran
    code to allow f2py to build an interface.  f2py understands the
    different orderings of indices between C and Fortran arrays.

* python

  * [Cython](https://cython.org/) : this is a superset of python that can convert python into
    compiled C code.

    The advantage here is that the code looks like python, with some
    declarations of the variable types with `cdef`.  Performance can be
    really great when you need to explicitly write out loops over
    NumPy array indices.

  * [Numba](https://numba.pydata.org/) : this is a just-in-time
    compiler.  It just requires a simple decorator and then it will
    compile a python function the first time it is encountered.
