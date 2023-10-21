def factorial(n):
    lst = []
    result = 1
    for el in range(1,n+1):
        lst.append(el)
        result *= el
        print(result,lst)
        # return result

try:
    factorial(9)
except ValueError: 
    print("Exceeds the limit (4300 digits) for integer string conversion. ",ValueError)
finally:
    print("Factorial calculated successfully!")