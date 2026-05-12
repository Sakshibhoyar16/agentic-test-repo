def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtracts b from a and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b
def divide(a, b):
    """Divides a by b and returns the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Raises base to the power of exponent."""
    return base ** exponent