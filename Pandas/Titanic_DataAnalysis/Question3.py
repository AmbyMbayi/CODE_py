"""write a pandas program to create apivot table with multiple indexes from the dataset of 
titanic.csv
"""
import pandas as pd 
import numpy as np 
df=pd.read_csv('titanic.csv')
result = pd.pivot_table(df, index=["sex","age"], aggfunc=np.sum)
print(result)