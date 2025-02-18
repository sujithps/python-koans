# Pandas Basics: A Comprehensive Guide

## 1. Introduction to Pandas

### What is Pandas?
Pandas is a powerful data manipulation and analysis library for Python. It provides:
- DataFrame objects (2-dimensional data)
- Series objects (1-dimensional data)
- Tools for reading/writing data
- Data alignment and manipulation functions

### Use cases

- Data analysis
- Data cleaning
- Data visualization
- Time series analysis
- Database-style operations

### Installing Pandas
```python
# Using pip
pip install pandas

# Import in your code
import pandas as pd
```

## Understanding DataFrame Structure
### Anatomy of a DataFrame
```python data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'San Francisco', 'Chicago']
}
df = pd.DataFrame(data)

# Components:
# 1. Index (row labels)
# 2. Columns (column labels)
# 3. Data (actual values)
# 4. dtypes (data types of columns)

print(df)
#       name  age           city
# 0    Alice   25      New York  ← Row with index 0
# 1      Bob   30  San Francisco ← Row with index 1
# 2  Charlie   35       Chicago  ← Row with index 2
#     ↑        ↑          ↑
#   Column   Column    Column
```

### Index Deep Dive

```python # Default numeric index
df = pd.DataFrame(data)  # Index: 0, 1, 2

# Custom index
df = pd.DataFrame(data, index=['p1', 'p2', 'p3'])

# Access index properties
index_values = df.index.values  # Array of index values
is_unique = df.index.is_unique  # Check if index is unique
index_type = df.index.dtype    # Data type of index

# Reset index
df_reset = df.reset_index()    # Makes current index a column
df_reset = df.reset_index(drop=True)  # Drops current index
``` 

## 2. Creating DataFrames

### From Dictionary
```python
# Dictionary with lists
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'San Francisco', 'Chicago']
}

# Create DataFrame
df = pd.DataFrame(data)

# Result:
#       name  age           city
# 0    Alice   25      New York
# 1      Bob   30  San Francisco
# 2  Charlie   35       Chicago
```

### From Lists
```python
# List of lists
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Chicago']
]

# Create DataFrame with column names
df = pd.DataFrame(data, columns=['name', 'age', 'city'])
```

## 3. Basic DataFrame Operations

### Accessing Data
```python
# Get number of rows
length = len(df)         # 3

# Get column names
columns = df.columns     # Index(['name', 'age', 'city'], dtype='object')
columns_list = list(df.columns)  # ['name', 'age', 'city']

# Access single column (returns Series)
ages = df['age']        # Series with age values
names = df['name']      # Series with name values

# Access multiple columns
subset = df[['name', 'age']]  # DataFrame with selected columns
```

### Statistical Operations
```python
# Mean of numeric column
age_mean = df['age'].mean()    # 30.0
# Step by step:
# 1. Get ages: [25, 30, 35]
# 2. Calculate mean: (25 + 30 + 35) / 3 = 30.0

# Other statistical functions
age_max = df['age'].max()      # 35
age_min = df['age'].min()      # 25
age_sum = df['age'].sum()      # 90
age_std = df['age'].std()      # Standard deviation
```

## 5. DataFrame Properties and Methods

### Basic Properties
```python
# Shape (rows, columns)
shape = df.shape        # (3, 3)

# Data types of columns
dtypes = df.dtypes     # Shows type of each column

# Basic information
info = df.info()       # Shows DataFrame info

# Summary statistics
stats = df.describe()  # Statistical summary of numeric columns
```

### Common Methods
```python
# First n rows
head = df.head(2)      # First 2 rows

# Last n rows
tail = df.tail(2)      # Last 2 rows

# Check for null values
nulls = df.isnull()    # Boolean DataFrame showing null values
null_sum = df.isnull().sum()  # Count of nulls per column
```

## 6. Data Selection and Filtering

### Selecting Data
```python
# Select by labels
row = df.loc[0]        # First row as Series
subset = df.loc[0:2]   # Rows 0 to 2 as DataFrame

# Select by position
row = df.iloc[0]       # First row as Series
subset = df.iloc[0:2]  # First two rows as DataFrame
```

### Filtering Data
```python
# Filter by condition
adults = df[df['age'] >= 30]
# Result:
#       name  age           city
# 1      Bob   30  San Francisco
# 2  Charlie   35       Chicago

# Multiple conditions
filtered = df[(df['age'] >= 30) & (df['city'] == 'Chicago')]
# Result:
#       name  age     city
# 2  Charlie   35  Chicago
```

## 7. Data Modification

### Adding Columns
```python
# Add single column
df['salary'] = [50000, 60000, 70000]

# Add calculated column
df['age_plus_10'] = df['age'] + 10
```

### Modifying Data
```python
# Update single value
df.loc[0, 'age'] = 26

# Update column
df['age'] = df['age'] + 1

# Update based on condition
df.loc[df['age'] > 30, 'status'] = 'Senior'
```

## 8. Best Practices

### 1. Check Data Types
```python
# Verify data types
print(df.dtypes)

# Convert types if needed
df['age'] = df['age'].astype(int)
```

### 2. Handle Missing Data
```python
# Check for missing values
print(df.isnull().sum())

# Fill missing values
df['age'].fillna(df['age'].mean(), inplace=True)
```

### 3. Use Method Chaining
```python
# Chain operations
result = (df
          .sort_values('age')
          .reset_index(drop=True)
          .head(2))
```

## 9. Common Pandas Operations

### Sorting
```python
# Sort by one column
sorted_df = df.sort_values('age')

# Sort by multiple columns
sorted_df = df.sort_values(['age', 'name'])

# Sort in descending order
sorted_df = df.sort_values('age', ascending=False)
```

### Grouping
```python
# Group by single column
grouped = df.groupby('city')

# Calculate group statistics
city_means = df.groupby('city')['age'].mean()
```