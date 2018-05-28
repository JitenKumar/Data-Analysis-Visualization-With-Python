import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series,DataFrame
array = np.array([[1,3,4,4],[1,4,5,5]])
dframe1 = DataFrame(array,index=list('AB'),columns=list('abcd'))
print(dframe1)

print(dframe1.describe())

import pandas.io.data as pdweb
import datetime

prices_oils = pdweb.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2013,1,1),end=datetime.datetime(2016,1,1))['Adj Close']

print(prices_oils.head())

prices_volume = pdweb.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2013,1,1),end=datetime.datetime(2016,1,1))['Volume']
prices_volume.head()

rets = prices_oils.pct_change()

corr = rets.corr

prices_oils.plot()
sns.corrplot(rets,annot=False,diag_names=False)
