"""write a pandas program to convert a numpy to a pandas series
"""

import numpy as np 
import pandas as pd 
np_array = np.array([10, 20, 30, 40, 50])
print("Numpy array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted pandas series: ")
print(new_series)