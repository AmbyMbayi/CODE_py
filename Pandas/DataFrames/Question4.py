"""write a pandas program to select the 'name' and 'score' columns from the follwoing dataframe
"""
import pandas as pd 
import numpy as np 

exam_data= {
    'name':['Amby','Joel','cliff','Odhiambo'],
    'score':[1,2,3,4],
    'attempts':[1,2,3,5],
    'qualify':['yes','no','yes','yes']
}
labels = ['a','b','c', 'd']

df =pd.DataFrame(exam_data, index=labels)
print("Select specific columns: ")
print(df[['name','score']])