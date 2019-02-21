"""write a pandas program toa ccess those moves, released after 1995-10-10
"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
small_df=df[['title', 'release_date']]
result = small_df[small_df['release_date']> '1995-01-01']
print("DataFrame based on release date > 1995-01-01")
print(result)