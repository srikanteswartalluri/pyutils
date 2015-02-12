__author__ = 'talluri'
import unittest
from fastcar import fastCar
from unittest import TestCase

class fastCarTest(TestCase):
    def setUp(self):
        self.fc_list = fastCar()
        print "called setup"

    def tearDown(self):
        print "called tearDown"

    def test_fast_car_list(self):
        self.assertEquals(type(self.fc_list),list,"not returning a list")

    def test_fast_car_list_empty(self):
        self.assertNotEquals(len(self.fc_list),0,"empty list returned")

    def test_fast_car_list_len(self):
        self.assertEquals(len(self.fc_list),100," list length returned is not 100")
    test_fast_car_list_len.talluritag = False
    def test_fast_car_3(self):
        self.assertEquals(self.fc_list[3-1],"Fast","string fast expected")

    def test_fast_car_7(self):
        self.assertEquals(self.fc_list[7-1],"Car","string Car expected")

    def test_fast_car_21(self):
        self.assertEqual(self.fc_list[21-1],"FastCar","Fast Car expected")

    def test_fast_car_22(self):
        self.assertEqual(self.fc_list[22-1],22,"22 expected")

    def test_fast_car_100(self):
        self.assertEqual(self.fc_list[100-1],100,"100 expected")

    # def test_fast_car_random(self):
    #     for i in range(1,101):
    #         if i
    #     self.assertEqual(self.fc_list[100-1],100,"100 expected")
    #

if __name__ == 'main':
    unittest.main()