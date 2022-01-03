
import numpy
import ctypes

_libfunctions = numpy.ctypeslib.load_library('libfunctions', '.')

_libfunctions.hello.argtypes = [ctypes.c_int]
_libfunctions.hello.restype  =  ctypes.c_void_p

_libfunctions.dprod.argtypes = [numpy.ctypeslib.ndpointer(dtype=numpy.float), ctypes.c_int]
_libfunctions.dprod.restype  = ctypes.c_double

_libfunctions.dcumsum.argtypes = [numpy.ctypeslib.ndpointer(dtype=numpy.float), numpy.ctypeslib.ndpointer(dtype=numpy.float), ctypes.c_int]
_libfunctions.dcumsum.restype  = ctypes.c_void_p

def hello(n):
    return _libfunctions.hello(int(n))

def dprod(x, n=None):
    if n is None:
        n = len(x)
    x = numpy.asarray(x, dtype=numpy.float)
    return _libfunctions.dprod(x, int(n))

def dcumsum(a, n):
    a = numpy.asarray(a, dtype=numpy.float)
    b = numpy.empty(len(a), dtype=numpy.float)
    _libfunctions.dcumsum(a, b, int(n))
    return b
