"""write a pandas program to get the longest runtime and shortest runtime
"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'runtime']]
run_time = small_df['runtime']
print(small_df)
print("===================")
print("Longest runtime")
print(run_time.max())
print("Shortest runtime")
print(run_time.min())