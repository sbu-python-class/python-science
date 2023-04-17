# Command line arguments

For standalone programs, we often want to have our program take
command line arguments that affect the runtime behavior of our
program.  There are a variety of mechanisms to do this in python, but
the best option is the [argparse
module](https://docs.python.org/3/library/argparse.html).

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
