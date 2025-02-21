import unittest


class AboutFunctions(unittest.TestCase):
    def test_functions(self):
        """Learn about functions and return values"""

        def multiply_list(numbers, factor):
            new_numbers = []
            for number in numbers:
                new_numbers.append(number * factor)
            return new_numbers

        input_list = [1, 2, 3, 4]
        self.assertEqual([2, 4, 6, 8], multiply_list(input_list, 2))
        self.assertEqual([3, 6, 9, 12], multiply_list(input_list, 3))
