"""write a pandas program to convert a dictionary to a pandas series
"""
import pandas as pd 
d1 = {'a':100, 'b':200, 'c':300, 'd':400, 'e':800}
print("original dictionary")
print(d1)
new_series = pd.Series(d1)
print("converted series: ")
print(new_series)

