"""Write a pandas program to create a pivot table and find the region wise total sale
"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index="Region", values="Sale_amt", aggfunc= np.sum)
print(table)