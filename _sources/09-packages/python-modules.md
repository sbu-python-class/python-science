# Python Modules

So far, we've been writing our code all in Jupyter.  But when it comes
time to write code that we want to reuse, we want to put it into a
standalone `*.py` file.

Then we can load it on in python (or Jupyter) and use the capabilities
it provides or make it a standalone program that can be run from the
command line.

```{tip}
Jupyter is great for interactive explorations and sharing your workflow with others
in a self-contained way.  But if there is an operation that you do over and over,
you should put it into a separate module that you import.  That way you only need to
maintain and debug a single instance of the function, and all your workflows can reuse it.
```


## Editors

There are a number of popular editors for writing python source.  Some
popular ones include:

* spyder: https://www.spyder-ide.org/

* VS Code: https://code.visualstudio.com/

* emacs / vi


## Standalone module

Here's a very simply module (lets call it `hello.py`):

```python
def hello():
    print("hello")

if __name__ == "__main__":
    hello()
```

There are two ways we can use this.

* Inside of python (or IPython), we can do:

  ```python
  import hello
  hello.hello()
  ```

* From the command line, we can do:

  ```python
  python hello.py
  ```

Additionally, on a Unix system, we can add:

```python
#!/usr/bin/env python3
```

to the top and then mark the file as executable, via:

```bash
chmod a+x hello.py
```

allowing us to execute it simply as:

```bash
./hello.py
```

```{hint}
Here we see how the `__name__` variable is treated by python:

* If we import our module into python, then `__name__` is set to the module name

* If we run the module from the command line, then `__name__` is set to `__main__`
```

## Changing module contents

If we make changes to our module file, then we need to re-import it.  This can be done as:

```python
import importlib
example = importlib.reload(example)
```
