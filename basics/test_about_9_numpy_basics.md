# NumPy Basics: A Comprehensive Guide

## 1. Introduction to NumPy

### What is NumPy?
NumPy (Numerical Python) is a fundamental package for scientific computing in Python. 
It provides:
- Multi-dimensional array objects
- Various derived objects (masks, matrices)
- A collection of routines for fast operations

Primarily works with homogeneous arrays (same data type)
Focuses on numerical operations
Data structure: n-dimensional arrays (ndarrays)

### Use Cases
- Mathematical operations
- Linear algebra
- Statistical functions
- Image processing
- Scientific computing

### Installing NumPy
```python
# Using pip
pip install numpy

# Import in your code
import numpy as np
```

## 2. Creating NumPy Arrays

### Basic Array Creation
```python
# From Python lists
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Create special arrays
zeros = np.zeros(3)          # [0. 0. 0.]
ones = np.ones(3)            # [1. 1. 1.]
range_array = np.arange(3)   # [0 1 2]
```

### Array Properties
```python
array = np.array([1, 2, 3, 4])

# Common properties
array.shape    # Returns shape (4,)
array.size     # Returns size 4
array.dtype    # Returns data type (e.g., int64)
array.ndim     # Returns number of dimensions (1)
```

## 3. Basic Array Operations

### Arithmetic Operations
```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Addition
sum_array = array1 + array2    # [5, 7, 9]
# Step by step:
# [1, 2, 3] + [4, 5, 6] = [1+4, 2+5, 3+6] = [5, 7, 9]

# Multiplication by scalar
doubled = array1 * 2           # [2, 4, 6]
# Step by step:
# [1, 2, 3] * 2 = [1*2, 2*2, 3*2] = [2, 4, 6]

# Element-wise multiplication
product = array1 * array2      # [4, 10, 18]
```

### Statistical Operations
```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Mean (average)
mean_value = np.mean(array1)    # 2.0
# Step by step:
# 1. Sum all elements: 1 + 2 + 3 = 6
# 2. Divide by count: 6 / 3 = 2.0

# Sum
sum_value = np.sum(array2)      # 15
# Step by step:
# 4 + 5 + 6 = 15

# Other statistical operations
min_value = np.min(array1)      # 1
max_value = np.max(array1)      # 3
median = np.median(array1)      # 2.0
std_dev = np.std(array1)        # Standard deviation
```

## 5. Additional NumPy Operations

### Array Indexing and Slicing
```python
array = np.array([1, 2, 3, 4, 5])

# Indexing
first = array[0]      # 1
last = array[-1]      # 5

# Slicing
subset = array[1:4]   # [2, 3, 4]
every_second = array[::2]  # [1, 3, 5]
```

### Array Reshaping
```python
array = np.array([1, 2, 3, 4, 5, 6])

# Reshape to 2x3 matrix
matrix = array.reshape(2, 3)
# Result:
# [[1, 2, 3],
#  [4, 5, 6]]

# Flatten matrix back to 1D
flattened = matrix.flatten()  # [1, 2, 3, 4, 5, 6]
```

### Array Comparison
```python
array1 = np.array([1, 2, 3])
array2 = np.array([1, 2, 3])

# Compare arrays
is_equal = np.array_equal(array1, array2)  # True

# Element-wise comparison
greater_than = array1 > 2  # [False, False, True]
```

## 6. Common NumPy Functions

### Mathematical Functions
```python
array = np.array([1, 2, 3])

# Square root
sqrt = np.sqrt(array)  # [1., 1.414, 1.732]

# Exponential
exp = np.exp(array)   # [2.718, 7.389, 20.086]

# Logarithm
log = np.log(array)   # [0., 0.693, 1.099]
```

### Aggregation Functions
```python
array = np.array([1, 2, 3, 4])

# Sum
total = np.sum(array)      # 10

# Product
product = np.prod(array)   # 24

# Cumulative sum
cumsum = np.cumsum(array)  # [1, 3, 6, 10]
```

## 7. Best Practices

### 1. Memory Efficiency
```python
# Good - Use NumPy operations
result = array1 + array2

# Bad - Use loops
result = []
for i in range(len(array1)):
    result.append(array1[i] + array2[i])
```

### 2. Type Checking
```python
# Check if input is NumPy array
if not isinstance(array, np.ndarray):
    array = np.array(array)

# Check array shape
if array.shape != (3,):
    raise ValueError("Array must be 1D with 3 elements")
```

### 3. Error Handling
```python
try:
    result = array1 + array2
except ValueError as e:
    print("Arrays must have same shape")
```