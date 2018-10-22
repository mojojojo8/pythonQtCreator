#!/usr/bin/env python
#-*- coding:utf-8 -*-

from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [125, 32, 54, 253, 67, 87, 233, 56, 67]

color = [str(item/255.) for item in y]

# Function to map the colors as a list from the input list of x variables
def pltcolor(lst):
    cols=[]
    for l in lst:
        if l>200:
            cols.append('red')
        elif l>100:
            cols.append('blue')
        else:
            cols.append('green')
    print cols
    return cols
# Create the colors list using the function above
cols=pltcolor(y)

#plt.scatter(x=x,y=y,s=500,c=cols) #Pass on the list created by the function here
plt.plot(x,y,c=cols) #Pass on the list created by the function here
plt.grid(True)
plt.show()

plt.show()