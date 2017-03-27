def hilbert(n):
    """ return a Hilbert matrix, H_ij = (i + j - 1)^{-1} """

    H = np.zeros((n,n), dtype=np.float64)

    for i in range(1, n+1):
        for j in range(1, n+1):
            H[i-1,j-1] = 1.0/(i + j - 1.0)
    return H

import scipy.linalg as linalg
import numpy as np

n = 13
H = hilbert(n)
x = np.arange(n)
print(x)
b = np.dot(H,x)
print(b)

xnew = linalg.solve(H, b)
print(xnew)
print(np.linalg.cond(H))

xs = linalg.lstsq(H, b)
print(xs)
