"""Write a pandas program tocreate a pivot table and find the maximum sale value of the items
"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index='Item', values='Sale_amt')
print(table)