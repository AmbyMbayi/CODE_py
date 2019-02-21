"""Write a pandas program to convert series of lists to one series
"""
import pandas as pd 
s=pd.Series([
    ['red', 'green', 'white'],
    ['red', 'black'],
    ['yellow']
])
print("original series of list: ")
print(s)

S = s.apply(pd.Series). stack().reset_index(drop =True)
print("one series")
print(S)