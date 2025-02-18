import unittest


class AboutFunctions(unittest.TestCase):
    def test_functions(self):
        """Learn about functions and return values"""

        def multiply_list(numbers, factor):
            # Implement the function
            pass

        input_list = [1, 2, 3, 4]
        self.assertEqual([2, 4, 6, 8], multiply_list(input_list, 2))
        self.assertEqual([3, 6, 9, 12], multiply_list(input_list, 3))
