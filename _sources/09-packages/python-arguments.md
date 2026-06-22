# Command line arguments

For standalone programs, we often want to have our program take
command line arguments that affect the runtime behavior of our
program.  There are a variety of mechanisms to do this in python, but
the best option is the [argparse
module](https://docs.python.org/3/library/argparse.html).

Here's an example of using `argparse` to take a variety of options:

```{literalinclude} argparse_example.py
---
language: python
```

A nice feature of `argparse` is that it automatically generates help for us.  If
we place the above code in `argparse_example.py` then we can do:

```python
python argparse_example.py --help
```
