"""write a pandas program to get the columns of the DataFrame
"""
import pandas as pd 
import numpy as np 

df = pd.read_csv('movies_metadata.csv', error_bad_lines=False)
print("columns of the dataframe")
print(df.columns)