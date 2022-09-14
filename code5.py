#modules
#csv
import csv

#from csv import *

x=[]
y=[]
with open('test1.txt','r') as f:
    data=csv.reader(f)
    for col in data:
        x.append(col[0])
        y.append(col[1])


print(x)
print(y)
