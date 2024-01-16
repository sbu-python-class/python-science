import matplotlib.pyplot as plt
import numpy as np


def sigmoid(p):
    return 1 / (1 + np.exp(-p))

p = np.linspace(-10, 10, 200)

fig, ax = plt.subplots()

ax.plot(p, sigmoid(p))

fig.savefig("sigmoid.png")
