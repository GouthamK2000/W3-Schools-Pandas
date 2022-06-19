# Wrong Data
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

# If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.

# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.


#Case-1-Replacing values in a specific column

import pandas as pd

df=pd.read_csv('data.csv')
df.loc[7,'Duration']=46  # syntax : .loc(row no, name of the row(first element, or the title)) = value we want
print(df.to_string())

#Case-2- Replacing for large datasets

import pandas as pd

df=pd.read_csv('data.csv')
if df.loc[x,'Duration']>120:
    df.loc[x,'Duration']=45

print(df.to_string())


#Case-3-Removing the entire row:

import pandas as pd

df=pd.read_csv('Read.csv')
if df.loc[x,'Duration']>300:
    df.drop[x,inplace=True]

print(df.to_string())