# 1. String Creation and Basics

### Ways to Create Strings
```python
# Single quotes
name = 'Python'

# Double quotes
name = "Python"

# Triple quotes (for multi-line)
description = '''This is a
multi-line string'''

# Triple double quotes
description = """Also works
for multiple lines"""
```

### String Characters
```python
# Each character in a string has an index
text = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5    (positive indexing)
#      -6 -5 -4 -3 -2 -1    (negative indexing)

# Accessing characters
first = text[0]     # 'P'
last = text[-1]     # 'n'
middle = text[2]    # 't'
```

## 2. String Operations

### Concatenation (Joining Strings)
```python
# Using + operator
first = "Hello"
second = "World"
message = first + " " + second    # "Hello World"

# Using join method
words = ['Hello', 'World']
message = ' '.join(words)         # "Hello World"

# Using f-strings (Python 3.6+)
name = "World"
message = f"Hello {name}"         # "Hello World"

# Using format method
message = "Hello {}".format("World")  # "Hello World"
```

### String Slicing
```python
text = "Python Programming"

# Basic slicing: text[start:end:step]
# start: inclusive
# end: exclusive
# step: how many characters to skip

# Examples
text[0:6]      # "Python" (first 6 characters)
text[7:]       # "Programming" (from index 7 to end)
text[:6]       # "Python" (from start to index 6)
text[::2]      # "Pto rgamn" (every second character)
text[::-1]     # "gnimmargorP nohtyP" (reverse string)

# Negative indices
text[-11:]     # "Programming" (last 11 characters)
text[:-12]     # "Python" (everything except last 12 characters)
```

## 3. String Methods

### Case Methods
```python
text = "Python Programming"

# Converting case
text.upper()       # "PYTHON PROGRAMMING"
text.lower()       # "python programming"
text.capitalize()  # "Python programming"
text.title()       # "Python Programming"
text.swapcase()    # "pYTHON pROGRAMMING"

# Checking case
text.isupper()     # False
text.islower()     # False
text.istitle()     # True
```

### Search Methods
```python
text = "Python Programming"

# Finding substrings
text.find('Pro')       # 7 (returns index, -1 if not found)
text.index('Pro')      # 7 (returns index, raises error if not found)
text.rfind('m')        # 15 (searches from right)
text.count('m')        # 2 (counts occurrences)

# Checking content
text.startswith('Py')  # True
text.endswith('ing')   # True
'Pro' in text          # True

# Finding all occurrences
import re
[m.start() for m in re.finditer('m', text)]  # [14, 15]
```

### Modification Methods
```python
text = "  Python Programming  "

# Removing whitespace
text.strip()       # "Python Programming"
text.lstrip()      # "Python Programming  "
text.rstrip()      # "  Python Programming"

# Replacing content
text.replace('Python', 'Java')  # "  Java Programming  "
text.replace('m', 'M', 1)      # "  Python PrograMming  "

# Splitting and joining
text.split()       # ['Python', 'Programming']
text.split('m')    # ['  Python Progra', '', 'ing  ']
'-'.join(['Python', 'Programming'])  # "Python-Programming"
```

### Validation Methods
```python
# Checking string content
"123".isdigit()      # True (only digits)
"abc".isalpha()      # True (only letters)
"abc123".isalnum()   # True (letters or numbers)
"   ".isspace()      # True (only whitespace)
```

## 4. String Formatting

### F-strings (Python 3.6+)
```python
name = "Alice"
age = 25
height = 1.75

# Basic formatting
print(f"Name: {name}, Age: {age}")  # "Name: Alice, Age: 25"

# With expressions
print(f"Next year: {age + 1}")      # "Next year: 26"

# Number formatting
print(f"Height: {height:.2f}m")     # "Height: 1.75m"
```

### Format Method
```python
# Basic formatting
"Hello, {}".format("World")     # "Hello, World"

# Multiple values
"{} is {} years old".format("Bob", 25)  # "Bob is 25 years old"

# Named placeholders
"{name} is {age}".format(name="Charlie", age=30)

# Number formatting
"Price: {:.2f}".format(49.9999)  # "Price: 50.00"
```

## 5. Special Characters

### Escape Characters
```python
# \n - newline
print("Line 1\nLine 2")

# \t - tab
print("Name:\tJohn")

# \\ - backslash
print("Path: C:\\Users\\John")

# \' and \" - quotes
print('It\'s a nice day')
print("He said \"Hello\"")
```

## 6. Common Operations and Patterns

### String Reversal
```python
# Using slicing
text = "Python"
reversed = text[::-1]    # "nohtyP"

# Using reversed function
reversed = ''.join(reversed(text))  # "nohtyP"
```

### Checking Palindrome
```python
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("A man a plan a canal Panama"))  # True
```

### Counting Characters
```python
from collections import Counter

text = "programming"
# Count all characters
char_count = Counter(text)
print(char_count)  # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

# Count specific character
print(text.count('m'))  # 2
```

## 7. Best Practices

1. **String Concatenation**
```python
# Bad (slow for many strings)
result = ""
for i in range(100):
    result += str(i)

# Good (more efficient)
result = ''.join(str(i) for i in range(100))
```

2. **String Comparison**
```python
# Case-sensitive comparison
"Python" == "python"  # False

# Case-insensitive comparison
"Python".lower() == "python".lower()  # True
```

3. **Checking String Content**
```python
# Bad
if text.find('Python') != -1:
    print("Found")

# Good
if 'Python' in text:
    print("Found")
```