import sys

def execute(x, function=None):
    if function == None:
        sys.exit("ERROR: no function supplied")

    return function(x)


def test_function(x):
    a = "you passed in {}".format(x)
    return a


print execute("test", function=test_function)
