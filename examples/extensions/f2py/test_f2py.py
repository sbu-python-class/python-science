import numpy as np
import numpy_in_f

a = np.arange(24, dtype=np.float64)
a.shape = (4,6)

print(a.flags)

b = numpy_in_f.square(a, a.shape[0], a.shape[1])

print(b)

print(b.flags)

