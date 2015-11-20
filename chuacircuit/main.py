# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:39:08 2015

@author: Brenda_Brandy
"""
from __future__ import division, print_function
from numpy import array
from pylab import plot, show
from diffsol import solver
from lyanupov_wolf import lyanupov_wolf


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

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
 
solver(r_array)
x = x
y = y
z = z
