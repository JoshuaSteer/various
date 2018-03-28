# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 13:54:19 2018

@author: js22g12

script 
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Select mesh density
n = 11

# Generate points between pi/2 in theta and phi
theta = np.linspace(0, np.pi/2, n) # Elevation
phi = np.linspace(0, np.pi/2, n) # Azimuth
r = np.ones([n])

# Create the mesh grid 
theta, phi = np.meshgrid(theta, phi)

# Convert to cartesian co-ordinates
xc = r * np.cos(theta) * np.cos(phi)
yc = r * np.cos(theta) * np.sin(phi)
zc = r * np.sin(theta) 

# Set value of each individual face
color = np.random.rand(n-1, n-1)

# Plot results
surf = ax.plot_surface(xc, yc, zc, facecolors=cm.coolwarm(color),
                       linewidth=0, antialiased=False)
