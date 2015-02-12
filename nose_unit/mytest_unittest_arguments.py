import unittest



class TestUM(unittest.TestCase):

    def __init__(self, testname, a, b):
        self.testname = testname
        self.a = a
        self.b = b

    @classmethod
    def setUpClass(cls):
        print 'i am in setupclass'

    def setUp(self):
        print 'i am in setup'

    def tearDown(self):
        print 'i am in tearDown'
    @classmethod
    def tearDownClass(tt):
        print 'i am in teardown class'

    def test_strings_a_3(self):
        print 'i am test_strings_a_3'
        # self.assertEqual( 'aaa', 'aaa', " equal")
        assert a == b, " test failed"

    def test_version(self):
        assert self.a == self.b, "test failed"

    def test_get_with_param(self):
        assert self.a == self.b, "test failed"

    def test_unknown_method(self):
        assert self.a == self.b, "test failed"

if __name__ == '__main__':
    import sys
    user = sys.argv[1]
    pword = sys.argv[2]

    suite = unittest.TestSuite()
    suite.addTest(TestUM("test_version", user, pword))
    suite.addTest(TestUM("test_get_with_param", user, pword))
    suite.addTest(TestUM("test_unknown_method", user, pword))
    unittest.TextTestRunner().run(suite)





