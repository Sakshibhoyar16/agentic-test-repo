# API Documentation

## calculator.py
The calculator.py file contains a set of arithmetic functions that can be used to perform basic mathematical operations.

### add(a, b)
#### Description
The `add(a, b)` function takes two numbers as input and returns their sum.
#### Parameters
* `a` (int or float): The first number to be added.
* `b` (int or float): The second number to be added.
#### Returns
* `int or float`: The sum of `a` and `b`.
#### Example
```python
result = add(5, 3)
print(result)  # Output: 8
```

### sub(c, d)
#### Description
The `sub(c, d)` function takes two numbers as input and returns their difference.
#### Parameters
* `c` (int or float): The first number.
* `d` (int or float): The second number to be subtracted from the first.
#### Returns
* `int or float`: The difference between `c` and `d`.
#### Example
```python
result = sub(10, 4)
print(result)  # Output: 6
```

### mul(a, b)
#### Description
The `mul(a, b)` function takes two numbers as input and returns their product.
#### Parameters
* `a` (int or float): The first number to be multiplied.
* `b` (int or float): The second number to be multiplied.
#### Returns
* `int or float`: The product of `a` and `b`.
#### Example
```python
result = mul(5, 6)
print(result)  # Output: 30
```

Since the calculator.py file has more than one function, the execution flow can be represented as follows:
```mermaid
flowchart TD
    A[Start] --> B[add]
    A --> C[sub]
    A --> D[mul]
    B --> E[End]
    C --> E
    D --> E
```