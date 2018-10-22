#!/usr/bin/env python
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import random
#
x_coordinates       = [1, 2, 3, 4, 5]
y_coordinates       = [1, 2, 2, 0, 0]
colors              = [0.0, 1, 1.0, .0]
#
colors = ['red', 'blue','red', 'blue']
#col1 = ['#E6764F', '#A12678','#E6764F', '#A12678']
#colors = [[0.9, 0.2, 0.4, 0.9],[0.9, 0.2, 0.4, 0.9],[0.9, 0.2, 0.4, 0.9],[0.9, 0.2, 0.4, 0.9]]
#
### iterate over the series
for x, y, c in zip(x_coordinates, y_coordinates, colors):
   #plt.plot(x, y, color=c, linestyle='-', marker='o', markeredgecolor='k',markersize=10)
   plt.plot(x, y, color=c)
plt.show()

#==============================================================================
# ###funguje dobre
# import numpy as np
# from matplotlib.collections import LineCollection
# import matplotlib.pyplot as plt
# x = np.linspace(0,4*np.pi,10000)
# y = np.cos(x)
# lwidths=1+x[:-1]
# 
# print 'lwidths', lwidths
# points   = np.array([x, y]).T.reshape(-1, 1, 2)
# segments = np.concatenate([points[:-1], points[1:]], axis=1)
# 
# lc = LineCollection(segments, linewidths=lwidths,color='blue')
# 
# fig,a = plt.subplots()
# a.add_collection(lc)
# a.set_xlim(0,4*np.pi)
# a.set_ylim(-1.1,1.1)
# fig.show()
# 
# plt.show()
#==============================================================================

#xs = range(11)
#ys = [0] * 11
#colors = [ i * 0.1 for i in range(11) ] 
#
#plt.scatter(xs, ys, s=600, c = colors, cmap='YlGnBu')
#plt.colorbar()
#plt.show()

#x       = [1, 2, 3, 4, 5]
#y       = [1, 2, 2, 0, 0]
#lasing  = [0.0, 1, 1.0, .0, 1.0]
#
#col = ['red', 'blue','red', 'blue']
#col1 = ['#E6764F', '#A12678','#E6764F', '#A12678']
#col2 = [[0.9, 0.2, 0.4, 0.9],[0.9, 0.2, 0.4, 0.9],[0.9, 0.2, 0.4, 0.9],[0.9, 0.2, 0.4, 0.9]]
#print 'lasing', lasing
#
#plt.plot(x, y, color=col2)
#plt.show()



## x and y coordinates
#x_coordinates = [range(1,4)]*2
#y_coordinates = [[3,4,5],[2,2,2]]
#
## colors (one per series --> 2 in this example)
#colors = []
#r = random.random
#for i in range(0,len(x_coordinates)):
#    rgb =  (r(),r(),r())
#    print 'rgb', rgb,'\n'
#    colors.append(rgb)
#
## iterate over the series
#for x, y, c in zip(x_coordinates, y_coordinates, colors):
#    plt.plot(x, y, color=c, linestyle='-', marker='o', markeredgecolor='k',
#            markersize=10)
#
## show the figure
#plt.margins(x=0.1, y=0.1)
#plt.show()
#
#print 'rgb', rgb
#print 'colors', colors