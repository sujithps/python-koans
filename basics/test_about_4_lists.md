# 1. List Basics

### Creating Lists
```python
# Empty list
empty_list = []
empty_list = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']
mixed = [1, 'hello', 3.14, True]  # Lists can contain different types
```

### List Length
```python
numbers = [1, 2, 3, 4, 5]
length = len(numbers)  # 5
```

### Accessing Elements
```python
numbers = [1, 2, 3, 4, 5]

# Positive indexing (starts from 0)
first = numbers[0]   # 1
third = numbers[2]   # 3

# Negative indexing (starts from -1)
last = numbers[-1]   # 5
second_last = numbers[-2]  # 4
```

## 2. List Operations

### Adding Elements
```python
numbers = [1, 2, 3]

# append() - adds single element to end
numbers.append(4)    # [1, 2, 3, 4]

# extend() - adds elements from iterable
numbers.extend([5, 6])   # [1, 2, 3, 4, 5, 6]

# insert() - adds element at specific position
numbers.insert(2, 10)    # [1, 2, 10, 3, 4, 5, 6]
```

### List Slicing
```python
numbers = [1, 2, 3, 4, 5]

# Syntax: list[start:end:step]
# end index is exclusive

numbers[1:4]    # [2, 3, 4]  (elements from index 1 to 3)
numbers[:3]     # [1, 2, 3]  (first three elements)
numbers[2:]     # [3, 4, 5]  (elements from index 2 to end)
numbers[-2:]    # [4, 5]     (last two elements)
numbers[::2]    # [1, 3, 5]  (every second element)
```

### Sorting Lists
```python
numbers = [3, 1, 4, 1, 5]

# Sort in ascending order
numbers.sort()              # [1, 1, 3, 4, 5]

# Sort in descending order
numbers.sort(reverse=True)  # [5, 4, 3, 1, 1]

# Create new sorted list
sorted_numbers = sorted(numbers)  # Original list unchanged
```

## 3. Common List Operations

### Removing Elements
```python
numbers = [1, 2, 3, 4, 5]

# remove() - removes first occurrence of value
numbers.remove(3)    # [1, 2, 4, 5]

# pop() - removes and returns element at index
last = numbers.pop()     # returns 5, list is now [1, 2, 4]
second = numbers.pop(1)  # returns 2, list is now [1, 4]

# del statement - removes element or slice
del numbers[0]      # removes first element
del numbers[1:3]    # removes slice
```

### Finding Elements
```python
numbers = [1, 2, 3, 2, 4]

# index() - finds first occurrence
position = numbers.index(2)    # 1

# count() - counts occurrences
count = numbers.count(2)       # 2

# in operator - checks existence
exists = 3 in numbers          # True
```

### List Manipulation
```python
# Concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2    # [1, 2, 3, 4]

# Repetition
repeated = [1, 2] * 3       # [1, 2, 1, 2, 1, 2]

# Reverse
numbers = [1, 2, 3]
numbers.reverse()           # [3, 2, 1]
reversed_new = numbers[::-1]  # Creates new reversed list
```

## 4. Common Mistakes to Avoid

1. **List Modification During Iteration**
```python
# Wrong
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can skip elements

# Correct
numbers = [num for num in numbers if num % 2 != 0]
```

2. **Copying Lists**
```python
# Wrong (creates reference)
list1 = [1, 2, 3]
list2 = list1  # Changes to list2 affect list1

# Correct (creates copy)
list2 = list1.copy()
list2 = list1[:]
```

3. **Index Out of Range**
```python
numbers = [1, 2, 3]

# Wrong
value = numbers[5]  # IndexError

# Correct
if len(numbers) > 5:
    value = numbers[5]
```

## 5. Practice Exercises

1. Create a function to find unique elements:
```python
def get_unique(lst):
    return list(set(lst))

# Test
numbers = [1, 2, 2, 3, 3, 4]
print(get_unique(numbers))  # [1, 2, 3, 4]
```

2. Create a function to flatten nested list:
```python
def flatten(lst):
    return [item for sublist in lst for item in sublist]

# Test
nested = [[1, 2], [3, 4], [5, 6]]
print(flatten(nested))  # [1, 2, 3, 4, 5, 6]
```

3. Create a function to find common elements:
```python
def find_common(list1, list2):
    return list(set(list1) & set(list2))

# Test
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(find_common(a, b))  # [3, 4]
```