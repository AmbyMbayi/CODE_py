"""write a pandas program to create a subtotal os labor hours against msha id from the excel

"""

import pandas as pd 
import numpy as np 

df = pd.read_excel('coalpublic2013.xls')
df_sub = df[["MSHA ID", "Labor Hours"]].groupby('MSHA ID').sum()
print(df_sub)