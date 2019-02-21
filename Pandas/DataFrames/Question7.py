"""write a pandas program to count the number of
rows and columns of a given dataframe
"""
import pandas as pd 
import numpy as np

exam_data= {
    'name':['Joel', 'Amby','Cliff', 'Moses'],
    'score':[1,2,3,4],
    'attempts':[1,3,5,7],
    'qualify':['yes','yes','yes','no']

}
labels = ['a','b','c','d']

df = pd.DataFrame(exam_data, index=labels)

total_rows = len(df.axes[0])
total_col =len(df.axes[1])

print("number of Rows: "+str(total_rows))
print("number of columns: "+str(total_col))