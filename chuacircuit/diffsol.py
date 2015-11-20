# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:39:36 2015

@author: Brenda_Brandy
"""

from __future__ import division, print_function

from numpy import array, arange


#Negative Resistor current, piecewise function voltage should be vc1
#for double scroll
def g(v):
	if v > -1 and v < 1:
		return -0.8* v
	elif v > 1: #if v is bigger than 1
		return -0.8 - 0.5*(v-1.0)
	else: #if v is less than -1
		return 0.8 - 0.5*(v+1.0)

def solver(r_array):
    
    c1 = 1.0 / 9.0
    c2 = 1.0 
    G = 0.7
    L = 1.0 / 7.0    
    
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
    return {"x" : x , "y" : y, "z" : z}
