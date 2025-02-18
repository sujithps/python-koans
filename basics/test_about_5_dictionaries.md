# 1. Dictionary Basics

### What is a Dictionary?
A dictionary is a collection of key-value pairs. Think of it like a real dictionary where:
- The word you're looking up is the "key"
- The definition is the "value"

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with initial key-value pairs
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Alternative creation using dict()
person = dict(name='Alice', age=25, city='New York')
```

### Key Characteristics
1. Keys must be unique
2. Keys must be immutable (strings, numbers, tuples)
3. Values can be of any type
4. Dictionaries are mutable (can be changed)
5. As of Python 3.7+, dictionaries maintain insertion order

## 2. Basic Dictionary Operations

### Accessing Values
```python
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Using square bracket notation
name = person['name']     # 'Alice'

# Using get() method (safer)
age = person.get('age')   # 25
# With default value if key doesn't exist
salary = person.get('salary', 0)  # 0
```

### Modifying Dictionaries
```python
person = {'name': 'Alice', 'age': 25}

# Adding new key-value pair
person['city'] = 'New York'

# Modifying existing value
person['age'] = 26

# Update multiple key-value pairs
person.update({'job': 'Engineer', 'age': 27})
```

### Dictionary Methods

#### Getting Keys and Values
```python
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Get all keys
keys = person.keys()      # dict_keys(['name', 'age', 'city'])
keys_list = list(keys)    # ['name', 'age', 'city']

# Get all values
values = person.values()  # dict_values(['Alice', 25, 'New York'])
values_list = list(values)  # ['Alice', 25, 'New York']

# Get all key-value pairs (items)
items = person.items()    # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])
```

## 4. Common Dictionary Operations

### Checking for Keys
```python
person = {'name': 'Alice', 'age': 25}

# Using in operator
has_name = 'name' in person              # True
has_salary = 'salary' in person          # False

# Using get() method
age = person.get('age')                  # 25
salary = person.get('salary')            # None
default_salary = person.get('salary', 0) # 0
```

### Removing Items
```python
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Remove and return value for key
age = person.pop('age')      # age = 25, key-value pair removed

# Remove and return last inserted item
last_item = person.popitem() # Returns tuple of last key-value pair

# Remove specific key
del person['name']

# Clear all items
person.clear()  # Empty dictionary
```

### Dictionary Comprehension
```python
# Create dictionary from two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
# Result: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Filter dictionary
person = {'name': 'Alice', 'age': 25, 'salary': 50000}
adult_info = {k: v for k, v in person.items() if k != 'age'}
# Result: {'name': 'Alice', 'salary': 50000}
```

## 5. Common Patterns and Best Practices

### Default Values with setdefault()
```python
person = {'name': 'Alice'}

# Instead of:
if 'age' not in person:
    person['age'] = 25

# Use:
person.setdefault('age', 25)  # Sets 'age': 25 if 'age' doesn't exist
```

### Merging Dictionaries
```python
# Python 3.5+
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'age': 26}

# Merge with update
merged = dict1.copy()
merged.update(dict2)

# Or use | operator (Python 3.9+)
merged = dict1 | dict2
```

### Handling Missing Keys
```python
person = {'name': 'Alice'}

# Bad: Direct access might raise KeyError
try:
    age = person['age']
except KeyError:
    age = None

# Good: Use get()
age = person.get('age')

# Better: Use get() with default
age = person.get('age', 0)
```

## 6. Common Mistakes to Avoid

1. **Modifying Dictionary During Iteration**
```python
# Wrong
for key in person:
    if some_condition:
        del person[key]  # Can raise RuntimeError

# Correct
keys_to_delete = [k for k in person if some_condition]
for key in keys_to_delete:
    del person[key]
```

2. **Using Mutable Objects as Keys**
```python
# Wrong - will raise TypeError
dict1 = {['a', 'b']: 1}

# Correct
dict1 = {('a', 'b'): 1}  # Use tuple instead of list
```

3. **Not Copying When Needed**
```python
# Wrong (creates reference)
dict1 = {'name': 'Alice'}
dict2 = dict1  # Changes to dict2 affect dict1

# Correct (creates copy)
dict2 = dict1.copy()
```

## 7. Practice Exercises

1. Create a frequency counter:
```python
def count_frequency(text):
    return {char: text.count(char) for char in text}

# Test
print(count_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

2. Invert a dictionary:
```python
def invert_dict(d):
    return {v: k for k, v in d.items()}

# Test
original = {'a': 1, 'b': 2}
print(invert_dict(original))  # {1: 'a', 2: 'b'}
```