"""write a pandas program to compare the elements of the two pandas series
"""
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])

print("Series1: ")
print(ds1)
print("Series2: ")
print(ds2)
print("Compare the elements of the said Series: ")
print(ds1==ds2)
print("Greater than: ")
print(ds1 > ds2)
print("less than: ")
print(ds1 < ds2)