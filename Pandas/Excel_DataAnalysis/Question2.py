"""write a pandas program to get the data types of the given excel fields"""
import pandas as pd 
import numpy as np 

df = pd.read_excel('coalpublic2013.xls')
print(df.dtypes)