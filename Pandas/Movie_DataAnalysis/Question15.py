"""Write a pandas program to compute the calculate the number of votes garnered by the 70% movie
"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
small_df = df['vote_count'].quantile(0.70)
print(small_df)