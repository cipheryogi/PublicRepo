x = 123
 
def sum_of_digits(y):
   sum = 0
   while (y != 0):
       sum = sum + int(y % 10)
       y = int(y / 10)
   print(sum)
 
sum_of_digits(x)