#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'widget')


# In[2]:


# read in the excel file
file = pd.read_excel("DynamicFriction_Mike3.xlsx")
vel = file["Velocity [deg/s]"]
tor = file["Viscous Friction [Nm]"]


# In[3]:


# create data to plot, adjust max_vel and vel_steps parameters (according to your measurements)
max_vel = 600
vel_steps = 50

velocities = []
for i in range(-max_vel,max_vel+1,vel_steps):
    if i != 0:
        velocities.append(i)

viscous_friction = [0] * len(velocities)
for i in range(0,len(velocities)):
    for j in range(0,len(vel)):
        if vel[j] == velocities[i]:
            viscous_friction[i] = tor[j]


# In[4]:


# plotting
plt.clf()
plt.scatter(velocities, viscous_friction)
plt.xlabel("Velocity [deg/s]")
plt.ylabel("Viscous Friction [Nm]")
plt.title("Mike 3 Viscous Friction")
plt.savefig("Mike3_DynamicFriction.pdf")
plt.show()

