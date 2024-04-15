# a test class is useful to hold data that we might want set up
# for every test.

import numpy as np
from numpy.testing import assert_array_equal

class TestClassExample:
    @classmethod
    def setup_class(cls):
        """ this is run once for each class, before any tests """
        print("\nrunning setup_class()")

    @classmethod
    def teardown_class(cls):
        """ this is run once for each class, after all tests """
        print("\nrunning teardown_class()")

    def setup_method(self):
        """ this is run before each of the test methods """
        print("\nrunning setup_method()")
        self.a = np.arange(24).reshape(6, 4)

    def teardown_method(self):
        """ this is run after each of the test methods """
        print("\nrunning teardown_method()")

    def test_max(self):
        print("inside test_max()")
        assert self.a.max() == 23

    def test_flat(self):
        print("inside test_flat()")
        assert_array_equal(self.a.flat, np.arange(24))
