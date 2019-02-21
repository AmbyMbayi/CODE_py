"""write a pandas program to find the sum, mean, max, min value of 'Production' column of
the file"""

import pandas as pd 
import numpy as np 
df = pd.read_excel('coalpublic2013.xls')
print("sum: ", df["Production (short tons)"].sum())
print("Mean:", df["Production (short tons)"]. mean())
print("Maximum", df["Production (short tons)"].max())
print("Minimum", df["Production (short tons)"]. min())