# pytest

`pytest` is a unit testing framework for python code.

Basic elements:

* Discoverability: it will find the tests

* Automation

* Fixtures (setup and teardown)

## Installing

You can install `pytest` for a single user as:

```
pip install pytest
```

This should put `pytest` in your search path, likely in `~/.local/bin`.

If you want to generate coverage reports, you should also install `pytest-cov`:

```
pip install pytest-cov
```

## Test discovery

Adhering to these naming conventions will ensure that your tests are automatically found:

* File names should start or end with “test”:

  * `test_example.py`
  * `example_test.py`

* For tests in a class, the class name should begin with `Test`

  * e.g., `TestExample`
  * There should be no `__init__()`

* Test method / function names should start with `test_`

  * e.g., `test_example()`

## Assertions

Tests use assertions (via python’s `assert` statement) to check behavior at runtime

* https://docs.python.org/3/reference/simple_stmts.html#assert 

* Basic usage: `assert expression`

  * Raises `AssertionError` if expression is not true

  * e.g., `assert 1 == 0` will fail with an exception

## Simple pytest example

Create a file named `test_simple.py` with the following content:

```python
def multiply(a, b):
    return a*b

def test_multiply():
    assert multiply(4, 6) == 24

def test_multiply2():
    assert multiply(5, 6) == 2
```

then we can run the tests as:

```
pytest -v
```

and we get the output:

```
============================= test session starts ==============================
platform linux -- Python 3.11.3, pytest-7.2.2, pluggy-1.0.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/zingale/temp/pytest
plugins: anyio-3.6.2
collected 2 items                                                              

test_simple.py::test_multiply PASSED                                     [ 50%]
test_simple.py::test_multiply2 FAILED                                    [100%]

=================================== FAILURES ===================================
________________________________ test_multiply2 ________________________________

    def test_multiply2():
>       assert multiply(5, 6) == 2
E       assert 30 == 2
E        +  where 30 = multiply(5, 6)

test_simple.py:8: AssertionError
=========================== short test summary info ============================
FAILED test_simple.py::test_multiply2 - assert 30 == 2
========================= 1 failed, 1 passed in 0.04s ==========================
```

this is telling us that one of our tests has failed.
