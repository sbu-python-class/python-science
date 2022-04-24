# Python Modules

So far, we've been writing our code all in Jupyter.  But when it comes
time to write code that we want to reuse, we want to put it into a
standalone `*.py` file.

Then we can load it on in python (or Jupyter) and use the capabilities
it provides or make it a standalone program that can be run from the
command line.


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

  ```
  import hello
  hello.hello()
  ```

* From the command line, we can do:

  ```
  python hello.py
  ```

Additionally, on a Unix system, we can add:

```python
#!/usr/bin/env python3
```

to the top and then mark the file as executable, via:

```
chmod a+x hello.py
```

allowing us to execute it simply as:

```
./hello.py
```

## Command line arguments

For standalone programs, we often want to have our program take command line arguments that affect the runtime behavior of our program.
There are a variety of mechanisms to do this in python, but the best option is the [argparse module](https://docs.python.org/3/library/argparse.html).

Here's an example of using `argparse` to take a variety of options:

```python
#!/usr/bin/env python3

# to get usage: use -h
import argparse

# simple example of argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", help="the -a option", action="store_true")
parser.add_argument("-b", help="-b takes a number", type=int, default=0)
parser.add_argument("-c", help="-c takes a string", type=str, default=None)
parser.add_argument("--darg", help="the --darg option", action="store_true")
parser.add_argument("--earg", help="--earg takes a string", type=str, metavar="t
est",
                    default="example string")

# extra arguments (positional)
parser.add_argument("extras", metavar="extra", type=str, nargs="*",
                    help="optional positional arguments")

args = parser.parse_args()

if args.a:
    print("-a set")
print(f"-b = {args.b}")
print(f"-c = {args.c}")
if args.darg:
    print("--dargs set")
print(f"--earg value = {args.earg}")

print(" ")
print("extra positional arguments: ")
if len(args.extras) > 0:
    for e in args.extras:
        print(e)
```
