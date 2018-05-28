import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series,DataFrame


dframe1 = DataFrame(np.arange(4).reshape((2,2)),index=['A','B'],columns=list('AB'))

print(dframe1)


dframe2= DataFrame(np.arange(16).reshape((4,4)),index=['A','B','C','D'],columns=list('ABCD'))


print(dframe1 + dframe2)

dframe1.add(dframe2,fill_value=0)

print(dframe1 - dframe2)