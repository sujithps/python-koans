import unittest
import numpy as np


class AboutNumpyBasics(unittest.TestCase):
    def test_numpy_basics(self):
        """Learn about basic NumPy operations"""

        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])

        self.assertTrue(np.array_equal(__, array1 + array2))
        self.assertTrue(np.array_equal(__, array1 * 2))
        self.assertEqual(__, np.mean(array1))
        self.assertEqual(__, np.sum(array2))
