"""wirte a pandas program to create a pivot table and find the item wise unit sold
"""
import pandas as pd 
import numpy as np 

df= pd.read_excel('SaleData.xlsx')
df_result = pd.pivot_table(df, index=["Item"], values="Units")
print(df_result)