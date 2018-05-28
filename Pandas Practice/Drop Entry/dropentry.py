import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series,DataFrame


# making a series
ser1 = Series([1,2,3,4,5],index=['A','B','C','D','E'])
print(ser1)
print(ser1.drop('A'))

# droping values in the dataframe

dframe = DataFrame(np.arange(9).reshape((3,3)),index=['India','Japan','China'],columns=['POP','Size','Year'])
print(dframe)
# droping a row
print(dframe.drop('India'))
# drop a row is not permanent
dframe2 = dframe.drop('Japan')
print(dframe2)

# dropping the columns
dframe3 = dframe2.drop('Year',axis=1)
print(dframe3)




