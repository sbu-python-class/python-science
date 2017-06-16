import re

strings = [r"<a>this is my string</a>",
           r"<b>this is a different string</b>",
           r"<tag>multicharacter tag</tag>"]

# this is the pattern that we will match -- it has 3 groups
re_test = r"<(\w*)>(.*)</(\w*)>"


for s in strings:
    a = re.search(re_test, s)

    if not a == None:
        if a.group(1) == a.group(3):
            # we found a match
            print("string in '{}' tags is: {}".format(a.group(1), a.group(2)))




