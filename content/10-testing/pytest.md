# pytest

`pytest` is a unit testing framework for python code.

Basic elements:

* Discoverability: it will find the tests

* Automation

* Fixtures (setup and teardown)

## Installing

You can install `pytest` for a single user as:

```
pip3 install pytest --user
```

This should put `pytest` in your search path, likely in `~/.local/bin`.

If you want to generate coverage reports, you should also install `pytest-cov`:

```
pip3 install pytest-cov --user
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

