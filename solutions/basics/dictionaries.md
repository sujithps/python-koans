# Solving the Test Cases

Let's break down and solve each test case:

```python
def test_dictionaries(self):
    person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    
    # 1. Access value using key
    self.assertEqual('Alice', person['name'])
    
    # 2. Get list of keys
    self.assertEqual(['name', 'age', 'city'], list(person.keys()))
    
    # 3. Get list of values
    self.assertEqual(['Alice', 25, 'New York'], list(person.values()))
    
    # 4. Add new key-value pair
    person['job'] = 'Data Scientist'
    self.assertEqual(
        {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Data Scientist'},
        person
    )
```