# a test class is useful to hold data that we might want setup
# for every test.



class TestClassExample(object):

    @classmethod
    def setup_class(cls):
        """ this is run once for each class, before any tests """
        print("testing class {}".format(cls))

    @classmethod
    def teardown_class(cls):
        """ this is run once for each class, after all tests """
        pass

    def setup_method(self):
        """ this is run before each of the test methods """
        self.l = list(range(20))
        self.s = "this is my test string"

    def teardown_method(self):
        """ this is run after each of the test methods """
        pass

    def test_list(self):
        assert len(self.l) == 20

    def test_string(self):
        assert len(self.s.split()) == 5


