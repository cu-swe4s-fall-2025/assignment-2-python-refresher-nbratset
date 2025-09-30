import sys
import unittest
import random
import numpy as np

sys.path.append('src/') # noqa

import my_utils


class TestMathLib(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(my_utils.mean([1, 1, 1, 1, 1]), 1)
        self.assertEqual(my_utils.mean([2, 5, 6, 9, 12, 7]), np.mean([2, 5, 6, 9, 12, 7]))
        self.assertEqual(my_utils.mean([10]), 10)

    # def test_mean_errors(self):
    #     pass

    def test_median(self):
        self.assertEqual(my_utils.median([1, 2, 3, 4]), 2.5)  # even case
        self.assertEqual(my_utils.median([1, 2, 3, 4, 5]), 3) # odd case
        self.assertEqual(my_utils.median([2, 5, 6, 9, 12, 7]), np.median([2, 5, 6, 9, 12, 7])) #out of order list

    def test_stdev(self):
        self.assertEqual(my_utils.stdev(10, 5), 50)
        self.assertEqual(my_utils.stdev(-1, 1), -1)
        self.assertIsNone(my_utils.stdev([10]))
        self.assertEqual(my_utils.stdev([10, 1, 20, 13, 5, 12, 11]), np.std([10, 1, 20, 13, 5, 12, 11]))


if __name__ == '__main__':
    unittest.main()