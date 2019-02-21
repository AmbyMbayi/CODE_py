"""write a pandas program to import excel data into a datafrema and find a specific MSHA ID
"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('coalpublic2013.xls')
df_id = df[df["MSHA ID"]==100329].head()
print(df_id)
