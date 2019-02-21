"""
write pandas program to select the specifed columns and rows from a given dataframe
"""

import pandas as pd 
import numpy as np 

exam_data = {
    'name':['Amby', 'Joel','Cliff', 'Moses'],
    'score':[12,23,34,45],
    'attempts':[1,2,3,4],
    'qualify':['me','no','yes','non']
}
labels = ['a','b','c','d']

df = pd.DataFrame(exam_data, index=labels)
print("Select specific rows and column")
print(df.iloc[[0,1,3],[0,1,3]])