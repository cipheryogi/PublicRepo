import numpy as np
x = [1,-2]
y = [2,2]
# normal prodct
print(np.array(x) * np.array(y))

'''dot product - The dot product takes two vectors and returns a scalar value. It's calculated by multiplying corresponding entries of the vectors and then summing those products. The result is a single scalar value. 
'''
print(np.dot(np.array([1,-1]),np.array([1,1]))) #output will be 0

A = np.array([[1,2,3],[3,4,7],[5,6,7],[7,8,7]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.dot(A,B))
