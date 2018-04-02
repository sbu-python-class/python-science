import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def main():

    data = np.loadtxt("signal.txt")

    x = data[:,0]
    sig = data[:,2]
    orig = data[:,1]

    N = len(x)

    window = signal.gaussian(N, 20.0)
    window /= np.sum(window)
    clean = signal.convolve(sig, window, mode="same")

    plt.plot(x, clean)
    plt.plot(x, orig)
    plt.savefig("cleaned.png")
    


if __name__ == "__main__":
    main()
