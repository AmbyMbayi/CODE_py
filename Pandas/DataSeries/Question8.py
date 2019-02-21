"""pytho pandas to convert the first column of a data series
"""
import pandas as pd 
d = {'col1':[1,2,3,4,5,6,7], 'col2':[4,5,6,9,1,4,3], 'col3':[9,7,5,8,12,1,11]}
df = pd.DataFrame(data=d)
print("original DataFrame")
print(df)
s1 = df.ix[:,0]
print("\n1st column as a Series: ")
print(s1)
print(type(type(s1)))