# Python List Comprehensions

## 1. Basic List Comprehension Syntax

### Basic Structure
```python
# Basic syntax:
# [expression for item in iterable]

# Traditional way (using for loop)
squares = []
for x in range(5):
    squares.append(x ** 2)

# Same thing with list comprehension
squares = [x ** 2 for x in range(5)]
```

### Anatomy of a List Comprehension
```python
# [expression      for item      in iterable]
# │                │             │
# │                │             └─ Source list/sequence
# │                └─ Loop variable
# └─ What to do with each item
```

## 2. Simple List Comprehension Examples

### Squaring Numbers
```python
numbers = [1, 2, 3, 4, 5]

# Create list of squares
squares = [num ** 2 for num in numbers]
# Result: [1, 4, 9, 16, 25]

# Step by step:
# 1. num = 1: 1 ** 2 = 1
# 2. num = 2: 2 ** 2 = 4
# 3. num = 3: 3 ** 2 = 9
# 4. num = 4: 4 ** 2 = 16
# 5. num = 5: 5 ** 2 = 25
```

### Filtering Even Numbers
```python
numbers = [1, 2, 3, 4, 5]

# Get even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
# Result: [2, 4]

# Step by step:
# 1. num = 1: 1 % 2 == 0? False (skip)
# 2. num = 2: 2 % 2 == 0? True (include 2)
# 3. num = 3: 3 % 2 == 0? False (skip)
# 4. num = 4: 4 % 2 == 0? True (include 4)
# 5. num = 5: 5 % 2 == 0? False (skip)
```

### Filtering Long Words
```python
words = ['hello', 'world', 'python', 'ai']

# Get words longer than 4 letters
long_words = [word for word in words if len(word) > 4]
# Result: ['hello', 'python']

# Step by step:
# 1. word = 'hello': len('hello') > 4? True (include 'hello')
# 2. word = 'world': len('world') > 4? True (include 'world')
# 3. word = 'python': len('python') > 4? True (include 'python')
# 4. word = 'ai': len('ai') > 4? False (skip)
```

## 4. Common Patterns

### Transform Each Item
```python
# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
# Result: [2, 4, 6, 8, 10]

# Convert to uppercase
words = ['hello', 'world']
upper = [word.upper() for word in words]
# Result: ['HELLO', 'WORLD']
```

### Filter Items
```python
# Filter positive numbers
numbers = [-2, -1, 0, 1, 2]
positive = [num for num in numbers if num > 0]
# Result: [1, 2]

# Filter strings containing 'a'
words = ['apple', 'banana', 'cherry']
a_words = [word for word in words if 'a' in word]
# Result: ['apple', 'banana']
```

### Combine Transform and Filter
```python
# Square only even numbers
numbers = [1, 2, 3, 4, 5]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
# Result: [4, 16]

# Uppercase words longer than 3 letters
words = ['cat', 'dog', 'elephant']
long_upper = [word.upper() for word in words if len(word) > 3]
# Result: ['ELEPHANT']
```

## 5. Comparing with Traditional For Loops

### Transform Example
```python
numbers = [1, 2, 3, 4, 5]

# Traditional for loop
squares_traditional = []
for num in numbers:
    squares_traditional.append(num ** 2)

# List comprehension
squares_comprehension = [num ** 2 for num in numbers]
```

### Filter Example
```python
numbers = [1, 2, 3, 4, 5]

# Traditional for loop
even_traditional = []
for num in numbers:
    if num % 2 == 0:
        even_traditional.append(num)

# List comprehension
even_comprehension = [num for num in numbers if num % 2 == 0]
```

## 6. Best Practices

### 1. Keep It Simple
```python
# Good - Simple and clear
squares = [x**2 for x in numbers]

# Bad - Too complex, use a for loop instead
result = [x**2 if x > 0 else -x**2 if x < 0 else 0 
          for x in numbers if x != 0]
```

### 2. Consider Readability
```python
# Good - Easy to understand
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Better - Use traditional loop if logic is complex
result = []
for x in numbers:
    if x % 2 == 0 and x > 0 and x < 100:
        result.append(complex_calculation(x))
```

### 3. Watch Out for Memory
```python
# Bad - May consume too much memory
big_list = [x**2 for x in range(1000000)]

# Good - Use generator expression for large sequences
big_list = list(x**2 for x in range(1000000))
```