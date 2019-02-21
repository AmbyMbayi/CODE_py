"""Write a pandas program to count the number of rows and columns of the dataframe
"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
result = df.shape
print("Number of rows and columns of the dataframe")
print(result)