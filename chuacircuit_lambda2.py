# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:05:30 2015
@author: Brenda_Brandy
"""
from __future__ import division, print_function
from numpy import array, arange, sqrt, log, arcsin, std
from pylab import plot, show, axhline
from math import pi

x = []
y = []
z = []
t_i 	= 	0.0
t_f 	= 	4000.0
N 		= 	200000
h 		=	(t_f-t_i) / N
tpoints = 	arange(t_i,t_f,h)
cutoff = 5.0/6.0
#Takes indecies of two points on the attractor
def dist(a,b):
    return sqrt((x[a]-x[b])**2 + (y[a]-y[b])**2 + (z[a]-z[b])**2)

#Takes vectors v1 and v2
def crossmag(x1,x2,y1,y2,z1,z2):
    i = y1*z2 - z1*y2
    j = z1*x2 - x1*z2
    k = x1*y2 - y1*x2
    crossprod = sqrt(i**2 + j**2 + k**2)
    v2 = sqrt(x2**2 + y2**2 + z2**2)
    v1 = sqrt(x1**2 + y1**2 + z1**2)
    if v1 == 0 or v2 ==0:
        return 0
    else:
        return(crossprod / (v1*v2))
     
#takes index of the compared point, returns index of closest point not on the same cycle, j
def test(index): 
    d = 1.0
    final_crit = 100
    for j in range (0 , index - 1000):
        distance= dist(index,j)
        theta = arcsin(crossmag(x[index]-x[j],vx,y[index]-y[j],vy,z[index]-z[j],vz)) 
        criteria = distance * (theta**2)
        if (dist(index,j) < d and theta < (pi/6)):
            if criteria < final_crit:
                d = dist(index,j)
                n = j
    for j in range (index + 1000 , int(N*cutoff)):
        distance= dist(index,j)
        theta = arcsin(crossmag(x[index]-x[j],vx,y[index]-y[j],vy,z[index]-z[j],vz)) 
        criteria = distance * (theta**2)
        if (dist(index,j) < d and theta < (pi/6)):
            if criteria < final_crit:
               d = dist(index,j)
               n = j
    #print(crossmag(x[index]-x[n],vx,y[index]-y[n],vy,z[index]-z[n],vz))
    return n
	
def g(v):
	if v > -1 and v < 1:
		return -0.8* v
	elif v > 1: #if v is bigger than 1
		return -0.8 - 0.5*(v-1.0)
	else: #if v is less than -1
		return 0.8 - 0.5*(v+1.0)
	
	
r_array = array([ -1.7713,0.0527854,1.74606  ],float)
c1 = 1.0 / 9.0
c2 = 1.0 
G = 0.7
L = 1.0 / 7.0
def diff(r_array,t):
    x 	= r_array[0]
    y 	= r_array[1]
    z 	= r_array[2]
    fx 	= (G*(y-x) - g(x) ) / c1	#dx/dt
    fy 	= (G*(x - y) + z) / c2		#dy/dt
    fz 	= - y / L					#dz/dt
    return array([fx,fy,fz],float)
#fourth order RK loop
for t in tpoints:
	x.append(r_array[0])
	y.append(r_array[1])
	z.append(r_array[2])
	k1 = h*diff(r_array,t)
	k2 = h*diff(r_array+0.5*k1, t+0.5*h)
	k3 = h*diff(r_array+0.5*k2, t+0.5*h)
	k4 = h*diff(r_array+k3, t+h)
	    
	r_array += (k1+2*k2+2*k3+k4)/6.0
	
#plot (x,y)
#show()
(xmin,xmax,ymin,ymax,zmin,zmax) = min(x),max(x),min(y),max(y),min(z),max(z)
x_range = xmax - xmin
y_range = ymax - ymin
z_range = zmax - zmin
max_d =  sqrt(x_range**2 + y_range**2 + z_range**2)
lim_d = 0.05 * max_d
print(lim_d)
separation = []
running_average_list = []
d_test = 1000
k = test(1000)
vx = x[1000] - x[k]
vy = y[1000] - y[k]
vz = z[1000] - z[k]
L = 0
di = dist(1000,k)
ti = 1000*h


for i in range(1000,int(cutoff*N)):
    d_test = dist(i,k) #check distance between fudicial and comparison point
    if d_test > lim_d: #if distance between two vectors bigger than limit distance
        tf = i*h
        df = dist(i,k)
        vx = x[i] - x[k]
        vy = y[i] - y[k]
        vz = z[i] - z[k]
        L = L + log(df/di)
        running_average = L / tf
        k = test(i)
        di = dist(i,k)
        ti = i*h
        #print("df: ",df)
        print("")
        print("init_pt: ",i)
        print("comp_pt: ",k)
        running_average_list.append(running_average)
        print("running_average: ",running_average)
        #print("di: ", di)
        #print("df/di: ",df/di)
    separation.append(dist(i,k))
    k += 1

average = L/((cutoff*t_f)-1000*h)
print("Average Lambda is ", average)
plot(running_average_list)
axhline(y=average)
axhline(y=0.23, color = 'r')
show()