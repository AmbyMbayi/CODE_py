"""write a pandas program to create a pivot table and compute suvival totals of all
classes along each group
"""
import pandas as pd 
import numpy as np 
df = pd.read_csv('titanic.csv')
result = df.pivot_table('survived', index='sex', columns='class', margins=True)
print(result)