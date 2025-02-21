# Python Fundamentals Guide for AI Learning

## Table of Contents
- [1. Numbers and Arithmetic](#1-numbers-and-arithmetic)
- [2. Variables and Data Types](#2-variables-and-data-types)
- [3. Strings](#3-strings)
- [4. Lists](#4-lists)
- [5. Dictionaries](#5-dictionaries)
- [6. Control Flow](#6-control-flow)
- [7. Functions](#7-functions)
- [8. List Comprehensions](#8-list-comprehensions)

## 1. Numbers and Arithmetic

### Basic Operations
```python
# Addition, Subtraction, Multiplication, Division
2 + 2    # = 4
10 - 5   # = 5
3 * 4    # = 12
15 / 3   # = 5.0 (always returns float)

# Integer Division and Modulo
17 // 5  # = 3 (floor division)
17 % 5   # = 2 (remainder)

# Exponentiation
2 ** 3   # = 8 (2 to the power of 3)
```

### Advanced Number Operations
```python
# Working with floating points
3.14 * 2        # = 6.28
round(3.14159, 2)  # = 3.14

# Absolute values and powers
abs(-42)        # = 42
pow(2, 4)       # = 16
max(3, 7, 2, 9) # = 9
```

## 2. Variables and Data Types

### Basic Variable Assignment
```python
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_valid = True # Boolean

# Multiple assignment
a, b, c = 1, 2, 3

# Type checking
type(x)     # <class 'int'>
type(y)     # <class 'float'>
type(name)  # <class 'str'>
```

### Complex Numbers
```python
z = 3 + 4j
z.real    # = 3.0
z.imag    # = 4.0
```

## 3. Strings

### String Operations
```python
# Concatenation
"Hello" + " " + "World"  # = "Hello World"

# Methods
text = "Python Programming"
text.lower()          # = "python programming"
text.upper()          # = "PYTHON PROGRAMMING"
text.replace("Python", "AI")  # = "AI Programming"
text.split()          # = ["Python", "Programming"]
len(text)            # = 18

# Slicing
text[0:6]   # = "Python"
text[-11:]  # = "Programming"
```

### String Formatting
```python
name = "Alice"
age = 25
f"Name: {name}, Age: {age}"  # = "Name: Alice, Age: 25"
```

## 4. Lists

### List Operations
```python
numbers = [1, 2, 3, 4, 5]

# Basic operations
numbers.append(6)     # Add to end
numbers.insert(2, 10) # Insert at position
numbers.extend([7, 8]) # Add multiple items
numbers.remove(3)     # Remove first occurrence
numbers.pop()         # Remove and return last item

# Slicing
numbers[1:4]    # Get subset
numbers[-2:]    # Get last two items
numbers[::-1]   # Reverse list

# Sorting
numbers.sort()           # In-place sort
numbers.sort(reverse=True) # Reverse sort
```

## 5. Dictionaries

### Dictionary Operations
```python
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Accessing and modifying
person['name']           # = 'Alice'
person['job'] = 'Developer'  # Add new key-value
person.get('salary', 'Not Found')  # Safe access with default

# Methods
person.keys()    # Get all keys
person.values()  # Get all values
person.items()   # Get key-value pairs

# Nested dictionaries
nested = {
    'user1': {'name': 'Bob', 'scores': [85, 90]},
    'user2': {'name': 'Charlie', 'scores': [88, 92]}
}
```

## 6. Control Flow

### If Statements
```python
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'
```

### Loops
```python
# For loops
for i in range(5):
    print(i)

# While loops
count = 0
while count < 5:
    count += 1
```

## 7. Functions

### Basic Functions
```python
def multiply_list(numbers, factor):
    return [num * factor for num in numbers]

# Function with multiple returns
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

### Advanced Functions
```python
# Recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Lambda functions
square = lambda x: x**2
```

## 8. List Comprehensions

### Basic Comprehensions
```python
numbers = [1, 2, 3, 4, 5]

# Square numbers
squares = [x**2 for x in numbers]

# Filter even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Nested comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
```

## Learning Path and Tips

### Beginner Level
1. Start with basic data types (numbers, strings)
2. Learn about variables and assignments
3. Practice with lists and dictionaries
4. Understand control flow (if statements, loops)

### Intermediate Level
1. Master functions and their variations
2. Learn list comprehensions
3. Start working with file operations
4. Practice error handling

### Advanced Level
1. Work with NumPy arrays
2. Learn Pandas for data manipulation
3. Explore advanced Python features
4. Practice with real-world projects

### Practice Tips
1. Write code daily
2. Use Python's interactive mode (REPL)
3. Solve coding challenges
4. Build small projects
5. Read and understand others' code

## Additional Resources

### Official Documentation
- [Python Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)


### Online/Offline Courses
- Upcode Software Labs: [Python for AI](https://upcode.in)

## Next Steps

After mastering these basics, consider:
1. Learning about Python decorators
2. Understanding generators and iterators
3. Exploring object-oriented programming
4. Learning about Python's asyncio
5. Studying Python for specific domains (web, data science, AI)