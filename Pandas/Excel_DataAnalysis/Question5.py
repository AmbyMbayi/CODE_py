"""Write a pandas program to insert a column in the sixth position of the said excel sheet and fill it with NaN values
"""

import pandas as pd 
import numpy as np 

df = pd.read_excel('coalpublic2013.xls')
df.insert(3, "column1", np.nan)
print(df.head)