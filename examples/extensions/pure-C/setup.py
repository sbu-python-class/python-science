from distutils.core import setup, Extension
import numpy

# define the extension module
numpy_in_c = Extension('numpy_in_c', sources=['numpy-ex.c'],
                       include_dirs=[numpy.get_include()]) #,
#                       define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")])

# run the setup
setup(ext_modules=[numpy_in_c])
