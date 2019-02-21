"""Write a pandas program to get the details of the third movie of the data frame"""
import pandas as pd 
df= pd.read_csv('movies_metadata.csv')
third_movie = df.iloc[2]
print("details of the third movie")
print(third_movie)