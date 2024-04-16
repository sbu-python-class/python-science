# More pytest

Unit tests sometimes require some setup to be done before the test is run.
Fixtures provide this capability, allowing tests to run with a consistent
environment and data.

Standard pytest fixtures are written as functions with the `@pytest.fixture`
decorator:
```python
@pytest.fixture
def message():
    return "Hello world!"
```

A fixture may return an object, which will be passed to any function
that requests it, or it may just do some setup tasks (like creating a file or
connecting to a database).

Test functions can request a fixture by specifying a parameter with the same
name as the fixture:
```python
def test_split(message):
    assert len(message.split()) == 2
```

An alternate method for initializing test state is with explicit setup/teardown
functions, which we'll look at a bit later. This is a style that's available in
many other languages as well: see https://en.wikipedia.org/wiki/XUnit.

## Fixtures examples

Fixtures are reusable across different tests. This lets us avoid repeating the
same setup code in multiple places, especially as we add more tests or need
more complicated inputs.

Here are some tests for the `Item` class that use fixtures, adapted from the
[shopping cart exercise](w4-exercise-1). The full code is available
[here](https://github.com/sbu-python-class/python-science/blob/main/examples/testing/pytest/fixtures/test_item.py)
on the github repository for this site. You can download this file and run
the tests with `pytest -v test_item.py`.

```{literalinclude} ../../examples/testing/pytest/fixtures/test_item.py
:lines: 58-68
```

All the fixtures that a test depends on will run once for each test.
This gives each test a fresh copy of the data, so any changes made to the
fixture results inside a test won't impact other tests.
```{literalinclude} ../../examples/testing/pytest/fixtures/test_item.py
:lines: 70-83
```

We can also test that a function raises specific exceptions with `pytest.raises`:
```{literalinclude} ../../examples/testing/pytest/fixtures/test_item.py
:lines: 85-91
```

### Fixtures can request other fixtures

This is useful to split up complex initialization into smaller parts.
A fixture can also modify the results of the fixtures it requests, which *will*
be visible to anything that includes the fixture.

Here is a set of tests that show how this can be used ([test_list.py](https://github.com/sbu-python-class/python-science/blob/main/examples/testing/pytest/fixtures/test_list.py)):
```{literalinclude} ../../examples/testing/pytest/fixtures/test_list.py
:lines: 1-13
```

Note that `append_1()` and `append_2()` only modify `numbers`, and don't return
anything. `append_2()` requires `append_1`, to make sure they are run in the
right order.

This test only requires `numbers`, so it will receive an empty list:
```{literalinclude} ../../examples/testing/pytest/fixtures/test_list.py
:lines: 15-16
```

This test requires `append_1`, but not `append_2`:
```{literalinclude} ../../examples/testing/pytest/fixtures/test_list.py
:lines: 18-19
```

This test requires `append_2`, which itself pulls in `append_1`:
```{literalinclude} ../../examples/testing/pytest/fixtures/test_list.py
:lines: 21-22
```


## Example class

It is common to use a class to organize a set of related unit tests.  This is
not a full-fledged class -- it simply helps to organize tests and data.  In particular,
there is no constructor, `__init__()`.  See https://stackoverflow.com/questions/21430900/py-test-skips-test-class-if-constructor-is-defined

We'll look at an example with a NumPy array

* We'll use xunit-style setup/teardown methods to store the array as a class
  member

  * This way we don't have to ask for it in each of the tests

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

```bash
pytest -v
```

```{admonition} Quick Exercise
Try adding a new test that modifies `self.a`, above `test_max()`.
Does this behave as you expect? What happens if you move the array creation
into `setup_class()` instead?
```

% By default, pytest will capture stdout and only show it on failures. To make it
% always show stdout, we add the `-s` flag.
