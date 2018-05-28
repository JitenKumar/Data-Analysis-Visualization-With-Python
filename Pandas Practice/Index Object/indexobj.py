import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series,DataFrame

my_data = Series([1,2,3,45,55,5],index=['A','B','C','D','E','F'])

print(my_data)

my_index_obj = my_data.index
print(my_index_obj[2])

print()
print(my_index_obj[2:])

# can't Reindex in the normal way

ser1 = Series([1,2,3,4,5],index=['a','b','c','d','e'])

print(ser1)

ser2 = ser1.reindex(['A','B','C','D','E'])
print(ser2)

ser3 = Series(['One','Two','Three'],index=[1,2,3])
print(ser3)

ser3.reindex([1,2,333,455])
print(ser3)

# making matrix
my_frame = DataFrame(randn(25).reshape((5,5)),index=['A','B','C','D','E'],columns=['C1','C2','C3','C4','C5'])

print(my_frame)
new_columns = ['a','b','c','d','e','f','g']
my_frame2 = my_frame.reindex(columns=new_columns)
print(my_frame2)
