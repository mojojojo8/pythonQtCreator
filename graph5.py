#!/usr/bin/env python
'''
Color parts of a line based on its properties, e.g., slope.
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


x = np.array([ -1.8,          2.35619449,  4.71238898,  7.06858347,  9.42477796]) #len5
y = np.array([ 0.00000000e+00,   7.07106781e-01,  -1.00000000e+00,   7.07106781e-01, 3.67394040e-16]) #len5
c = np.array([ 0.0, 0.0,  1.0, 1.0, 1.0]) #len4
w = np.array([ 0.5, 0.5,  2, 2, 2.5])

print 'x', x, len(x), type(x)
print 'y', y, len(y), type(y)
print 'c', c, len(c), type(c)

# Create a colormap for red, green and blue and a norm to color
# f' < -0.5 red, f' > 0.5 blue, and the rest green
#red= z -1:0.1, green = z 0.1:05, blue= z 0.5:1
cmap = ListedColormap(['b', 'g', 'r'])
norm = BoundaryNorm([-1, 0.2, 0.5, 1], cmap.N)  


# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be numlines x points per line x 2 (x and y)
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Create the line collection object, setting the colormapping parameters.
# Have to set the actual values used for colormapping separately.

lc = LineCollection(segments, linewidths=w,cmap=cmap, norm=norm)
#lc.set_linewidth(3)
lc.set_array(c)

plt.gca().add_collection(lc)

#plt.xlim(x.min(), x.max())
#plt.ylim(y.min(), y.max())

plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.plot(0, 0, '+', color='black')
plt.plot(x[0], y[0], '+')
plt.annotate('Start point', xy=(x[0], y[0]), xytext=(x[0]*1.005, y[0]*1.005))
            
plt.show()
