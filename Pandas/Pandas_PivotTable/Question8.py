"""Write a pandas program to create pivot table and find manager wise, saleman wise total sale and also
display the sum of all sale amount at the bottm
"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index=["Manager", "SalesMan"], values=["Units", "Sale_amt"],aggfunc =[np.sum], fill_value=0, margins=True)
print(table)
