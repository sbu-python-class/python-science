import matplotlib.pyplot as plt
import numpy as np

# the mandelbrot set is defined such that z_{n+1} = z_n^2 + c
# remains bounded, which is sufficient to say that |z_{n+1}| <= 2
# where c is a complex # and we start with z_0 = 0

# we want to consider a range of c, as complex numbers c = x + iy,
# were -2 < x < 2 and -2 < y < 2

N = 1024

c = np.zeros((N, N), dtype=np.complex)

region = 2

if region == 0:
    xmin = -2
    xmax = 1
    ymin = -1.5
    ymax = 1.5

elif region == 1:
    xmin = 0
    xmax = 0.5
    ymin = -0.75
    ymax = -0.25

elif region == 2:
    # nice spot
    xc = -0.7435669
    yc = 0.1314023
    dx = 0.004 #0.0022878

    xmin = xc-0.5*dx
    xmax = xc+0.5*dx
    ymin = yc-0.5*dx
    ymax = yc+0.5*dx

elif region == 3:
    # dagger
    xmin = -0.8
    xmax = -0.7
    ymin = 0.0
    ymax = 0.1

x = np.linspace(xmin, xmax, N, dtype=np.float)
y = np.linspace(ymin, ymax, N, dtype=np.float)

c[:,:].real = x[:,np.newaxis]
c[:,:].imag = y[np.newaxis,:]

z = np.zeros((N,N), dtype=np.complex)

niter = np.zeros((N,N), dtype=np.int)
niter[:,:] = -1

MAX_ITER = 1024

for n in range(MAX_ITER):
    idx = niter == -1
    z[idx] = z[idx]**2 + c[idx]
    idx = np.logical_and(abs(z) > 2, niter == -1)
    niter[idx] = n

# some things may still have not passed
niter[niter == -1] = MAX_ITER-1

plt.imshow(np.log10(niter.T), extent=[xmin, xmax, ymin, ymax],
           origin="lower", cmap="magma_r")

f = plt.gcf()
f.set_size_inches(8.0, 8.0)
plt.savefig("mandel.png")
