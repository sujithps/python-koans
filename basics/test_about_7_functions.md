# Python Functions: A Comprehensive Guide

## 1. Function Basics

### What is a Function?
A function is a reusable block of code that performs a specific task. Think of it as a mini-program that you can call whenever needed.

### Basic Function Structure
```python
def function_name(parameter1, parameter2):
    # Function body
    # Code to perform the task
    return result  # Optional return statement
```

### Simple Function Example
```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")  # Returns "Hello, Alice!"
```

## 2. Function Parameters

### Types of Parameters
```python
# Required parameters
def add(a, b):
    return a + b

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple parameters
def calculate_total(items, tax_rate, discount=0):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    final_total = subtotal + tax - discount
    return final_total
```

### Parameter Passing
```python
# Passing arguments by position
result = add(5, 3)  # a=5, b=3

# Passing arguments by name (keyword arguments)
result = add(b=3, a=5)  # Same result

# Mix of positional and keyword arguments
greeting = greet("Alice", greeting="Hi")
```

## 3. Return Values

### Single Return Value
```python
def square(number):
    return number ** 2

result = square(4)  # Returns 16
```

### Multiple Return Values
```python
def get_coordinates():
    return 5, 10  # Returns tuple (5, 10)

x, y = get_coordinates()  # Unpacking return values
```

### No Return Value (None)
```python
def print_message(msg):
    print(msg)
    # No return statement = returns None

result = print_message("Hello")  # result is None
```

## 5. Common Function Patterns

### Processing Lists
```python
# Sum all numbers
def sum_list(numbers):
    return sum(numbers)

# Filter list
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

# Transform list
def square_all(numbers):
    return [n ** 2 for n in numbers]
```

### Working with Multiple Lists
```python
# Combine two lists
def combine_lists(list1, list2):
    return list(zip(list1, list2))

# Merge lists with operation
def add_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]
```

## 6. Best Practices

### 1. Add Docstrings
```python
def multiply_list(numbers, factor):
    """
    Multiply each number in a list by a factor.
    
    Args:
        numbers (list): List of numbers to multiply
        factor (int): Number to multiply by
    
    Returns:
        list: New list with multiplied values
    
    Example:
        >>> multiply_list([1, 2, 3], 2)
        [2, 4, 6]
    """
    return [number * factor for number in numbers]
```

### 2. Input Validation
```python
def multiply_list(numbers, factor):
    # Validate inputs
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("all elements must be numbers")
    if not isinstance(factor, (int, float)):
        raise TypeError("factor must be a number")
    
    return [number * factor for number in numbers]
```

### 3. Use Clear Names
```python
# Bad
def ml(n, f):
    return [x * f for x in n]

# Good
def multiply_list(numbers, factor):
    return [number * factor for number in numbers]
```

## 7. Practice Examples

1. Filter and Transform List
```python
def process_numbers(numbers):
    """Filter even numbers and multiply by 2"""
    return [n * 2 for n in numbers if n % 2 == 0]

# Test
print(process_numbers([1, 2, 3, 4]))  # [4, 8]
```

2. Combine Multiple Operations
```python
def analyze_numbers(numbers):
    """Return min, max, and average"""
    if not numbers:
        return None
    return {
        'min': min(numbers),
        'max': max(numbers),
        'avg': sum(numbers) / len(numbers)
    }

# Test
print(analyze_numbers([1, 2, 3, 4]))
```