#Case-1- Basic DataFrame/Printing the Data FRame as it is


import pandas as pd

data={
    "calories":[34,23,5,45,24,46],
    "Days":["Day1","Day2","Day3","Day4","Day5","Day6"]
}

df=pd.DataFrame(data)
print(df)

#Outputs :
#    calories  Days
# 0        34  Day1
# 1        23  Day2
# 2         5  Day3
# 3        45  Day4
# 4        24  Day5
# 5        46  Day6

#Case-2-loc[]

import pandas as pd

data={
      "calories":[34,23,5,45,24,46],
    "Days":["Day1","Day2","Day3","Day4","Day5","Day6"]
    
}

df=pd.DataFrame(data,index=[1,2,3,4,5,6])
print(df.loc[3])

#Output:

# calories       5
# Days        Day3

#NOTE :Above example returns a series.

#Case-3-Return multiple rows.

import pandas as pd

data={
      "calories":[34,23,5,45,24,46],
    "Days":["Day1","Day2","Day3","Day4","Day5","Day6"]
    
}

df=pd.DataFrame(data)
print(df.loc[[0,1]])

#Outputs:

#    calories  Days
# 0        34  Day1
# 1        23  Day2

#Case-4-Reading files

import pandas as pd

df=pd.read_csv('data.csv')
print(df)

#Here exterior files such as excel and csv files can be used to  read data from.Upcoming lessons talk about it.

