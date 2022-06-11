#Case-1-Series

# What is a Series?
# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.

import pandas as pd

a=[7,5,6]
x=pd.Series(a)
print(x)

#Outputs :
# 0    7
# 1    5
# 2    6

#Note that the series method helps us to print the series with indexes, indexes default value is numbers.

#Case-2-Labels


# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.

import pandas as pd

arr=[3,4,5,60]
x=pd.Series(arr)
print(x[2])

#Outputs: 5  (Returns the element in the specified position)

#Case-3 -Indexes

#We can create our own labels, default is numbers, but you vcan change them!

import pandas as pd

arr=[8,3,5,2,4]
x=pd.Series(arr,index=['a','b','c','d','e'])
print(x)

#Outputs:

# a    8
# b    3
# c    5
# d    2
# e    4

#Note : Number of index values specified must always be equal to the number of elements.


#Case-4 -Accessing the element of a specific  index, when index parameter is used

import pandas as pd

arr=[7,6,4,6]
x=pd.Series(arr,index=['a','b','c','d'])
print(x['a'])   #NOte : SPecifying the elemtn inside an inverted comma is a must!

# Output: 7

#Case-5-Key/Value pair as a list

import pandas as pd

calories={"Monday":410,"Tuesday":650,"Wednesday":400}
x=pd.Series(calories)
print(x)

#Output:
# Monday       410
# Tuesday      650
# Wednesday    400

#Case-6-Dataframes

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.

import pandas as pd

data={
    "calories":[430,560,340],
    "Days":[780,540,230]
}
x=pd.DataFrame(data)
print(x)

#Outputs:

#    calories  Days
# 0       430   780
# 1       560   540
# 2       340   230
