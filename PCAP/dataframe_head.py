import pandas as pd
from pandas import DataFrame as df

dict1 = {'a':[1,2,3],'b':[4,5,6],'c':[1,2,4],'d':[2,2,2],'e':[3,3,4],'f':[4,1,1],'g':[9,1,1],'h':[0,1,1]}
df = pd.DataFrame(dict1)

print(df.head())
