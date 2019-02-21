"""write a pandas program to read specific columns form a given excel file"""

import pandas as pd
import numpy as np 

cols = [0,1,2,4]
df = pd.read_excel('coalpublic2013.xls', usecols=cols)
print(df)