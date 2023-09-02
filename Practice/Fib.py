import math

def fibonacci_binet_formula(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi ** n - (-phi) ** (-n)) / math.sqrt(5))

# Example usage
n = 10
result = fibonacci_binet_formula(n)
print(f"The {n}th Fibonacci number is: {result}")
