# Packaging



Let's look at the structure of creating an installable python package.
The python packaging system is constantly evolving, and the current recommendations
of tools is list here: https://packaging.python.org/en/latest/guides/tool-recommendations/


## Our example

We'll work on an example that builds on the Mandelbrot set exercise
from our matplotlib discussion.  Our example is hosted here:

https://github.com/sbu-python-class/mymodule

On your local computer, if you have `git` installed, you can clone this via:

```
git clone https://github.com/sbu-python-class/mymodule.git
```

The directory structure appears as:

```
mymodule
├── mymodule
│   ├── __init__.py
│   └── mandel.py
└── README.md
```


## setuptools

We'll look at how to use `setuptools` to package our library.  See the
packaging gui




Some documentation on `setuptools` is available here:
https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/



