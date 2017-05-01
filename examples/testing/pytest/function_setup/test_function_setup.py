# to run this, in this directory, simply do
#
#   pytest -vs .

def multiply(a, b):
    return a*b

def setup_function(function):
    # this is called before every function
    print("setting up {}".format(function))

def teardown_function(function):
    # this is called after every function
    print("done")

def test_multiply():
    assert multiply(4, 6) == 24

def test_multiply2():
    assert multiply(5, 6) == 24

