"""Write a python program to convert a given series to an array"""
import pandas as pd 
import numpy as np 

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("original data series ")
print(s1)
print("Series to an array")
a = np.array(s1.values.tolist())
print(a)
