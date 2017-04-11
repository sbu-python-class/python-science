# based on http://technicaldiscovery.blogspot.com/2011/06/speeding-up-python-numpy-cython-and.html

import numpy as np
import time

# here's an alternate way to do the building of the cython version
import pyximport
pyximport.install(setup_args={'include_dirs':[np.get_include()]})
from laplace_cython import cy_update

# f2py version
from laplace_fortran import f90_update

# ctypes version
import ctypes as C
from numpy.ctypeslib import ndpointer
_cfunc = np.ctypeslib.load_library('laplace_C', '.')
_cfunc.C_update.restype = C.c_int
_cfunc.C_update.argtypes = [ndpointer(C.c_double, flags="C_CONTIGUOUS"),
                            C.c_int, C.c_int,
                            C.c_double, C.c_double]

# C-API version
from laplace_CAPI import CAPI_update


dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy

# pure python (the wrong way) method
def py_update(u):
    nx, ny = u.shape
    for i in range(1,nx-1):
        for j in range(1, ny-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))

# numpy method -- note that this is actually a Jacobi iteration, not G-S.
# the operation count should be the same, but the convergence will be worse.
def num_update(u):
    u[1:-1,1:-1] = ((u[2:,1:-1]+u[:-2,1:-1])*dy2 + 
                    (u[1:-1,2:] + u[1:-1,:-2])*dx2) / (2*(dx2+dy2))



# ctypes wrapper 
def ctypes_update(u):
    return _cfunc.C_update(u, C.c_int(u.shape[0]), C.c_int(u.shape[1]),
                           dx2, dy2)


# our driver that will run things with a given implementation of the 
# smoothing
def calc(N, Niter=100, func=py_update, args=(), order="C"):
    u = np.zeros([N, N], dtype=np.float64, order=order)
    u[0] = 1   # boundary condition
    for i in range(Niter):
        func(u,*args)
    return u



N = 64
iters = 1000

# pure python
start = time.time()
res_py = calc(N, Niter=iters)
print("pure python: {} s".format(time.time()-start))


# NumPy
start = time.time()
res_np = calc(N, Niter=iters, func=num_update)
print("NumPy: {} s".format(time.time()-start))


# Cython
start = time.time()
res_cy = calc(N, Niter=iters, func=cy_update, args=(dx2, dy2))
print("Cython: {} s".format(time.time()-start))


# f2py -- here we need to initialize the array in Fortran order so
# we can use the "inout" argument type in Fortran
start = time.time()
res_f90 = calc(N, Niter=iters, func=f90_update, 
              args=(N, N, dx2, dy2), order="F")
print("f2py: {} s".format(time.time()-start))


# ctypes
start = time.time()
res_ctypes = calc(N, Niter=iters, func=ctypes_update)
print("ctypes: {} s".format(time.time()-start))


# C-API
start = time.time()
res_CAPI = calc(N, Niter=iters, func=CAPI_update, args=(dx2, dy2))
print("C-API: {} s".format(time.time()-start))







# check the answers
print(" ")
print("max diff NumPy: {}".format(np.max(abs(res_py-res_np)[1:-1,1:-1])))
print("max diff Cython: {}".format(np.max(abs(res_py-res_cy)[1:-1,1:-1])))
print("max diff F90: {}".format(np.max(abs(res_py-res_f90)[1:-1,1:-1])))
print("max diff ctypes: {}".format(np.max(abs(res_py-res_ctypes)[1:-1,1:-1])))
print("max diff C-API: {}".format(np.max(abs(res_py-res_CAPI)[1:-1,1:-1])))


