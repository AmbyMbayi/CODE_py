"""write a pandas program to create apivot table and find the total sale amount regionwise,
manager wise. sales man wise where Manager="Douglas"

"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index=["Region","Manager","SalesMan"], values="Sale_amt")
result=table.query('Manager==["Douglas"]')
print(result)