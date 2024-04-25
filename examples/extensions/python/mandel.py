import numpy as np

def mandelbrot(N,
               xmin=-2.0, xmax=2.0,
               ymin=-2.0, ymax=2.0,
               max_iter=10):

    x = np.linspace(xmin, xmax, N)
    y = np.linspace(ymin, ymax, N)

    xv, yv = np.meshgrid(x, y, indexing="ij")

    c = xv + 1j*y

    z = np.zeros((N, N), dtype=np.complex128)

    m = np.zeros((N, N), dtype=np.int32)

    for i in range(1, max_iter+1):
        z[m == 0] = z[m == 0]**2 + c[m == 0]

        m[np.logical_and(np.abs(z) > 2, m == 0)] = i

    return m
