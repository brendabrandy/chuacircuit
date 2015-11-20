# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:52:04 2015

@author: Brenda_Brandy
"""

from __future__ import division, print_function

from numpy import array, arange, sqrt
from pylab import plot, show

N = 100000					#steps

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
        if (testd < d) and ((k < (ref_pt-100)) or (k > (ref_pt + 100))) :
            nearpt = k
            d = testd
    return nearpt
            

def lyanupov_wolf(x,y,z):

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
            
    return{"ref_list": ref_list, "dist_list":dist_list}