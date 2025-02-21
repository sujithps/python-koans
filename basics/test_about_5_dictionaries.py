import unittest


class AboutDictionaries(unittest.TestCase):
    def test_dictionaries(self):
        """Learn about dictionaries"""
        person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
        # Fill in the blanks
        self.assertEqual("Alice", person['name'])
        self.assertEqual(["name", "age", "city"], list(person.keys()))
        self.assertEqual(["Alice", 25, "New York"], list(person.values()))
        person['job'] = 'Data Scientist'
        self.assertEqual({'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Data Scientist'}, person)
