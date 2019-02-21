"""write pandas program to select the rows where the number of attempts in the
examination is greater than 2"""

import pandas as pd 
import numpy as np 

exam_data ={
    'name':['Amby','Joel','Cliff', 'Moses'],
    'score':[1,2,3,4],
    'attempts':[2,3,5,6],
    'qualify':['yes','no','no','yes']

}
labels = ['a','b','c','d']

df = pd.DataFrame(exam_data, index=labels)
print("Select specific columnts and rows")
print(df.ix[[1,2,3],['name','score']])