import unittest


class AboutNumbersAndArithmetic(unittest.TestCase):
    def test_numbers_and_arithmetic(self):
        """Learn about numbers and basic arithmetic operations"""
        # Fill in the values using numbers to make the assertions pass
        self.assertEqual(4, 2 + 2)
        self.assertEqual(5, 10 - 5)
        self.assertEqual(12, 3 * 4)
        self.assertEqual(5, 15 / 3)
        self.assertEqual(3, 17 // 5)  # Integer division
        self.assertEqual(2, 17 % 5)  # Modulo
        self.assertEqual(8, 2 ** 3)  # Exponentiation
