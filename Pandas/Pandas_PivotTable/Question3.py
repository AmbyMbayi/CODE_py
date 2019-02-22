"""write a pandas program to create a pivot table and find the total sale amount region wise
manger wise, sales man wise
"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('SaleData.xlsx')
df_result =pd.pivot_table(df, index=["Region", "Manager", "SalesMan"], values="Sale_amt")
print(df_result)