"""Write a pandas program to display the first 10rows of the dataframe
"""

import pandas as pd
df = pd.read_csv('movies_metadata.csv')
result=df.head(10)
print("first 10 rows of the dataframe")
print(result)