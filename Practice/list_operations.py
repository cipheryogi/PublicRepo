list = [[2-i for i in range(2)] for j in range(2)]
 
var = 0
for i in range(2):
      var += list[i][i]
print(var)

# example 2
list = [[1, 2, 3]]
result = 1
 
for i in range(1):
   result *= 10
   for j in range(1):
       list[i][j] *= result
 
print(list)

# example 3 

lst = [1, 5, 10, 15, 20]
print(lst[::-1])