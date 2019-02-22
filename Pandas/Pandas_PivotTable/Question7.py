"""write a pandas program to create a pivot table and count the manager wise sale and mean value of sale amount
"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('SaleData.xlsx')
table =pd.pivot_table(df, index=["Manager"], values=["Sale_amt"], aggfunc=[np.mean, len])
print(table)