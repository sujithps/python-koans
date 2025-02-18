import unittest


class AboutLists(unittest.TestCase):
    def test_lists(self):
        """Learn about lists and list operations"""
        numbers = [1, 2, 3, 4, 5]
        # Fill in the operations
        self.assertEqual(__, len(numbers))
        self.assertEqual(__, numbers[2])
        numbers.append(__)
        self.assertEqual([1, 2, 3, 4, 5, 6], numbers)
        self.assertEqual(__, numbers[-1])  # Last element
        self.assertEqual(__, numbers[1:4])  # Slicing

        letters = ['a', 'b', 'c']
        letters.extend(['d', 'e'])
        self.assertEqual(__, letters)

        mixed_list = [1, 'hello', 3.14, True]
        self.assertEqual(__, mixed_list[1:3])

        numbers.insert(2, 10)
        self.assertEqual(__, numbers)

        numbers.sort(reverse=True)
        self.assertEqual(__, numbers)
