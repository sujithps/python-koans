import unittest


class AboutStrings(unittest.TestCase):
    def test_strings(self):
        """Learn about string operations and methods"""
        string1 = "Hello"
        string2 = "World"
        # Fill in the blanks
        self.assertEqual("Hello World", string1 + " " + string2)
        self.assertEqual("hello", string1.lower())
        self.assertEqual(5, len(string1))
        self.assertEqual("ell", string1[1:4])
        self.assertTrue("e" in string1)  # Check if 'e' is in string1

        text = "Python Programming"
        self.assertEqual("AI Programming", text.replace("Python", "AI"))
        self.assertEqual(["Python","Programming"], text.split())
        self.assertEqual(2, text.count('m'))
        self.assertTrue(text.startswith("Python"))
        self.assertEqual("PYTHON PROGRAMMING", text.upper())
        self.assertEqual("spaces", " spaces ".strip())
