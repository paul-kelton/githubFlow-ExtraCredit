# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    return a / b  # Potential division by zero error

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")
    print(f"The result of addition is: {add_numbers(x, y)}")
