import unittest


class AboutVariablesAndAssignments(unittest.TestCase):
    def test_variables_and_assignment(self):
        """Learn about variable assignment and basic data types"""
        # Assign values to make the assertions pass
        x = 7
        y = 8.0
        self.assertEqual(x + y, 15)
        self.assertIsInstance(x, int)
        self.assertIsInstance(y, float)
