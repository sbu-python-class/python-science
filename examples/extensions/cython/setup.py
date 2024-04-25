from setuptools import setup
from Cython.Build import cythonize

setup(name="mandel",
      ext_modules=cythonize("mandel.pyx"),
      zip_safe=False)
