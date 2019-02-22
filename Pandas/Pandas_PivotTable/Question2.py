"""Write a pandas program to create a pivot table and find the total sale amount region wise, 
manager wise
"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('SaleData.xlsx')
df_result= pd.pivot_table(df,index = ["Region", "Manager"], values =["Sale_amt"], aggfunc=np.sum)
print(df_result)