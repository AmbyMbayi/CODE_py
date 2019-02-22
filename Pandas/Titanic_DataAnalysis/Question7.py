"""write a pandas program to partition each of the passangers into four categories based on their ages

NOte age categories(0,10),(10,30),(30,60)(60,80)
"""
import pandas as pd 
import numpy as np 
df = pd.read_csv('titanic.csv')
result = pd.cut(df['age'],[0,10,30,60,80])
print(result)