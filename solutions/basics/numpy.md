# Solving the Test Cases

Let's solve each test case:

```python
def test_numpy_basics(self):
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    
    # 1. Array addition
    self.assertTrue(np.array_equal([5, 7, 9], array1 + array2))
    
    # 2. Scalar multiplication
    self.assertTrue(np.array_equal([2, 4, 6], array1 * 2))
    
    # 3. Mean calculation
    self.assertEqual(2.0, np.mean(array1))
    
    # 4. Sum calculation
    self.assertEqual(15, np.sum(array2))
```
