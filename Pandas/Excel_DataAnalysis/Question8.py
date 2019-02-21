"""Write a pandas program to add summation to a row of the given excel file"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('coalpublic2013.xls')
sum_row = df[["Production (short tons)", "Labor Hours"]].sum()
df_sum=pd.DataFrame(data=sum_row).T
df_sum = df_sum.reindex(columns=df.columns)
print(df_sum)