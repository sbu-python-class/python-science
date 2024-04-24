import matplotlib.pyplot as plt
import numpy as np

import mandel_f2py

import time

start = time.time()

xmin = -2.5
xmax = 1.5
ymin = -2.0
ymax = 2.0

max_iter = 50

m = mandel_f2py.mandelbrot(1024, xmin, xmax, ymin, ymax, max_iter)

print(f"execution time = {time.time() - start}\n")

fig, ax = plt.subplots()
ax.imshow(np.transpose(m), origin="lower",
          extent=[xmin, xmax, ymin, ymax])

fig.tight_layout()
fig.savefig("test.png")
