# see https://docs.scipy.org/doc/numpy/reference/routines.ctypeslib.html

import numpy as np
import numpy.ctypeslib as npc
import ctypes as C

# load our extension -- this returns a ctypes library object
cfunc = npc.load_library('cfunc', '.')

# set the return type
cfunc.my_subroutine.restype = C.c_int

# set the argument types
cfunc.my_subroutine.argtypes = [npc.ndpointer(C.c_double, flags="C_CONTIGUOUS"),
                                C.c_int]

def my_subroutine(A):
    return cfunc.my_subroutine(A, len(A))

A = np.arange(10, dtype=np.float64)
n = my_subroutine(A)


