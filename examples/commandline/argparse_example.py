#!/usr/bin/env python

# to get usage: use -h
from __future__ import print_function

import sys
import argparse


# simple example of argparse
#
# ./argparse_example.py -a -b # -c string --darg --earg fextra

parser = argparse.ArgumentParser()
parser.add_argument("-a", help="the -a option", action="store_true")
parser.add_argument("-b", help="-b takes a number", type=int, default=0)
parser.add_argument("-c", help="-c takes a string", type=str, default=None)
parser.add_argument("--darg", help="the --darg option", action="store_true")
parser.add_argument("--earg", help="--earg takes a string", type=str, metavar="test",
                    default="example string")

# extra arguments (positional)
parser.add_argument("extras", metavar="extra", type=str, nargs="*",
                    help="optional positional arguments")

args = parser.parse_args()


if args.a: print("-a set")
print("-b = {}".format(args.b))
print("-c = {}".format(args.c))
if args.darg: print("--dargs set")
print("--earg value = {}".format(args.earg))

print(" ")
print("extra positional arguments: ")
if len(args.extras) > 0:
    for e in args.extras:
        print(e)

