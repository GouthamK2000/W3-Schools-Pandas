#Case-1-TO find the duplicated rows

import pandas as pd

df=pd.read_csv('data.csv')
print(df.duplicated())  #.duplicated() value returns True, if the row already exists, else returns False

# Case-2-Removing Duplicates

import pandas as pd

df=pd.read_csv('Data.csv')
df.drop_duplicates(inplace=True) #drop_duplicates() deletes all the duplicate. specyfying inplace=True ensures that the original file is returned after modyfying and that new one is not returned.
print(df.to_string())