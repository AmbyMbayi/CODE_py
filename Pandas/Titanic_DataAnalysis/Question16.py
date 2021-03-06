"""write a pandas program to create a pivot table and find number of 
adult male, adult female and children
"""
import pandas as pd 
import numpy as np 
df= pd.read_csv('titanic.csv')
result = df.pivot_table(index = 'sex', columns ='class', aggfunc ={'survived':sum, 'fare':'mean'})
print(result)