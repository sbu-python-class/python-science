import numpy_in_c
import numpy as np

a = np.arange(20, dtype=np.float64)
a.shape = (4,5)
print(a)

b = numpy_in_c.example(a)
print(b)



