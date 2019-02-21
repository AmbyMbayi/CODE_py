"""write a pandas program to import excel data skipping first rows into a pandas dataframe
"""

import pandas as pd 
import numpy as np 

df = pd.read_excel('coalpublic2013.xls', skiprows = 1220)
print(df)
