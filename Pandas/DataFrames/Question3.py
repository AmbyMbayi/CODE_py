"""python pandas program to get the first 3 rows of a given dataframe
"""

import pandas as pd 
import numpy as np 

exam_data = {
    'name':['Joel', 'Amby', 'Moses', 'Cliff'],
    'scores':[12,2,3,5],
    'attempts':[1,2,3,4],
    'qualify':['yes','no','no','yes']
}
labels = ['a','b','c', 'd']

df = pd.DataFrame(exam_data, index=labels)
print("First three rows of the data frame: ")
print(df.iloc[:3])