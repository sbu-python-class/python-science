import numpy as np
import square

import time

N = 400
M = 600

A = np.arange(M*N, dtype=np.float64)
A.shape = (N,M)

# python version (note: this is a simple example, so doing B = A**2
# will be faster than any of these methods)
start = time.time()

B = np.zeros_like(A)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        B[i,j] = A[i,j]**2


print("pure python: ", time.time() - start)

start = time.time()
B = A**2
print("numpy: ", time.time() - start)


# using our Cython routine
start = time.time()

B_cy = square.cy_square(A)

print("cython: ", time.time() - start)






