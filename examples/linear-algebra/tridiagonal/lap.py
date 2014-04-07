# we want to solve f" = g(x)
#
# differencing  f_{i+1} - 2 f_i + f_{i-1} = dx**2 g_i
#
# imagine that our grid runs from 0, ... N-1.  We specify Dirichlet
# boundary conditions at 0 and N-1, so we only need to solve for 
# the interior points, 1, ..., N-2.
#
# at the left boundary, we have:
#
# f_2 - 2 f_1 = dx**2 g_1
#
# at the right boundary, we have:
#
# -2 f_{N-1} + f_{N-2} = dx**2 g_{N-1}
#
# Our system can be written as:
#
# A f = dx**2 g
#
# where A is an (N-2) x (N-2) tridiagonal matrix and f is the solution
# for the N-2 interior points.
#
# Here, we'll solve f" = sin x on [0, 2pi], with f(0) = f(2pi) = 0.  This
# has the analytic solution f(x) = -sin x

import numpy as np
from scipy import linalg
import pylab


# our grid -- including endpoints
N = 100
x = np.linspace(0.0, 2.0*np.pi, N, endpoint=True)
dx = x[1]-x[0]

# our source
g = np.sin(x)

# our matrix will be tridiagonal, with [1, -2, 1] on the diagonals
# we only solve for the N-2 interior points

# diagonal
d = -2*np.ones(N-2)

# upper -- note that the upper diagonal has 1 less element than the
# main diagonal.  The SciPy banded solver wants the matrix in the 
# form:
#
# *    a01  a12  a23  a34  a45    <- upper diagonal
# a00  a11  a22  a33  a44  a55    <- diagonal
# a10  a21  a32  a43  a54   *     <- lower diagonal
#

u = np.ones(N-2)
u[0] = 0.0

# lower
l = np.ones(N-2)
l[N-3] = 0.0

# put the upper, diagonal, and lower parts together as a banded matrix
A = np.matrix([u,d,l])

# solve A sol = dx**2 g for the inner N-2 points
sol = linalg.solve_banded((1,1), A, dx**2*g[1:N-1])

pylab.plot(x[1:N-1], sol)
pylab.savefig("lap.png")

