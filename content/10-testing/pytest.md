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

