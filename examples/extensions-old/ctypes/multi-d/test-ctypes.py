import numpy as np
import ctypes as C
from numpy.ctypeslib import ndpointer

# the NumPy way to call this function

_cfunc = np.ctypeslib.load_library('cfunc_multid', '.')
_cfunc.my_subroutine.restype = C.c_int
_cfunc.my_subroutine.argtypes = [ndpointer(C.c_double, flags="C_CONTIGUOUS"),
                                 C.c_int, C.c_int, 
                                 ndpointer(C.c_double, flags="C_CONTIGUOUS")]

def my_subroutine(A, B):
    return _cfunc.my_subroutine(A, C.c_int(A.shape[0]), C.c_int(A.shape[1]), B)

A = np.arange(20, dtype=np.float64)
A.shape = (4,5)


# here we pre-allocate the return array
B = np.zeros_like(A)

n = my_subroutine(A, B)

print(B)



