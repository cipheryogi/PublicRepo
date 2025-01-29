# import math

# def fibonacci_binet_formula(n):
#     phi = (1 + math.sqrt(5)) / 2
#     return round((phi ** n - (-phi) ** (-n)) / math.sqrt(5))

# # Example usage
# n = 10
# result = fibonacci_binet_formula(n)
# print(f"The {n}th Fibonacci number is: {result}")

# Python 3: Fibonacci series up to n
# def fib(n):
#      a, b = 0, 1
#      while a < n:
#          print(a, end=' ')
#          a, b = b, a+b
#      print()
# fib(1000)

def fibo(n):
    tup0 = (0, 1)
    i = 0
    j = 1
    count = 2  # We start with 2 numbers in the tuple (0 and 1)

    while count < n:
        next_num = tup0[i] + tup0[j]
        print(next_num)
        tup0 = tup0 + (next_num,)  # Add the next Fibonacci number to the tuple
        i += 1
        j += 1
        count += 1

fibo(10)  # Call the function with the desired number of Fibonacci numbers

     