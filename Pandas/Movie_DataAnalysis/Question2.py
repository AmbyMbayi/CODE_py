"""write a pandas program to get the information of the datafreame includeing date type and memory usage.

"""
import pandas as pd 
import numpy as np 
df = pd.read_csv('movies_metadata.csv')
result = df.info()
print("details of the dataframe")
print(result)