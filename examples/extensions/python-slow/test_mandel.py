import matplotlib.pyplot as plt
import numpy as np

import mandel

import time

start = time.time()

xmin = -2.5
xmax = 1.5
ymin = -2.0
ymax = 2.0

m = mandel.mandelbrot(1024, xmin, xmax, ymin, ymax, max_iter=50)

print(f"execution time = {time.time() - start}\n")

fig, ax = plt.subplots()
ax.imshow(np.transpose(m % 16), origin="lower",
          extent=[xmin, xmax, ymin, ymax], cmap="viridis")

fig.tight_layout()
fig.savefig("test.png")
