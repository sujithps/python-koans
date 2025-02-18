import unittest
import pandas as pd


class AboutPandasBasics(unittest.TestCase):
    def test_pandas_basics(self):
        """Learn about basic Pandas operations"""

        data = {
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [25, 30, 35],
            'city': ['New York', 'San Francisco', 'Chicago']
        }
        df = pd.DataFrame(data)

        self.assertEqual(__, len(df))
        self.assertEqual(__, list(df.columns))
        self.assertEqual(__, df['age'].mean())
