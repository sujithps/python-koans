import unittest


class AboutDictionaries(unittest.TestCase):
    def test_dictionaries(self):
        """Learn about dictionaries"""
        person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
        # Fill in the blanks
        self.assertEqual(__, person['name'])
        self.assertEqual(__, list(person.keys()))
        self.assertEqual(__, list(person.values()))
        person['job'] = __
        self.assertEqual({'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Data Scientist'}, person)
