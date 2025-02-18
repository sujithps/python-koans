## Solving the Test Case

Let's break down the test case and implement the solution:

```python
def multiply_list(numbers, factor):
    """
    Multiply each number in the list by the factor.
    
    Args:
        numbers (list): List of numbers to multiply
        factor (int): Number to multiply by
        
    Returns:
        list: New list with multiplied values
    """
    # Create a new list with multiplied values
    result = []
    for number in numbers:
        result.append(number * factor)
    return result

# Alternative solution using list comprehension
def multiply_list(numbers, factor):
    return [number * factor for number in numbers]
```

### How it Works
1. The function takes two parameters:
   - `numbers`: A list of numbers
   - `factor`: The number to multiply by

2. For each number in the input list:
   - Multiply it by the factor
   - Add it to the result list

3. Return the new list with multiplied values

### Test Cases Explained
```python
input_list = [1, 2, 3, 4]

# Test Case 1
result = multiply_list(input_list, 2)
# [1*2, 2*2, 3*2, 4*2] = [2, 4, 6, 8]

# Test Case 2
result = multiply_list(input_list, 3)
# [1*3, 2*3, 3*3, 4*3] = [3, 6, 9, 12]
```