import cython
import numpy as np
cimport numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.returns(np.ndarray)
def mandelbrot(int N,
               double xmin=-2.0, double xmax=2.0,
               double ymin=-2.0, double ymax=2.0,
               int max_iter=10):

    cdef np.ndarray[np.float64_t, ndim=1] x = np.linspace(xmin, xmax, N, dtype=np.float64)
    cdef np.ndarray[np.float64_t, ndim=1] y = np.linspace(ymin, ymax, N, dtype=np.float64)

    cdef np.ndarray[np.complex128_t, ndim=2] c = np.zeros((N, N), dtype=np.complex128)

    cdef unsigned int i, j
    for i in range(N):
        for j in range(N):
            c[i, j] = x[i] + 1j * y[j]

    cdef np.ndarray[np.complex128_t, ndim=2] z = np.zeros((N, N), dtype=np.complex128)

    cdef np.ndarray[np.int32_t, ndim=2] m = np.zeros((N, N), dtype=np.int32)

    cdef unsigned int n
    for n in range(1, max_iter+1):

        for i in range(N):
            for j in range(N):
                if m[i, j] == 0:
                    z[i, j] = z[i, j] * z[i, j] + c[i, j]

                    if abs(z[i,j]) > 2:
                        m[i, j] = n

    return m
