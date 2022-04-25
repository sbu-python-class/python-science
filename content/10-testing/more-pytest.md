# More pytest

Unit tests sometiems require some setup to be done before the test is run.  Fixtures
provide this capability.

pytest provides `setup` and `teardown` functions/methods for tests --
see https://docs.pytest.org/en/6.2.x/fixture.html for more details

:::{note}
By default, pytest will capture stdout and only show it on failures.  If you want
to always show stdout, add the `-s` flag.
:::
