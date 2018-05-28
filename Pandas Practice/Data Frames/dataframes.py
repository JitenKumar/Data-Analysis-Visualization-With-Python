import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# importing browser
# import webbrowser
# website_url = 'https://en.wikipedia.org/wiki/List_of_all-time_NFL_win%E2%80%93loss_records'
# webbrowser.open(website_url)
# copying a data from clipboard
nfl_data = pd.read_clipboard()

print(nfl_data)

#getting all the columns name

print(nfl_data.columns)

# getting a particular column (only single words)

print(nfl_data.Rank)

# getting multiple words columsn
print(nfl_data['Total Games'])

#using the dataframs
DataFrame(nfl_data,columns=['Rank','Team','Total Games','Division'])

#getting few rows
print(nfl_data.head(3))

#getting the last frames

print(nfl_data.tail(4))

# getting the rows on particular index
print(nfl_data.ix[4])
#Assigning the values
nfl_data['Rank'] = 34
print(nfl_data)
# using arrays

nfl_data['Rank'] = np.arange(16)

print(nfl_data)

# importing the series into the data frame

ins_data = Series(["Jiten","Palsra"],index=[4,9])

nfl_data['Team'] = ins_data
print(nfl_data)

# Deleting a particular columns
del nfl_data['Rank']
print(nfl_data)


# constructing a dataframe from a dictionary

new_dict = {'Name':['Jiten','Palsra','Kumar'],'Rank':[1,2,3]}

new_data_frame = DataFrame(new_dict)
print(new_data_frame)