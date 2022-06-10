#Basic example

import pandas as pd

mydata={
    'cars':["BMW","Maruti","Ferrari"],
    'Cost':[6000,7000,3000]
}

var=pd.DataFrame(mydata)
print(var)

#Outputs:
#       cars  Cost
# 0      BMW  6000
# 1   Maruti  7000
# 2  Ferrari  3000