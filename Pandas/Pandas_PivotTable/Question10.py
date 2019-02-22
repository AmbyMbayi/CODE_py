"""write a pandas program to create a pivot table and dins the maximum sale value of the items

"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index=["Region", "Item"], values="Units")
result=table.query('Item==["Television", "Home Theater"]')
print(result)