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

    def test_random_mean(self):
        for i in range(0,10):
            length = random.randint(1, 100)
            random_array = random.randrange(0,100,length)
            self.assertEqual(my_utils.mean(random_array, np.mean(random_array)))

    def test_mean_errors(self):
        with self.assertRaises(SystemExit) as cm:
            my_utils.mean([])
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            my_utils.mean('string')
        self.assertEqual(cm.exception.code, 1)

    def test_median(self):
        self.assertEqual(my_utils.median([1, 2, 3, 4]), 2.5)  # even case
        self.assertEqual(my_utils.median([1, 2, 3, 4, 5]), 3) # odd case
        self.assertEqual(my_utils.median([2, 5, 6, 9, 12, 7]), np.median([2, 5, 6, 9, 12, 7])) #out of order list

    def test_median_errors(self):
        with self.assertRaises(SystemExit) as cm:
            my_utils.median([])
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            my_utils.median('string')
        self.assertEqual(cm.exception.code, 1)

    def test_random_median(self):
        for i in range(0,10):
            length = random.randint(1, 100)
            random_array = random.randrange(0,100,length)
            self.assertEqual(my_utils.median(random_array, np.median(random_array)))

    def test_stdev(self):
        self.assertEqual(my_utils.stdev(10, 5), 50)
        self.assertEqual(my_utils.stdev(-1, 1), -1)
        self.assertIsNone(my_utils.stdev([10]))
        self.assertEqual(my_utils.stdev([10, 1, 20, 13, 5, 12, 11]), np.std([10, 1, 20, 13, 5, 12, 11]))
    
    def test_random_stdev(self):
        for i in range(0,10):
            length = random.randint(1, 100)
            random_array = random.randrange(0,100,length)
            self.assertEqual(my_utils.stdev(random_array, np.std(random_array)))
    
    def test_stdev_errors(self):
        with self.assertRaises(SystemExit) as cm:
            my_utils.stdev([])
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            my_utils.stdev('string')
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()