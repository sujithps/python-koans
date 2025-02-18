# Basic Arithmetic Operations

### Addition (+)
```python
# Basic addition
2 + 2 = 4
5 + 3 = 8
10 + 20 = 30

# Example test
self.assertEqual(4, 2 + 2)  # This will pass
```

### Subtraction (-)
```python
# Basic subtraction
10 - 5 = 5
20 - 8 = 12
100 - 50 = 50

# Example test
self.assertEqual(5, 10 - 5)  # This will pass
```

### Multiplication (*)
```python
# Basic multiplication
3 * 4 = 12
5 * 6 = 30
10 * 10 = 100

# Example test
self.assertEqual(12, 3 * 4)  # This will pass
```

### Division (/)
```python
# Regular division (always returns float)
15 / 3 = 5.0
10 / 2 = 5.0
20 / 4 = 5.0

# Example test
self.assertEqual(5.0, 15 / 3)  # This will pass
```

### Integer Division (//)
```python
# Integer division (floors the result)
17 // 5 = 3    # Because 17 ÷ 5 = 3.4, floored to 3
20 // 3 = 6    # Because 20 ÷ 3 = 6.666..., floored to 6
10 // 3 = 3    # Because 10 ÷ 3 = 3.333..., floored to 3

# How it works:
# 1. 17 ÷ 5 = 3.4
# 2. Floor the result (round down to nearest integer)
# 3. Result is 3

# Example test
self.assertEqual(3, 17 // 5)  # This will pass
```

### Modulo (%)
```python
# Modulo (remainder after division)
17 % 5 = 2    # Because 17 = 3 * 5 + 2
20 % 3 = 2    # Because 20 = 6 * 3 + 2
10 % 3 = 1    # Because 10 = 3 * 3 + 1

# How it works:
# 1. 17 ÷ 5 = 3 remainder 2
# 2. Result is 2 (the remainder)

# Example test
self.assertEqual(2, 17 % 5)  # This will pass
```

### Exponentiation (**)
```python
# Exponentiation (power)
2 ** 3 = 8     # 2 * 2 * 2 = 8
3 ** 2 = 9     # 3 * 3 = 9
5 ** 2 = 25    # 5 * 5 = 25

# Example test
self.assertEqual(8, 2 ** 3)  # This will pass
```


## Understanding Order of Operations

Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction):

```python
# Order of operations
2 + 3 * 4         # = 14 (not 20) because multiplication happens before addition
(2 + 3) * 4       # = 20 because parentheses are evaluated first
2 ** 3 + 1        # = 9 because exponentiation happens before addition
15 / 3 + 2        # = 7.0 because division happens before addition
```

##  Common Mistakes to Avoid

1. **Division Always Returns Float**
```python
15 / 3  # Returns 5.0 (float), not 5 (integer)
# Use // for integer division if you need an integer result
```

2. **Integer Division Floors Down**
```python
17 // 5  # Returns 3, not 3.4
-17 // 5  # Returns -4, not -3 (floors down, not towards zero)
```

3. **Modulo with Negative Numbers**
```python
17 % 5   # Returns 2
-17 % 5  # Returns 3 (might be unexpected)
```

## Practice Problems

Try these problems to test your understanding:

1. What is the result of `8 // 3`?
   ```python
   # Solution:
   # 8 ÷ 3 = 2.666...
   # Floor down to 2
   self.assertEqual(2, 8 // 3)
   ```

2. What is the remainder when 23 is divided by 7?
   ```python
   # Solution:
   # 23 = 3 * 7 + 2
   # Remainder is 2
   self.assertEqual(2, 23 % 7)
   ```

3. What is 2 to the power of 4?
   ```python
   # Solution:
   # 2 * 2 * 2 * 2 = 16
   self.assertEqual(16, 2 ** 4)
   ```

## Running the Tests

To run the tests:
```bash
# From command line
python -m unittest about_numbers_and_arithmetic.py

# Or run specific test
python -m unittest about_numbers_and_arithmetic.py -k test_numbers_and_arithmetic
```