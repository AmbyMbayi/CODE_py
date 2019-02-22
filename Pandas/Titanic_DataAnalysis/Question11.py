"""write a pandas program to create a pivot table and calculate number of women and men were in 
a particular cabin class
"""
import pandas as pd 
import numpy as np 
df = pd.read_csv('titanic.csv')
result = df.pivot_table(index=['sex'], columns=['pclass'], aggfunc='count')
print(result)