import numpy as np

def mandelbrot(N,
               xmin=-2.0, xmax=2.0,
               ymin=-2.0, ymax=2.0,
               max_iter=10):

    x = np.linspace(xmin, xmax, N)
    y = np.linspace(ymin, ymax, N)

    c = np.zeros((N, N), dtype=np.complex128)

    for i in range(N):
        for j in range(N):
            c[i, j] = x[i] + 1j * y[j]

    z = np.zeros((N, N), dtype=np.complex128)

    # note: we need to use a numba type here
    m = np.zeros((N, N), dtype=np.int32)

    for n in range(1, max_iter+1):

        for i in range(N):
            for j in range(N):
                if m[i, j] == 0:
                    z[i, j] = z[i, j] * z[i, j] + c[i, j]

                    if np.abs(z[i,j]) > 2:
                        m[i, j] = n

    return m
