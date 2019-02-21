"""Write a pandas program that select the rows where number of attempts in the examination
is less than 2 and socre is greater than 15
"""

import pandas as pd 
import numpy as np 

exam_data = {
    'name': ['Joel','Amby','Moses','Cliff'],
    'score':[41,32,23,44],
    'attempts':[2,3,4,5],
    'qualify':['yes','no','yes','yes']
}

labels = ['a','b','c','d']

df = pd.DataFrame(exam_data, index=labels)
print("attempts is less than 2 and score id greater than 15")
print(df[(df['attempts']<3 ) & (df['score']> 15)])