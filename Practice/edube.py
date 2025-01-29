# dictionary = {'one':'two','three':'one','two':'three'}

# v = dictionary['one']

# for k in range(3):
#     v = dictionary[v]
# print(v)


# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i],)

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0],type(k))

tup = (1,2,4,8)
print(type(tup))
tup = tup[1:-1]
print(type(tup))
tup = tup[0] # due to this assignment the type of variable tup changed from Tuple to Int. If we want to maintain it as Tuple then it should given as a slice i.e., tup = [0:1]
print(type(tup))
print(tup)

# def fun(x,y,z):
#     return x + 2 * y + 3 * z
# print(fun(0,z=1,y=3))  

# print(Hello world!) #syntaxerror execption

# lst = [[x for x in range(3)] for y in range(3)]
# print(lst)

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print('#',r,c)

# following will cause syntax errro because break is used outside the loop  (without loop). And not zerodivision
# try:
#     print(5/0)
#     break
# except:
#     print('xyz')
# except (ValueError, ZeroDivisionError):
#     print('err')

# # following will give value error as the index(x) returns the index of the given value of x in the tuple. In this case 0 is not a value in the tuple
# foo = (1,2,3)
# print(foo.index(0))

#  following prints 21 and (2,1). Note that by using [][] we are accessing individual elements of the tuples which are in turn the elements of the list
# dct = {}
# dct['1'] = (1,2)
# dct['2'] = (2,1)
# for x in dct.keys():
#     print(dct[x][1],end='')

# Note that insert() function inserts the value 'before' the given index
# mlst = [1,2]
# for v in range(2):
#     mlst.insert(-1,mlst[v])
# print(mlst)
