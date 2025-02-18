# Understanding Assertions in Python

### What are Assertions?
Assertions are statements that check if a condition is True. If the condition is False, an AssertionError is raised.

```python
# Basic assertion syntax
assert condition, "Optional error message"

# Example
x = 5
assert x > 0, "x should be positive"
```

## 2. Python Unit Testing with unittest

### Basic Concepts

1. **Test Case**: A class that inherits from `unittest.TestCase`
2. **Test Methods**: Methods that start with `test_`
3. **Assertions**: Methods to check if conditions are met

### Common Assertion Methods

```python
# 1. assertTrue() - Checks if condition is True
self.assertTrue(1 < 2)  # Passes
self.assertTrue(1 > 2)  # Fails

# 2. assertEqual() - Checks if two values are equal
self.assertEqual(1 + 1, 2)  # Passes
self.assertEqual(1 + 1, 3)  # Fails

# 3. assertFalse() - Checks if condition is False
self.assertFalse(1 > 2)  # Passes
self.assertFalse(1 < 2)  # Fails
```

## 3. Additional Tips

1. **assertTrue vs assertEqual**
   - `assertTrue` checks if a condition is True
   - `assertEqual` compares two values for equality
   - `assertEqual` provides better error messages when tests fail

2. **Running the Tests**
```bash
# From command line
python -m unittest test_about_0_assertions.py

# Or run specific test
python -m unittest test_about_0_assertions.py -k test_assert_truth
```

3. **Understanding Error Messages**
When a test fails, you'll see:
- The name of the failing test
- The assertion that failed
- Expected vs actual values
- Line number where the failure occurred

4. **Best Practices**
- Use descriptive test names
- Include meaningful error messages
- Use `assertEqual` instead of `assertTrue` for equality comparisons
- Keep tests focused and simple