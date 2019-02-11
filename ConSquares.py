'''
Created on Feb 7, 2019

@author: Ramon Bustamante
'''
import numpy as np
import matplotlib.pyplot as plt

# n is the number of squares.
# ax is the axis
# p is the points on the axis
#q alters these points with w and i1 modifiers.
# w never changes and is the percent change to reach he designated point in i1
def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]    #must be in array bounds [0,1,2,3,4] makes no changes because they are in the same place first entered.
        q = p*w + p[i1]*(1-w) # takes the length with appropriate weight and gets new coordinates to approach selected coordinates.
        ax.plot(p[:,0],p[:,1],color='k') # x and y axis orientation and locations
        draw_squares(ax,n-1,q,w)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]]) #size or grid
fig, ax = plt.subplots()

draw_squares(ax,15,p,.8) # function call here. Make changes here.

ax.set_aspect(1.0) ##1.0 sets the aspect ration of the picture, try to keep at one.
ax.axis('off') ##  turns on the axis grid numbers
plt.show()
fig.savefig('ConSquares.png')


