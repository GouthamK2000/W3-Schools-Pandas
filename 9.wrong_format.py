# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

#Case-1- converting all things to date

import pandas as pd

df=pd.read_csv('data.csv')
df['Date']=pd.to_datetime(df['Date'])
print(df.to_string())   #In the output, all the wrong  formats are converted to Nat

#Case-2-Remove the row

import pandas as pd

df=pd.read_csv('data.csv')
df['Date']=pd.to_datetime(df['Date'])
df.dropna(subset=['Date'],inplace=True)
print(df.to_string())