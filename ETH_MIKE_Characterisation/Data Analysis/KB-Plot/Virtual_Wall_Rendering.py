#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import
from nptdms import TdmsFile # https://nptdms.readthedocs.io/en/stable/
from matplotlib import pyplot as plt
import numpy as np


# In[2]:


file = TdmsFile.read("mike6_wall_rendering.tdms")
wall_position = 45


# In[3]:


position = file['KB_Plot']['Position [deg]'][:]-wall_position
force = file['KB_Plot']['Force [N]'][:]


# In[4]:


plt.clf()
plt.plot(position, force)
plt.xlabel('Position [deg]')
plt.ylabel('Force [N]')
plt.title("Mike 6 Virtual Wall Rendering")
plt.xlim([-5,5])
plt.savefig("Mike6_VirtualWall.pdf")
plt.show()

