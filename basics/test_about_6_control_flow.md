# Python Control Flow
## 1. Understanding Boolean Expressions
Before diving into control flow, it's crucial to understand boolean expressions:

Comparison Operators in Detail

```python # Equality (==)
5 == 5     # True
5 == '5'   # False (different types)
5 == 5.0   # True (numeric comparison)

# Not Equal (!=)
5 != 3     # True
5 != 5     # False
5 != '5'   # True (different types)

# Greater Than (>)
5 > 3      # True
5 > 5      # False
5 > 7      # False

# Less Than (<)
3 < 5      # True
5 < 5      # False
7 < 5      # False

# Greater Than or Equal (>=)
5 >= 5     # True
6 >= 5     # True
4 >= 5     # False

# Less Than or Equal (<=)
5 <= 5     # True
4 <= 5     # True
6 <= 5     # False
```

Boolean Operations in Detail
```python # AND operator (both conditions must be True)
True and True     # True
True and False    # False
False and True    # False
False and False   # False

# OR operator (at least one condition must be True)
True or True      # True
True or False     # True
False or True     # True
False or False    # False

# NOT operator (inverts boolean value)
not True          # False
not False         # True
not (5 > 3)       # False

# Combining operators
x = 5
(x > 0) and (x < 10)    # True
not (x < 0 or x > 10)   # True (same as above)
```

## 1. if Statements

### Basic if Structure
```python
# Simple if statement
if condition:
    # code executed if condition is True
    pass

# if-else statement
if condition:
    # code executed if condition is True
    pass
else:
    # code executed if condition is False
    pass

# if-elif-else statement
if condition1:
    # code executed if condition1 is True
    pass
elif condition2:
    # code executed if condition2 is True
    pass
else:
    # code executed if all conditions are False
    pass
```

### Example 1: Simple if-else
```python
# Test case 1
if True:
    result = 'true value'
else:
    result = 'false value'
# result will be 'true value'

# Understanding why:
# - True is a boolean value
# - When condition is True, the first block executes
# - The else block is skipped entirely
```

### Example 2: if without else
```python
# Test case 2
result = 'default value'
if True:
    result = 'true value'
# result will be 'true value'

# Understanding why:
# - Initial value is set to 'default value'
# - When condition is True, value is overwritten
# - If condition was False, default value would remain
```

### Example 3: if-elif-else
```python
# Test case 3
if False:
    result = 'first value'
elif True:
    result = 'true value'
else:
    result = 'default value'
# result will be 'true value'

# Understanding why:
# - First condition (False) is skipped
# - Second condition (True) is executed
# - else block is skipped
# - Program exits the if-elif-else structure
```

## 2. While Loops

### Basic While Structure
```python
# While loop syntax
while condition:
    # code executed while condition is True
    # make sure condition eventually becomes False
    pass

# Common while loop pattern
counter = 0
while counter < limit:
    # do something
    counter += 1
```

### Example: Factorial Calculation
```python
# Test case 4
i = 1
result = 1
while i <= 10:
    result = result * i
    i += 1
# result will be 3628800 (10!)

# Understanding why:
# - Initial values: i = 1, result = 1
# - First iteration: result = 1 * 1 = 1
# - Second iteration: result = 1 * 2 = 2
# - Third iteration: result = 2 * 3 = 6
# - And so on until i = 10
# - Final result is 10! (10 factorial)
```

## 3. Implementing the Grade Function

### Grade Function Structure
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

# Understanding how it works:
# score = 95 → returns 'A' (95 >= 90)
# score = 85 → returns 'B' (85 >= 80)
# score = 75 → returns 'C' (75 >= 70)
# score = 60 → returns 'F' (60 < 70)
```

## 5. Additional Control Flow Concepts

### Break and Continue
```python
# Break statement exits the loop
i = 1
while True:
    if i > 5:
        break
    i += 1

# Continue statement skips rest of current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4
```

### Nested Control Structures
```python
# Nested if statements
if condition1:
    if condition2:
        # code for both conditions true
    else:
        # code for condition1 true, condition2 false
else:
    # code for condition1 false

# Nested loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1
```

### Boolean Expressions
```python
# Comparison operators
x = 5
x > 3   # True
x >= 5  # True
x < 10  # True
x <= 5  # True
x == 5  # True
x != 3  # True

# Boolean operators
True and True   # True
True or False   # True
not True        # False

# Combined conditions
age = 25
income = 50000
if age >= 21 and income >= 40000:
    print("Qualified")
```

## 6. Common Mistakes to Avoid

1. **Indentation Errors**
```python
# Wrong
if condition:
result = "value"  # IndentationError

# Correct
if condition:
    result = "value"
```

2. **Infinite Loops**
```python
# Wrong
while True:
    print("Infinite")

# Correct
counter = 0
while counter < 5:
    print("Finite")
    counter += 1
```

3. **Forgetting else Cases**
```python
# Incomplete
def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    # Missing lower scores!

# Complete
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'F'
```