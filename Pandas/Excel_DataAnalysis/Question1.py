"""write a pandas program to import excel data into pandas dataframe 
"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('coalpublic2013.xls')
print(df.head)