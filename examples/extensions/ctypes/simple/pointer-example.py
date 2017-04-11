# this version of the driver uses the normal ctypes POINTER(), so you
# need to have your numpy array make itself appear as a C pointer
# explicitly.

import numpy as np
import ctypes as C

# load our extension -- this returns a ctypes library object
cfunc = np.ctypeslib.load_library('cfunc', '.')

# set the return type
cfunc.my_subroutine.restype = C.c_int

# set the argument types
cfunc.my_subroutine.argtypes = [C.POINTER(C.c_double),
                                C.c_int]

def my_subroutine(A):
    return cfunc.my_subroutine(A.ctypes.data_as(C.POINTER(C.c_double)), len(A))

A = np.arange(10, dtype=np.float64)
n = my_subroutine(A)


