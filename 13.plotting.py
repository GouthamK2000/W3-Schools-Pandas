#Case-1-Regular plotting

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Read.csv')
df.plot()
plt.show()

#Case-2- Selecting what we ant to plot

# Scatter Plot
# Specify that you want a scatter plot with the kind argument:

# kind = 'scatter'

# A scatter plot needs an x- and a y-axis.

# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

# Include the x and y arguments like this:

# x = 'Duration', y = 'Calories'

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Read.csv')
df.plot(kind='scatter',x='Duration',y='Calories') #kind tells us what ind of chart we want to plot. x and y axis should be the titles in the imported csv file.
df.show()


#Histogram

import pandas as pd
import matplotlib.pyplot as plt

df=pdread_csv('Data.csv')
df['Duration'].plot(kind='hist') # If we want to plot a histogram, it is enough if we include one column.
plt.show()