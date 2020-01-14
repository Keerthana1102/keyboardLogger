import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
f = open('test1.txt' , "r")
lines = [line for line in f.readlines()]
lineList = [line.rstrip('\n') for line in open('logsPy2.txt')]
lineList1 = [i.replace("'", "") for i in lineList]
print(lines)
print(lineList1)

count = {}
for s in lineList1:
    if s in count:
        count[s]+=1
    else:
        count[s] = 1
myList = []
newList = [['symbol', 'change', 'Yrows', 'Xcols']]
i=1
j=0

for key in count:
    if count[key]>=1:
        print(key, count[key])
        myList.append(key)
        myList.append(count[key])
        if j<2:
            j+=1
        else:
            j=1
        myList.append(i)
        myList.append(j)
        if j==2:
            i+=1
        newList.append(myList)
        myList=[]
with open('createCsvFile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(newList)


f.close()

# Read the  data
df = pd.read_csv("createCsvFile.csv")
print(df.head(10))
print(len(df))
d= len(df)
e=0
if (d % 2) == 0:
    e = d
    print("$$$$$$$$$$$$$$$$$",e)
else:
    df = df[:-1]
    e = d-1
    print("$$$$$$$$$$$$$$$$$",e)
a = e/2
print(a)
print(int(a))
b = int(a)

# Create an array of stock alphabets & their respective percentage change
symbol = ((np.asarray(df['symbol'])).reshape(b,2))
perchange = ((np.asarray(df['change'])).reshape(b,2))

print(symbol)
print(perchange)

# Create a pivot table
result = df.pivot(index='Yrows',columns='Xcols',values='change')
print(result)

# Create an array to annotate the heatmap
labels = (np.asarray(["{0} \n {1:.2f}".format(symb,value)
                      for symb, value in zip(symbol.flatten(),
                                               perchange.flatten())])
         ).reshape(b,2)

# Define the plot
fig, ax = plt.subplots(figsize=(13,13))

# Add title to the Heat map
title = "Keyloggers"

# Set the font size and the distance of the title from the plot
plt.title(title,fontsize=8)
ttl = ax.title
ttl.set_position([0.5,1.05])

# Hide ticks for X & Y axis
ax.set_xticks([])
ax.set_yticks([])

# Remove the axes
ax.axis('off')

# Use the heatmap function from the seaborn package
sns.heatmap(result,annot=labels,fmt="",cmap='RdYlGn',linewidths=1,ax=ax)

# Display the Keylogger
plt.show()