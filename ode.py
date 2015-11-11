# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:32:18 2015

@author: Brenda_Brandy
"""

from __future__ import division, print_function

from numpy import array, arange
from pylab import plot, show


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#coefficients
c1 = 1.0 / 10.0
c2 = 1.0 / 0.5
G = 0.7
L = 1.0 / 0.7

#function or response of non-linear circuit
    

#r_array = array([ 1.45305 ,-4.36956 ,0.15034 ],float)
r_array = array([ 9.13959 , - 1.35164  , - 59.2869],float)
#r_array = array([ 10.00717  , 0.80100  ,-23.90375  ],float)

#define vector funciton f
def f(r_array,t):
    x = r_array[0]
    y = r_array[1]
    z = r_array[2]
    fx = (G*(y-x)) / c1
    fy = (G*(x - y) + z) / c2
    fz = - y / L
    return array([fx,fy,fz],float)

#initial condtion and stepsize
t_i = 0.0
#t_f = 50.0
t_f = 100.0
N = 10000.0
h = (t_f-t_i) / N

tpoints = arange(t_i,t_f,h)
xpoints = []
ypoints = []
zpoints = []

#fourth order RK loop
for t in tpoints:
    xpoints.append(r_array[0])
    ypoints.append(r_array[1])
    zpoints.append(r_array[2])
    k1 = h*f(r_array,t)
    k2 = h*f(r_array+0.5*k1, t+0.5*h)
    k3 = h*f(r_array+0.5*k2, t+0.5*h)
    k4 = h*f(r_array+k3, t+h)
    
    r_array += (k1+2*k2+2*k3+k4)/6.0

#plot y against t  
#plot(tpoints,ypoints)
#show()

#plot z againt x
#plot (xpoints,zpoints)
#show()

ax.plot(xpoints, ypoints, zpoints, label='parametric curve')
ax.legend()
plt.show()