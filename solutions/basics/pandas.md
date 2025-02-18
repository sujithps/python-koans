# Solving the Test Cases

Let's solve each test case:

```python
def test_pandas_basics(self):
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'Chicago']
    }
    df = pd.DataFrame(data)
    
    # 1. Number of rows
    self.assertEqual(3, len(df))
    
    # 2. Column names
    self.assertEqual(['name', 'age', 'city'], list(df.columns))
    
    # 3. Mean age
    self.assertEqual(30.0, df['age'].mean())
```