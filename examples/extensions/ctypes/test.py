import numpy as np
import ctypes as C

_cfunc = np.ctypeslib.load_library('cfunc', '.')
_cfunc.my_subroutine.restype = C.c_int
_cfunc.my_subroutine.argtypes = [C.POINTER(C.c_double), C.c_int]

def my_subroutine(A):
    return _cfunc.my_subroutine(A.ctypes.data_as(C.POINTER(C.c_double)), len(A))

A = np.arange(10, dtype=np.float64)
n = my_subroutine(A)


