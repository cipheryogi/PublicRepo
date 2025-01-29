'''Let's write a simple function that will help organise lotteries. The function will generate a list of random numbers (to simulate lottery tickets), and it will also choose one number from the generated list (to simulate the winning ticket).

Write a function named generate_tickets that will accept two integer arguments: ticket_count and max_number. The function should return a tuple with exactly two elements:

first element: a list of random unique integer numbers in the range from 0 (inclusive) to max_number (exclusive); the number of elements is provided in the ticket_count argument

second element: one random element from the generated list of numbers

Calling generate_tickets(5, 10) should generate 5 random unique integers in the range from 0 (inclusive) to 10 (exclusive). An example return value for this invocation could be:

([2, 8, 9, 3, 0], 8)

In this case, the random numbers are: 2, 8, 9, 3, 0. The winning number is 8.

Note: You can assume that the arguments of the function are always correct (i.e. you always get two correct integers as the input arguments).'''

import random
 
def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return (list_to_return, random.sample(list_to_return, 1)[0])

x,y = generate_tickets(5,10)
print(x,y)