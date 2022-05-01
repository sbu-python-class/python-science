# example from: http://technicaldiscovery.blogspot.com/2011/06/speeding-up-python-numpy-cython-and.html
from numpy import zeros
import laplace

import time

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy


# pure python version
def py_update(u):
    nx, ny = u.shape
    for i in range(1,nx-1):
        for j in range(1, ny-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))


# general interface to do Niter iterations
def calc(N, Niter=100, func=py_update, args=()):
    u = zeros([N, N])
    u[0] = 1   # this is a boundary condition
    for i in range(Niter):
        func(u,*args)
    return u

# python version
start = time.time()

res_py = calc(64)

print("pure python: ", time.time() - start)


start = time.time()

res_cy = calc(64, func=laplace.cy_update, args=(dx2, dy2) )

print("cython: ", time.time() - start)






