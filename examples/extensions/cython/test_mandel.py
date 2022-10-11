import mandel

import time

start = time.time()

m = mandel.mandelbrot(1024, max_iter=50)

print(f"execution time = {time.time() - start}\n")
