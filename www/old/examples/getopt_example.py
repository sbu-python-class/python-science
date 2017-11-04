#!/usr/bin/env python

import sys
import getopt

# simple example of getopt
#
# ./getopt_example.py -a -b # -c string --darg --earg fextra

try: opts, next = getopt.getopt(sys.argv[1:], "ab:c:",
                                ["darg", "earg="])
except getopt.GetoptError:
    sys.exit("invalid calling sequence")


# set the defaults
a_present = 0
b_value = None
c_value = None
d_present = 0
e_value = None

for o, a in opts:
    if o == "-a":
        a_present = 1
    elif o == "-b":
        b_value = int(a)
    elif o == "-c":
        c_value = str(a)
    elif o == "--darg":
        d_present = 1
    elif o == "--earg":
        e_value = a

try: extras = next[0:]
except IndexError:
    pass

if a_present: print "-a set"
if not b_value == None: print "b = {}".format(b_value)
if not c_value == None: print "c = {}".format(c_value)
if d_present: print "--darg set"
if not e_value == None: print "e = {}".format(e_value)

print "extra arguments:"
for e in extras:
    print e

