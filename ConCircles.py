'''
Created on Feb 7, 2019

@author: Ramon Bustamante
'''
import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w,v):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w,v)    #center
        
        
        draw_circles(ax,n-1,[center[0],radius*v],radius*w,w,v)    #smaller top
        draw_circles(ax,n-1,[center[0],-radius*v],radius*w,w,v)   #smaller bottom
        draw_circles(ax,n-1,[-radius*v,center[1]],radius*w,w,v)   #smaller left
        draw_circles(ax,n-1,[radius*v,center[1]],radius*w,w,v)    #smaller right
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 5, [0,0], 100,1/3,2/3)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('conCircles.png')