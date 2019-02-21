"""write a pandas program to get those movies whose reveune more that 2mil and spent less than 1 mi

"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'release_date', 'budget', 'revenue']]
result = small_df[ (small_df['budget'] < 1000000)]
print("movies ")
print(result.head())