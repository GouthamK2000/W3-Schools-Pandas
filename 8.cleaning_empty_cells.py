#Case-1- Simply removing the empty cells

import pandas as pd

df=pd.read_csv('data.csv')
new_df=df.dropna()
print(new_df.to_string())       

#dropna() returns a new datafram and wont modify the original.


#case-2- If we want to change the original dataframe

import pandas as pd

df=pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())

#Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.


#Case-3-Replace empty cells with some values

import pandas as pd

df=pd.read_csv('data.csv')
df.fillna(130,inplace=True)  #Value we want to substitute in empty cells

print(df.to_string())



# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

import numpy as np

df=pd.read_csv('data.csv')
x=df['calories'].mode()                #mean(),median() also can be used, depending on what we need to use.
df['calories'].fillna(x,inplace=True)
print(df.go_string())