"""pandas program to selct the rows the score is between 15 and 20(inclusive)
"""

import pandas as pd 
import numpy as np 

exam_data={
    'name':['Joel','Amby','Moses','Cliff'],
    'score':[16,3,20,15],
    'attempts':[1,2,3,4],
    'qualify':['yes','no','yes','yes']

}
labels = ['a','b', 'c', 'd']

df = pd.DataFrame(exam_data, index =labels)
print("Rows where score is between 15 and 20(inclusive): ")
print(df[df['score'].between(15,20)])