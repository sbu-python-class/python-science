#cython: boundscheck=False
#cython: wraparound=False

cimport numpy as np

def cy_update(np.ndarray[double, ndim=2] u, double dx2, double dy2):
    cdef unsigned int i, j
    for i in xrange(1,u.shape[0]-1):
        for j in xrange(1, u.shape[1]-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))
