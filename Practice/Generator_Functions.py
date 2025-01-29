# # In Python, a generator function is a special type of function that returns an iterator, which can be used to iterate over a sequence of values. Unlike regular functions that return a value and then terminate, generator functions can suspend and resume their execution, allowing them to produce a sequence of values over time.
# Generator functions are defined using the yield keyword instead of the return keyword. When a generator function is called, it returns a generator object, which can be iterated over using a loop or other iterator-consuming functions.
def number_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1
# Using the generator function
my_generator = number_generator(5)
for num in my_generator:
    print(num)
# notice that without a generator function we would have to use the "next(object)" keyword to move to the next value. Since the generator function retains the 'state' of the variables, the manipulation becomes easier by using a just a loop. Note that 'return' function destroys the 'state' of the variables before passing the control back to the calling program. This is where the yield keyword is useful.
 
