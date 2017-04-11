import numpy as np
import ctypes as C

_cfunc = np.ctypeslib.load_library('cfunc_multid', '.')
_cfunc.my_subroutine.restype = C.c_int
_cfunc.my_subroutine.argtypes = [C.POINTER(C.c_double), C.c_int, C.c_int, C.POINTER(C.c_double)]

def my_subroutine(A, B):
    return _cfunc.my_subroutine(A.ctypes.data_as(C.POINTER(C.c_double)), 
                                C.c_int(A.shape[0]), C.c_int(A.shape[1]),
                                B.ctypes.data_as(C.POINTER(C.c_double)))

A = np.arange(20, dtype=np.float64)
A.shape = (4,5)


# here we pre-allocate the return array
B = np.zeros_like(A)

n = my_subroutine(A, B)

print(B)



