# Note that Lambda functions can be used only for single expression (as shown in the example below). A lambda function, also known as an anonymous function, is a way to define a small, one-line function without a formal def statement. It is typically used for simple, one-off operations. The syntax of a lambda function is as follows: lambda arguments: expression
# Lambda function
multiply = lambda x, y: x * y # note: single expression i.e., x * y. No other calculation.
print(multiply(3, 5))  # Output: 15

# Regular function
def multiply(x, y):
    result = x * y
    return result

print(multiply(3, 5))  # Output: 15
