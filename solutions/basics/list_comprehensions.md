# Solving the Test Cases

Let's solve each test case:

```python
def test_list_comprehensions(self):
    numbers = [1, 2, 3, 4, 5]
    
    # 1. Create list of squares
    squares = [num ** 2 for num in numbers]
    self.assertEqual([1, 4, 9, 16, 25], squares)
    
    # 2. Filter even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    self.assertEqual([2, 4], even_numbers)
    
    # 3. Filter long words
    words = ['hello', 'world', 'python', 'ai']
    long_words = [word for word in words if len(word) > 4]
    self.assertEqual(['hello', 'python'], long_words)
```
