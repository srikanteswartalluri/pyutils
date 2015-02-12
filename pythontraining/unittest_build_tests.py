__author__ = 'talluri'
import unittest
import testFastCar
import testing_sum

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(testFastCar)
suite.addTests(loader.loadTestsFromModule(testing_sum))
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
