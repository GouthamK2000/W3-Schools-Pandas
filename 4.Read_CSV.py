#Case-1-Read a CSV file

import pandas as pd

x=pd.read_csv('data.csv')
print(x.to_string())  #.to_string prints the entire dara set

# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).

# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

# In our examples we will be using a CSV file called 'data.csv'.

#NOTE: If to_string is not used, only the first and the last 5 rows are printed, by default.

#Case-2-pd.options .display.max_rows

import pandas as pd

print(pd.options.display.max_rows)  #Returns the maximum rows that can be printed by the computer. (Outputs 60)

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows,
#  the print(df) statement will return only the headers and the first and last 5 rows.

#Case-3-Change maximum number of lines

import pandas as pd

pd.options.display.max_rows=9999
df=pd.read_csv('data.csv')
print(df)