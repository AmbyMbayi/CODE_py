"""write a pandas program to pirnt a concise summary of the dataset
"""
import pandas as pd 
import numpy as np 
ds = pd.read_csv('titanic.csv')
result = ds.info()
print(result)