"""write a pandas program to change the score in row 'd' to 11.5

"""

import pandas as pd 
import numpy as np 

exam_data = {
    'name':['Amby','Mbayi','Joel','Nyaribo'],
    'score':[1,2,3,4],
    'attempts':[1,2,3,4],
    'qualify':['yes','yes','no','no']
}
labels = ['a','b','c','d']

df = pd.DataFrame(exam_data, index=labels)
print("original data frame")
print(df)
print("change score in row 'd' to 11.5")
df.loc['d', 'score']=11.5
print(df)
