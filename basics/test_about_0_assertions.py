import unittest


class AboutAssertions(unittest.TestCase):
    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        self.assertTrue(False)  # This should be True

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """

        self.assertTrue(False, "This should be True -- Please fix this")

    def test_fill_in_values(self):
        """
        Fill in the values to make the tests pass
        """

        self.assertEqual(__, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = __
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = __
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)
