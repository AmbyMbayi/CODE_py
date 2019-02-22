"""write a pandas program to create a pivot table with multiple indexes from a given excel sheet
"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('SaleData.xlsx')
print(df)
print("the pivot table is shown as: ")
pivot_result = pd.pivot_table(df, index=["Region", "SalesMan"])
print(pivot_result)