import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series,DataFrame

ser1 = Series(np.arange(3),index=['c','d','e'])

ser1 = 2* ser1

print(ser1)

dframe = DataFrame(randn(25).reshape((5,5)),index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])

print(dframe)

print(dframe[['c1','c2']])

print(dframe[dframe['c3']>3])

print(dframe > 10)

print(dframe.ix['a'])