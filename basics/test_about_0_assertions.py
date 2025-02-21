import unittest


class AboutAssertions(unittest.TestCase):
    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        self.assertTrue(True)  # This should be True

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """

        self.assertTrue(True, "This should be True -- Please fix this")

    def test_fill_in_values(self):
        """
        Fill in the values to make the tests pass
        """

        self.assertEqual(2, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)
