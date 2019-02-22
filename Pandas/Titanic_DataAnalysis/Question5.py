"""write a pandas program tocreate a pivot table and find survival rate by gender age wise of various classes
"""
import pandas as pd 
import numpy as np 

df = pd.read_csv('titanic.csv')
result = df.groupby('sex')[['survived']].mean()
print(result)