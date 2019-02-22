"""write a pandas program to create a pivot table and find survival rate by gender, age wise of various classes
"""
import pandas as pd 
import numpy as np 
df = pd.read_csv('titanic.csv')
result = df.pivot_table('survived', index=['sex', 'age'], columns='class')
print(result)