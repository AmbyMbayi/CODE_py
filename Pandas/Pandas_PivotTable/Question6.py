"""write a pandas program to create a pivot table and find the region wise item unit sold
"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index=["Region","Item"], values ="Units")
print(table)
