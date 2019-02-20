"""write a pandas program to add, subtract, multiply and divide two pandas
"""

import pandas as pd 
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])

ds = ds1+ds2
print("Add two series ")
print(ds)

print("Substract two series")
ds = ds1-ds2
print(ds)

print("multiply two series")
ds = ds1*ds2
print(ds)