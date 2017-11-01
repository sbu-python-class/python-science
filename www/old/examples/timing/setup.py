from distutils.core import setup, Extension
import numpy

# define the extension module
laplace_CAPI = Extension('laplace_CAPI', sources=['laplace_CAPI.c'],
                       include_dirs=[numpy.get_include()]) #,
#                       define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")])

# run the setup
setup(ext_modules=[laplace_CAPI])

