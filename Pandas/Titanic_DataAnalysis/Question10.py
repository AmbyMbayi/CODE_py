"""Write a pandas program to create a pivot table and find survival rate by gender,
age of the different categories of various classes
Add the fare as a dimension of columns and partition fare column into 2 categories based on the 
values present in fare columns.

"""
import pandas as pd 
import numpy as np 
df = pd.read_csv('titanic.csv')
fare = pd.qcut(df['fare'],2)
age = pd.cut(df['age'],[0,10,30,60,80])
result = df.pivot_table('survived', index=['sex', age], columns=[fare, 'pclass'])
print(result)