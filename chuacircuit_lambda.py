# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:05:30 2015

@author: Brenda_Brandy
"""

from __future__ import division, print_function

from numpy import array, arange, sqrt
from pylab import plot, show
#from visual import *

#Choose value of c based on what attractor you want.

c = 3

#for the large stable limit cycle
if c == 0:
	r_array = array([ 1.45305 ,-4.36956 ,0.15034 ],float)

#for the large stable limit cycle
if c == 1:
	r_array = array([ 9.13959 , - 1.35164  , - 59.2869],float)

#for the hyperbolic periodic orbit with period T = 3.93615
if c == 2:
	r_array = array([ 10.00717  , 0.80100  ,-23.90375  ],float)

#for the double scroll attractor
if c == 3:
	r_array = array([ 0.15264, -0.02281 ,0.38127  ],float)
	c1 = 1.0 / 9.0
	c2 = 1.0 
	G = 0.7
	L = 1.0 / 7.0

#Negative Resistor current, piecewise function voltage should be vc1
#for double scroll
def g(v):
	if v > -1 and v < 1:
		return -0.8* v
	elif v > 1: #if v is bigger than 1
		return -0.8 - 0.5*(v-1.0)
	else: #if v is less than -1
		return 0.8 - 0.5*(v+1.0)
  
#x,y, and z coordinates for each point
x = []
y = []
z = []
    
#time range

t_i = 0.0					#initial time
t_f = 300.0					#final time
N = 100000					#steps
h = (t_f-t_i) / float(N)        	#step size
tpoints = arange(t_i,t_f,h)         #list of times t

#calculate distance between two point
def dist(ref_pt, comp_pt):
    dist = sqrt((x[comp_pt]-x[ref_pt])**2 + (y[comp_pt]-y[ref_pt])**2 + (z[comp_pt]-z[ref_pt])**2)
    return dist
    
#find nearest point between reference point and point i
def ntest(ref_pt): 
    d = 10000 
    nearpt = 1
    for k in range (N):
        testd = dist(ref_pt, k)
        """
        print ("k: ", k)
        print ("ref_pt: ", ref_pt)
        print ("d: ", d)
        print ("testd: ", testd)
        """
        if (testd < d) and ((k < (ref_pt-100)) or (k > (ref_pt + 100))) :
            nearpt = k
            d = testd
    return nearpt
            

#system of differential equations that describe the circuit
def f(r_array,t):
    x = r_array[0] #voltage across c1
    y = r_array[1] #voltage across c2
    z = r_array[2] #current across L
    fx = (G*(y-x) - g(x) ) / c1	#dx/dt
    fy = (G*(x - y) + z) / c2	#dy/dt
    fz = - y / L				#dz/dt
    return array([fx,fy,fz],float)

#fourth order RK loop
for t in tpoints:
	x.append(r_array[0])
	y.append(r_array[1])
	z.append(r_array[2])

	k1 = h*f(r_array,t)
	k2 = h*f(r_array+0.5*k1, t+0.5*h)
	k3 = h*f(r_array+0.5*k2, t+0.5*h)
	k4 = h*f(r_array+k3, t+h)
	    
	r_array += (k1+2*k2+2*k3+k4)/6.0
	
	i = i + 1


#find range f xyz
xmax = max(x)
ymax = max(y)
zmax = max(z)
xmin = min(x)
ymin = min(y)
zmin = min(z)
x_range = xmax - xmin
y_range = ymax - ymin
z_range = zmax - zmin


#find the limiting distance
unit_mag =  sqrt(x_range**2 + y_range**2 + z_range**2)
limit_dist = 0.05* unit_mag
print (limit_dist)
dtest = 0    
ref_pt = 0 #start from 0, find nearest point              
ref_list = []
dist_list = []

#find nearest point to 0
comp_pt = ntest(ref_pt)

#trace the two points
while ref_pt < 3*N/4: #as long as reference point is less than 3/4 of total num of points
    print("ref_pt: ",ref_pt)
    print ("comp_pt: ",comp_pt)
    #record down values between two nearest points
    while ((dtest < limit_dist) and comp_pt < N):
        ref_list.append(ref_pt)
        dtest = dist(ref_pt, comp_pt)
        dist_list.append(dtest)
        ref_pt += 1
        comp_pt += 1
        
    ref_pt += 500
    if ref_pt < N:
        comp_pt = ntest(ref_pt) #find another nearest point
        dtest = dist(ref_pt, comp_pt)

       
"""

#animation
p1 = sphere(pos = (x[0],y[0],z[0]), radius = 0.1, make_trail=True, trail_type="curve", interval=1, retain=50)
p2 = sphere(pos = (x[I],y[I],z[I]), radius = 0.1, make_trail=True, trail_type="curve", interval=1, retain=50)


for i in range(1, N-I):
    rate(60)
    p1.pos = (x[i], y[i], z[i])
    p2.pos = (x[I+i-1], y[I+i-1], z[I+i-1])
"""

#plot dist againt ref_pt
plot (ref_list,dist_list)
show()