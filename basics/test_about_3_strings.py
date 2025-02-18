import unittest


class AboutStrings(unittest.TestCase):
    def test_strings(self):
        """Learn about string operations and methods"""
        string1 = "Hello"
        string2 = "World"
        # Fill in the blanks
        self.assertEqual(__, string1 + " " + string2)
        self.assertEqual(__, string1.lower())
        self.assertEqual(__, len(string1))
        self.assertEqual(__, string1[1:4])
        self.assertTrue(__ in string1)  # Check if 'e' is in string1

        text = "Python Programming"
        self.assertEqual(__, text.replace("Python", "AI"))
        self.assertEqual(__, text.split())
        self.assertEqual(__, text.count('m'))
        self.assertTrue(text.startswith(__))
        self.assertEqual(__, text.upper())
        self.assertEqual(__, " spaces ".strip())
