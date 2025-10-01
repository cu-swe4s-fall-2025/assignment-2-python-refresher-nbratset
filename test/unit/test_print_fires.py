import sys
import unittest
import random
import numpy as np

sys.path.append('src/') # noqa

import my_utils


class TestMathLib(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(my_utils.mean([1, 1, 1, 1, 1]), 1.0)
        self.assertEqual(my_utils.mean([2, 5, 6, 9, 12, 7]), np.mean([2, 5, 6, 9, 12, 7]))
        self.assertEqual(my_utils.mean([10]), 10.0)

    def test_random_mean(self):
        for i in range(0,10):
            length = random.randint(1, 100)
            random_array = [random.randint(1, 99) for _ in range(length)]
            self.assertEqual(my_utils.mean(random_array), np.mean(random_array))

    def test_mean_errors(self):
        self.assertEqual(my_utils.mean([]), None)
        self.assertEqual(my_utils.mean(['1', '2', '3']), 2.0)

    def test_median(self):
        self.assertEqual(my_utils.median([1, 2, 3, 4]), 2.5)  # even case
        self.assertEqual(my_utils.median([1, 2, 3, 4, 5]), 3) # odd case
        self.assertEqual(my_utils.median([2, 5, 6, 9, 12, 7]), np.median([2, 5, 6, 9, 12, 7])) #out of order list

    def test_median_errors(self):
        self.assertEqual(my_utils.mean([]), None)
        self.assertEqual(my_utils.mean(['1', '2', '3']), 2.0)

    def test_random_median(self):
        for i in range(0,10):
            length = random.randint(1, 100)
            random_array = [random.randint(1, 99) for _ in range(length)]
            self.assertEqual(my_utils.median(random_array), np.median(random_array))

    def test_stdev(self):
        self.assertEqual(my_utils.stdev([10, 5]), np.std([10, 5]))
        self.assertEqual(my_utils.stdev([-1, 1]), np.std([-1, 1]))
        self.assertEqual(my_utils.stdev([10]), 0.0)
        self.assertEqual(my_utils.stdev([10, 1, 20, 13, 5, 12, 11]), np.std([10, 1, 20, 13, 5, 12, 11]))
    
    def test_stdev_errors(self):
        self.assertEqual(my_utils.mean([]), None)
        self.assertEqual(my_utils.mean(['1', '2', '3']), 2.0)

    def test_random_stdev(self):
        for i in range(0,10):
            length = random.randint(2, 100)
            random_array = [random.randint(1, 99) for _ in range(length)]
            self.assertAlmostEqual(my_utils.stdev(random_array), np.std(random_array))


if __name__ == '__main__':
    unittest.main()