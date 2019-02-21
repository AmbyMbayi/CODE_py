"""write a pandas program to get the details of the movie with the title 'Grumpier old men'

"""
import pandas as pd 
df = pd.read_csv('movies_metadata.csv')

df = df.set_index('title')
result = df.loc['Grumpier Old Men']
print("Details of the movie 'Grumpier Old Men")
print(result)