# Tools to Make Your Life Easier

There are a number of tools that help check code for formatting and
syntax errors that are quite useful for developers.  Many projects
automatically enforce these tools on changes submitted to github.

```{tip}
Many editors have plugins that can automatically run these tools
as your write your code.
```

* [flake8](https://flake8.pycqa.org/en/latest/)

  `flake8` is a checker for [PEP 8](https://peps.python.org/pep-0008/)
  style conformance.  You can turn off checks that you don't like
  via a [`.flake8`
  file](https://flake8.pycqa.org/en/latest/user/configuration.html#configuration-locations).

* [pylint](https://pypi.org/project/pylint/)

  `pylint` is a static code analyzer.  It can find errors and also suggest improvements
  to your code.  You can [generate a configuration file](https://pylint.readthedocs.io/en/latest/user_guide/configuration/index.html)
  to customize its behavior (or add a section to `pyproject.toml`).

* [black](https://pypi.org/project/black/)

  `black` is an _uncompromising code formatted_.  It will automatically rewrite your code
  based on PEP-8 style.

* [pyupgrade](https://github.com/asottile/pyupgrade)

  `pyupgrade` will upgrade source to a later python standard, making
  use of new features where available.  For instance, you can run as:

  ```
  pyupgrade --py39-plus file.py
  ```

  to update to python 3.9 support.

* [isort](https://pycqa.github.io/isort/)

  `isort` simply sorts the module imports at the top of your modules,
  grouping the standard python ones together followed by
  package-specific ones.
