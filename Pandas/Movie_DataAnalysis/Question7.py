"""Write a pandas program to get the details of the fifth movie of the dataframe
"""

import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
result = df.iloc[4]
print("details of the fifth movie of the DataFrame:")
print(result)