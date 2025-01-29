import pandas as pd

list1 = [1,2,3,4]
p = pd.Series(list1)
# print(type(p))
# print(p.shape)
# print(p)
print(p.iloc[0:3])

list1 = [1,2,3,4]
# Note that index label can be changed. In Pandas the access method 'loc' access the elements based on the label while the 'iloc' method accesses the elements using actual index values.
p = pd.Series(list1,index=['a','b','c','d']) 
# print(type(p))
# print(p.shape)
# print(p)
print(p.loc['a':'c'])