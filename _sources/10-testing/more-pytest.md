# More pytest

Unit tests sometimes require some setup to be done before the test is run.  Fixtures
provide this capability.

pytest provides `setup` and `teardown` functions/methods for tests --
see https://docs.pytest.org/en/6.2.x/fixture.html for more details

:::{note}
By default, pytest will capture stdout and only show it on failures.  If you want
to always show stdout, add the `-s` flag.
:::

## Example class

It is common to use a class to organize a set of related unit tests.  This is
not a full-fledged class -- it simply helps to organize data.  In particular,
there is no constructor, `__init__()`.  See https://stackoverflow.com/questions/21430900/py-test-skips-test-class-if-constructor-is-defined

We'll look at an example with a NumPy array

* We always want the array to exist for our tests, so we’ll use
  fixtures (in particular `setup_method()`) to create the array

* Using a class means that we can access the array created in setup from our class.

* We'll use NumPy's own assertion functions: https://numpy.org/doc/stable/reference/routines.testing.html


Here's an example:

```python
# a test class is useful to hold data that we might want setup
# for every test.

import numpy as np
from numpy.testing import assert_array_equal

class TestClassExample:

    @classmethod
    def setup_class(cls):
        """ this is run once for each class, before any tests """
        pass

    @classmethod
    def teardown_class(cls):
        """ this is run once for each class, after all tests """
        pass

    def setup_method(self):
        """ this is run before each of the test methods """
        self.a = np.arange(24).reshape(6, 4)

    def teardown_method(self):
        """ this is run after each of the test methods """
        pass

    def test_max(self):
        assert self.a.max() == 23

    def test_flat(self):
        assert_array_equal(self.a.flat, np.arange(24))
```

```{note}
Here we see the [`@classmethod` decorator](https://docs.python.org/3/library/functions.html#classmethod).
This means that the function receives the class itself as the first argument rather then an instance,
e.g., `self`.
```

Put this into a file called `test_class.py` and then we can run as:

```
pytest -v
```

