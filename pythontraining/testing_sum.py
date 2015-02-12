__author__ = 'talluri'
import unittest
from unittest import TestCase
from unittesting import sum


class unittestingTest(TestCase):
    def test_sum(self):
        sum_val = sum(3,5)
        self.assertEqual(sum_val, 8, "there is a problem in sum")
    def test_sum_2(self):
        try:
            sum_val = sum('tet','pi','qui')
        except Exception as e:
            print e.message
    def test_sum_0_args(self):#test driven development
        self.assertEquals(sum(),None,'fault behaviour')
    def test_float_args(self):
        self.assertEquals(sum(3.5,2.5),6.0)
    # def test_non_numeric_args(self):
    #     self.assertRaises(sum('ts','pi'),"hello")
if __name__ == 'main':
    unittest.main()