import unittest


class AboutListComprehensions(unittest.TestCase):
    def test_list_comprehensions(self):
        """Learn about list comprehensions"""
        numbers = [1, 2, 3, 4, 5]
        # Fill in the list comprehensions
        squares = [n*n for n in numbers]  # Create a list of squares
        even_numbers = [n for n in numbers if n%2 ==0]  # Filter even numbers

        self.assertEqual([1, 4, 9, 16, 25], squares)
        self.assertEqual([2, 4], even_numbers)

        words = ['hello', 'world', 'python', 'ai']
        long_words = [n for n in words if len(n) >= 4]  # Words longer than 4 letters
        self.assertEqual(['hello', 'world', 'python'], long_words)


