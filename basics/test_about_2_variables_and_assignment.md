# Variables and Assignment

### Basic Variable Assignment
```python
# Simple assignment
name = "John"
age = 25
height = 1.75

# Multiple assignment
x, y = 10, 20
```

### Variable Naming Rules
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive
- Cannot use Python keywords

```python
# Valid names
age = 25
_private = "hidden"
user_name = "john"
firstName = "Alice"

# Invalid names
2name = "John"    # Can't start with number
my-name = "John"  # Can't use hyphen
class = "Python"  # Can't use Python keywords
```

## 2. Basic Data Types

### Integers (int)
```python
# Whole numbers without decimal points
x = 5
y = -10
big_num = 1000000

# Checking type
isinstance(x, int)  # Returns True
type(x)            # Returns <class 'int'>
```

### Floating Point Numbers (float)
```python
# Numbers with decimal points
x = 3.14
y = -0.001
z = 2.0

# Converting to float
float_num = float(5)    # 5.0
float_str = float("3.14")  # 3.14

# Checking type
isinstance(x, float)  # Returns True
type(x)              # Returns <class 'float'>
```

## 3. Type Conversion

### Converting Between Types
```python
# Integer to float
x = float(5)      # 5.0

# Float to integer
y = int(3.14)     # 3 (truncates decimal)

# String to number
z = int("123")    # 123
w = float("3.14") # 3.14
```


## 4. Common Operations with Mixed Types

```python
# Integer + Integer = Integer
5 + 3      # 8 (int)

# Integer + Float = Float
5 + 3.0    # 8.0 (float)

# Float + Float = Float
3.0 + 2.0  # 5.0 (float)
```

## 5. Common Mistakes to Avoid

1. **Forgetting to Make a Float**
```python
# Wrong
x = 10
y = 5    # This is an integer, not a float

# Correct
x = 10
y = 5.0  # Add decimal point for float
```

2. **Using String Numbers**
```python
# Wrong
x = "10"
y = "5.0"   # These are strings, not numbers

# Correct
x = 10
y = 5.0     # Use actual numbers
```

3. **Not Checking Types**
```python
# Always verify types when required
isinstance(x, int)    # Check if integer
isinstance(y, float)  # Check if float
```

## 6. Practice Problems

1. Create an integer and a float that sum to 20:
```python
# Solution
a = 15        # integer
b = 5.0       # float
print(a + b)  # 20.0
```

2. Convert types and check results:
```python
# Integer to float
num1 = 7
float_num = float(num1)
print(isinstance(float_num, float))  # True

# Float to integer
num2 = 7.8
int_num = int(num2)
print(int_num)  # 7 (decimal is truncated)
```

## 7. Testing the Solution

To run the tests:
```bash
python -m unittest about_variables_and_assignments.py
```

Remember:
- The sum must be exactly 15
- x must be an integer (no decimal point)
- y must be a float (must have decimal point)
- Many correct combinations are possible