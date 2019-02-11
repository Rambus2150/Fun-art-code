'''
Created on Feb 7, 2019

@author: Ramon Bustamante
'''
import numpy as np
import matplotlib.pyplot as plt

# n is the number of iterations.
# ax is the axis
# p is the points on the axis
# w will be the size
# x is the size modifier
def draw_Fsquares(ax,n,p,w,x):
    if n>0:
       
        w=w*x
        ns=w # new size
        # origin point to calculate new squares
        ll=p[0] #lower left origin point a
        ul=p[1] #upper left  origin point b
        ur=p[2] #upper right origin point c
        lr=p[3] # lower right origin point d
        '''use these points as origin points to calculate the new squares to be created'''    
        
        a = np.array([ll-ns,[ll[0]-ns,ll[1]+ns],ll+ns,[ll[0]+ns,ll[1]-ns],ll-ns])
        b = np.array([ul-ns,[ul[0]-ns,ul[1]+ns],ul+ns,[ul[0]+ns,ul[1]-ns],ul-ns])
        c = np.array([ur-ns,[ur[0]-ns,ur[1]+ns],ur+ns,[ur[0]+ns,ur[1]-ns],ur-ns])
        d = np.array([lr-ns,[lr[0]-ns,lr[1]+ns],lr+ns,[lr[0]+ns,lr[1]-ns],lr-ns])
        
        ax.plot(p[:,0],p[:,1],color="k") # x and y axis orientation and locations
        
        ''' new squares on the all four corners'''
        draw_Fsquares(ax,n-1,a,w,x)
        draw_Fsquares(ax,n-1,b,w,x)
        draw_Fsquares(ax,n-1,c,w,x)
        draw_Fsquares(ax,n-1,d,w,x)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]]) #size or grid and draws line from left to right
fig, ax = plt.subplots()

draw_Fsquares(ax,8,p,orig_size,.25) #draw_squares(ax,15,p,.8) function call here 

ax.set_aspect(1.0) ##1.0 sets the aspect ration of the picture, try to keep at one.
ax.axis('off') ##  turns on the axis grid numbers
plt.show()
fig.savefig('fsquares.png')


