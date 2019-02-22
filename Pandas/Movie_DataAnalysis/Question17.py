"""write a pandas program to display the movies(title, number of votes) that received specified number
of votes
"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
n =500
small_df = df[['title', 'vote_count']]
result = small_df[small_df['vote_count']>=n]
print("List of movies longer than 30mins and shorter than 360 mins")
print(result)