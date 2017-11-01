cimport numpy as np
import numpy as np

#cython: boundscheck=False
#cython: wraparound=False

def cy_square(np.ndarray[double, ndim=2] A):
    
    # in Cython, we should use cdef to declare the types of the variables
    # this helps with generating the C code
    cdef int nx = A.shape[0]
    cdef int ny = A.shape[1]

    # return array -- we allocate it much like in straight NumPy
    cdef np.ndarray B = np.zeros( (nx, ny), dtype=np.float64)

    cdef int i, j
    for i in range(nx):
        for j in range(ny):
            B[i,j] = A[i,j]**2

    return B

    

