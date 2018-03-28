import numpy as np
import matplotlib.pyplot as plt

# make a signal that we will convolve

def f(x, L):
    A = L/10.0
    return 2*np.sin(2*np.pi*x/L) + x*(L-x)**2/L**3 * np.cos(x) + 5*x*(L-x)/L**2 + A/2 + 0.1*A*np.sin(13*np.pi*x/L)


N = 2048
L = 50.0

x = np.linspace(0, L, N, endpoint=False)
f = f(x, L)
fnew = f + 0.5*np.random.randn(N)

with open("signal.txt", "w") as fo:
    for n in range(N):
        fo.write("{:20} {:20} {:20}\n".format(x[n], f[n], fnew[n]))

plt.plot(x, f)
plt.plot(x, fnew, zorder=-100)



plt.savefig("test.png")
