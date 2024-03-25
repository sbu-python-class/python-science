# Real World Example

Let's look at the testing in a larger python package.  We'll use our
group's python hydrodynamics code, pyro, as a test:

https://github.com/python-hydro/pyro2

## Installing

We need to install the package first, via the `setup.py`:

```bash
python setup.py install --user
```

or alternately as

```bash
pip install .
```

## Running the tests

We can run the tests via:

```bash
cd pyro
pytest -v
```

## Using notebooks as tests

Sometimes we want to use Jupyter notebooks as tests themselves&mdash;this
is enabled via the [nbval plugin](https://nbval.readthedocs.io/en/latest/).  In
this way, pytest will execute the cells in the notebook and compare
the result to the result stored in the notebook.  If they agree, then
the test passes.

Sometimes there's a particular cell that we don't want to be part of the
testing&mdash;we can disable these on a cell-by-cell basis by [adding
tags to a cell](https://nbval.readthedocs.io/en/latest/#Using-tags-instead-of-comments).

We can test notebooks as:

```bash
cd pyro
pytest -v --nbval
```

## Coverage report

The [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) plugin enables the generation
of a coverage report.  This will tell you what fraction of each python file was tested.
We run this as:

```bash
cd pyro
pytest -v --cov=. --nbval
```

## Other types of tests

Unit tests are only one form of testing&mdash;they test a function in
isolation of others.  Sometimes we need to test everything working together.
For scientific codes, regression testing is often used.  The basic workflow
is:

* Start with the project working in a way you are happy with

* Store the output of one (or more) runs as a _benchmark_.

* Each time you make changes, run the code and compare the new output
  to the stored benchmark.

  * If there are no differences, then your changes are likely good
    (but there is always the case of some feature not being tested).

  * If there are differences, then either you introduced a bug, in which
    case you should fix it, or you fixed a bug, in which case you should
    update the benchmarks.

For our example code, pyro, the regression test runs simulations using
all the different solvers and compares against the stored output, zone-by-zone
for any differences.  The comparison itself is built into the main driver
of the code and can be invoked as:

```bash
./pyro/test.py
```
