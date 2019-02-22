"""wrie a pandas program to display the movies(title, runtime) longer than 30mins and shorter than 360minutes
"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
small_df = df[['title','runtime']]
result = small_df[(small_df['runtime']>=30) & (small_df['runtime']<=360)]
print("List of movies longer than 30minutes and shorter than 360minutes: ")

print(result)