import unittest


class AboutLists(unittest.TestCase):
    def test_lists(self):
        """Learn about lists and list operations"""
        numbers = [1, 2, 3, 4, 5]
        # Fill in the operations
        self.assertEqual(5, len(numbers))
        self.assertEqual(3, numbers[2])
        numbers.append(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], numbers)
        self.assertEqual(6, numbers[-1])  # Last element
        self.assertEqual([2,3,4], numbers[1:4])  # Slicing

        letters = ['a', 'b', 'c']
        letters.extend(['d', 'e'])
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], letters)

        mixed_list = [1, 'hello', 3.14, True]
        self.assertEqual(['hello', 3.14], mixed_list[1:3])

        numbers.insert(2, 10)
        self.assertEqual([1, 2, 10, 3, 4, 5, 6], numbers)

        numbers.sort(reverse=True)
        self.assertEqual([10, 6, 5, 4, 3, 2, 1], numbers)
