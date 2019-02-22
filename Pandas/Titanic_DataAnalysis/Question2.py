"""write a pandas program to extract the column labels shape and data types of the dataset

"""
import pandas as pd 
import numpy as np
df = pd.read_csv('titanic.csv')
print("List of columns: ")
print(df.columns)
print("\nShape of the dataset: ")
print(df.shape)
print("\nData types of the dataset")
print(df.dtypes)
