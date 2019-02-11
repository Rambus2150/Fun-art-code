'''
Created on Feb 7, 2019

@author: Ramon Bustamante
'''
import numpy as np
import matplotlib.pyplot as plt

# n is the number of iterations.
# ax is the axis
# p is the points on the axis
# w is the size and changes with the modifier x
def draw_Fsquares(ax,n,p,w,x):
    if n>0: 
        ''' coordinates being changed'''
        '''             #left######,center,#right###########################'''   
        left= np.array([p[0]-w*(1-x),p[0],[p[2][0]-w*(1+x),p[2][1]-w*(1-x)]])  
        right= np.array([p[2]-w*(1-x),p[2],[p[2][0]+w*(1-x),p[2][1]-w*(1-x)]])  

        w=w*(1-x) #change the size before the iterative call    
        ax.plot(p[:,0],p[:,1],color='k') # x and y axis orientation and locations
        #two branches so two calls
        draw_Fsquares(ax,n-1,left,w,x)
        draw_Fsquares(ax,n-1,right,w,x)
       

plt.close("all") 
'''change size here'''
size = 200              
p = np.array([[-size,-size],[0,0],[size,-size]]) #size or grid and draws line from left to right
fig, ax = plt.subplots()

draw_Fsquares(ax,8,p,size,.5) # main function call here 

ax.set_aspect(1) ##1.0 sets the aspect ratio of the picture, try to keep at one.
ax.axis('off') ##  turns on the axis grid numbers
plt.show()
fig.savefig('branches.png') 


