"""Write a pandas program to import excel data into a pandas dataframe and display the last ten rows
"""
import pandas as pd 
import numpy as np 
df = pd.read_excel('coalpublic2013.xls')
print(df.tail(n=10))