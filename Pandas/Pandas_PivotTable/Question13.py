"""write a pandas program to create a pivot table and find the minimum sale value of the items
"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=[np.max, np.min])
print(table)