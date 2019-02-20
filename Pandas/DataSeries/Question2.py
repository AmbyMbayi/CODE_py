"""write a pandas program to convert a panda module series to Python list and its type
"""
import pandas as pd 
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas as Series and type ")
print(ds)
print(type(ds))
print("Convert pandas series to python list")
print(ds.tolist())
print(type(ds.tolist()))