"""sort the data frame bsed on release date
"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
small_df=df[['title', 'release_date']]
result = small_df.sort_values('release_date')
print("DataFrame based on release date: ")
print(result)