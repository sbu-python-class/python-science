# Tools to Make Your Life Easier

There are a number of tools that help check code for formatting and
syntax errors that are quite useful for developers.  Many projects
automatically enforce these tools on changes submitted to github.

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

* [isort](https://pycqa.github.io/isort/)

