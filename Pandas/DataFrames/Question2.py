"""write a python program to create and display a DataFrame from a specified dictionary data which has the index labels"""

import pandas as pd 
import numpy as np 

exam_data = {'name': ['Amby', 'Odhiambo', 'Moses'],
             'score':[10,12,21],
             'attempts':[1,3,4],
             'qualify':['yes', 'no', 'yes']
}
labels = ['a', 'b', 'c']
df = pd.DataFrame(exam_data, index=labels)
print(df)