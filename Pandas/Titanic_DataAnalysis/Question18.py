"""write a pandas program to create a pivot table and separete the 
gender according to whether they traveled alone or not to get the 
probability of survival
"""
import pandas as pd 
import numpy as np 
df = pd.read_csv('titanic.csv')
result = df.pivot_table('survived',['sex', 'alone'], 'class')
print(result)