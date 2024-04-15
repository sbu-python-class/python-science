# More pytest

Unit tests sometimes require some setup to be done before the test is run.
Fixtures provide this capability, allowing tests to run with a consistent
environment and data.

Standard pytest fixtures are written as functions with the `@pytest.fixture`
decorator. Test functions can use them by adding a parameter with the same name
as the fixture, and will be called with whatever object the fixture returns.

An alternate method for initializing test state is with explicit setup/teardown
functions, which we'll look at shortly
(see https://docs.pytest.org/en/stable/how-to-xunit_setup.html for more details).

## Fixtures example

Here are some tests for the `Item` class using fixtures, adapted from the
[shopping cart exercise](w4-exercise-1):

```{include} ../../examples/testing/pytest/fixtures/test_item.py
:code: python
```

By default, all the fixtures that a test depends on will be run separately for
each test, to make sure one test doesn't unexpectedly modify the data for
another test. This can be overridden with the `scope` parameter to
`@pytest.fixture`, which will store the result of running the fixture and re-use
it for all the tests.


## Example class

It is common to use a class to organize a set of related unit tests.  This is
not a full-fledged class -- it simply helps to organize tests and data.  In particular,
there is no constructor, `__init__()`.  See https://stackoverflow.com/questions/21430900/py-test-skips-test-class-if-constructor-is-defined

We'll look at an example with a NumPy array

* We always want the array to exist for our tests, so we'll use
  `setup_method()` to create the array

* Using a class means that we can access the array created in setup from our class.

* We'll use NumPy's own assertion functions: https://numpy.org/doc/stable/reference/routines.testing.html


Here's an example:

```{include} ../../examples/testing/pytest/class/test_class.py
:code: python
```

```{note}
Here we see the [`@classmethod` decorator](https://docs.python.org/3/library/functions.html#classmethod).
This means that the function receives the class itself as the first argument rather than an instance,
e.g., `self`.
```

Put this into a file called `test_class.py` and then we can run as:

```
pytest -v -s
```

By default, pytest will capture stdout and only show it on failures. To make it
always show stdout, we add the `-s` flag.

```
============================= test session starts ==============================
platform linux -- Python 3.11.8, pytest-8.1.1, pluggy-1.4.0 -- /home/eric/mambaforge/envs/python-science/bin/python3.11
cachedir: .pytest_cache
rootdir: /home/eric/dev/python-science
configfile: pyproject.toml
plugins: nbval-0.10.0, cov-5.0.0, anyio-4.3.0
collected 2 items

test_class.py::TestClassExample::test_max
running setup_class()

running setup_method()
inside test_max()
PASSED
running teardown_method()

test_class.py::TestClassExample::test_flat
running setup_method()
inside test_flat()
PASSED
running teardown_method()

running teardown_class()


============================== 2 passed in 0.11s ===============================
```
