"""write a python pandas program to sort movies on runtime in descending order

"""

import pandas as pd 
df = pd.read_csv('movies_metadata.csv')
small_df =df[['title','runtime']]
result = small_df.sort_values('runtime', ascending=False)
print(result.head())