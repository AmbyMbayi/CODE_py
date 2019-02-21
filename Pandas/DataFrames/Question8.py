"""write a pandas program tha select the rows where ther score is missing
i.e is NaN 
"""

import pandas as pd 
import numpy as np 

exam_data ={
    'name':['Joel', 'Amby','Cliff','Moses'],
    'score':[1,np.nan,3,np.nan],
    'attempts':['yes','no','yes','yes'],
    'qualify':['yes','no','yes','yes']

}
labels = ['a','b','c','d']

df = pd.DataFrame(exam_data, index=labels)
print("rows where score is missing")
print(df[df['score'].isnull()])
