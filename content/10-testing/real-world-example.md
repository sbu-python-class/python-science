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



## Using notebooks as tests




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
