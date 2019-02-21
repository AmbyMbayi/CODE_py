"""write a pandas program to create a smaller dataframe with a subset of all features
"""
import pandas as pd 

df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'release_date','budget', 'revenue', 'runtime']]
print("smaller DataFrame")
print(small_df.head())