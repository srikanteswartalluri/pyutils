import unittest


class TestUM(unittest.TestCase):
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
    def test_numbers_3_4(self):
        print 'i am test_numbers_3_4'
        self.assertEqual( 2, 12, "test failed")

    def test_strings_a_3(self):
        print 'i am test_strings_a_3'
        self.assertEqual( 'aaa', 'aaa', " equal")

if __name__ == '__main__':
    unittest.main()
