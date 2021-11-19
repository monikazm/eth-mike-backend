#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import
from nptdms import TdmsFile # https://nptdms.readthedocs.io/en/stable/
from matplotlib import pyplot as plt
import numpy as np


# In[16]:


file = TdmsFile.read("tdms_files/"+"Mike3_maxAcc3.tdms")
current = file["maxAcc"]["Current [A]"][:]

max_current = max(current)
min_current = min(current)

torque_constant = 0.137  # Mike6: 0.0302 Nm/A; Mike1-5 & 7: 0.137 Nm/A

maxTorque = max_current*torque_constant
minTorque = min_current*torque_constant

print("maximum Torque =", maxTorque, "maximum current =", max_current)
print("minimum Torque =", minTorque, "minimum current =", min_current)

