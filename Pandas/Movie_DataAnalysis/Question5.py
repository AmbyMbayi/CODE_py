"""Write a pandas program to get the details of the columns title and generes of the dataframe
"""

import pandas as pd 
import numpy as np 
df = pd.read_csv('movies_metadata.csv')
result=df[['original_title', 'genres']]
print("details of title and genres")
print(result)