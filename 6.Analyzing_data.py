#Case-1-head()

import pandas as pd

df=pd.read_csv('data.csv')
print(df.head(10))  #Outputs the heading along with the 10 rows following it.

#NOTE: head actually df.head(), if not specified with any number returns the top 5 rows +  the title.

#Case-2-tail()

import pandas as pd

df=pd.reaad_csv('data.csv')
print(df.tail(10))  #Outputs the heading along with the last 10 rows in each heading.

#NOTE : if nothing is mentioned inside df.tail(), then it return the bottom 5 elements + the title for each column.


#Case-3- info()

import pandas as pd

df=pd.read_csv('data.csv')
print(df.info())  #Outputs some basic infor of the daatset, like the no of entries, data usage, data types etc.