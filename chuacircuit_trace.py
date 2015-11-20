# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:27:34 2015

@author: Brenda_Brandy
"""

from __future__ import division, print_function

from numpy import array, arange
##from pylab import plot, show
from visual import *

"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
"""


"""
#coefficients
c1 = 1.0 / 10.0
c2 = 1.0 / 0.5
G = 0.7
L = 1.0 / 7.0
"""

#different initial conditions

#for the large stable limit cycle
#r_array = array([ 1.45305 ,-4.36956 ,0.15034 ],float)

#for the large stable limit cycle
#r_array = array([ 9.13959 , - 1.35164  , - 59.2869],float)

#for the hyperbolic periodic orbit with period T = 3.93615
#r_array = array([ 10.00717  , 0.80100  ,-23.90375  ],float)

#for the double scroll attractor
r_array = array([ 0.15264, -0.02281 ,0.38127  ],float)

#coefficients for double scroll attractor
c1 = 1.0 / 9.0
c2 = 1.0 
G = 0.7
L = 1.0 / 7.0


"""
#Negative Resistor current, piecewise function voltage should be vc1

def g(v):
	if v > -1 and v < 1:
		return -4.0 * v
	elif v > 1: #if v is bigger than 1
		return -4.0 - 0.1*(v-1.0)
	else: #if v is less than -1
		return 4.0 - 0.1*(v+1.0)

"""

#Negative Resistor current, piecewise function voltage should be vc1
#for double scroll
def g(v):
	if v > -1 and v < 1:
		return -0.8* v
	elif v > 1: #if v is bigger than 1
		return -0.8 - 0.5*(v-1.0)
	else: #if v is less than -1
		return 0.8 - 0.5*(v+1.0)

#define vector function f
def f(r_array,t):
    x = r_array[0] #voltage across c1
    y = r_array[1] #voltage across c2
    z = r_array[2] #current across L
    fx = (G*(y-x) - g(x) ) / c1
    fy = (G*(x - y) + z) / c2
    fz = - y / L
    return array([fx,fy,fz],float)

#initial condition and step size
t_i = 0.0
#t_f = 50.0
t_f = 300.0
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
#show()5

"""
ax.plot(xpoints, ypoints, zpoints, label = "double scroll")
ax.legend()
plt.show()
"""

#for animation
ball = sphere(make_trail=True, trail_type="curve", interval=1, retain=20)
ball2 = sphere(make_trail=True, trail_type="curve", interval=1, retain=20, color = color.blue)
ball.radius = 0.1
ball2.radius = 0.1
ball2.trail_object.color=color.blue
ball.pos = (xpoints[0],ypoints[0],zpoints[0])
pointer = arrow(pos=(xpoints[500],ypoints[500],zpoints[500]),axis=(xpoints[500]-xpoints[0],ypoints[500]-ypoints[0],zpoints[500]-zpoints[0]), shaftwidth=0.05)
n = 500
for i in range(1, int(N)-n):
    rate(120)
    ball.pos = (xpoints[i], ypoints[i], zpoints[i])
    ball2.pos = (xpoints[i+n], ypoints[i+n], zpoints[i+n])
    pointer.pos = (xpoints[i+n],ypoints[i+n],zpoints[i+n])
    pointer.axis = (-xpoints[i+n]+xpoints[i],-ypoints[i+n]+ypoints[i],-zpoints[i+n]+zpoints[i])
 

