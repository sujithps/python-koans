import unittest


class AboutControlFlow(unittest.TestCase):
    def test_if_then_else_statements(self):
        if True:
            result = 'true value'
        else:
            result = 'false value'
        self.assertEqual(__, result)

    def test_if_then_statements(self):
        result = 'default value'
        if True:
            result = 'true value'
        self.assertEqual(__, result)

    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'
        self.assertEqual(__, result)

    def test_while_statement(self):
        i = 1
        result = 0
        while i <= 5:
            result = result + i
            i += 1
        self.assertEqual(__, result)

    def test_control_flow(self):
        """Learn about if statements and loops"""

        def get_grade(score):
            # Implement the function
            pass

        self.assertEqual('A', get_grade(95))
        self.assertEqual('B', get_grade(85))
        self.assertEqual('C', get_grade(75))
        self.assertEqual('F', get_grade(60))
