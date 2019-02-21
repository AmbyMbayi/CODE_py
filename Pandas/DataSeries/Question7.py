"""write a python pandss to change the dta type of given column or series"""

import pandas as pd 
s1 = pd.Series(['100', '200', 'python', '300.2','400'])
print("original data series")
print(s1)
print("Change the said data type to numeric")
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)