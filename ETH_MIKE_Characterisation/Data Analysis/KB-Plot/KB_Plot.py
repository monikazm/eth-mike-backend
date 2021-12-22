#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import
from matplotlib import pyplot as plt
import pandas as pd


# In[2]:


file = pd.read_excel("KB_mike3.xlsx")
print(file)


# In[3]:


# extract from csv
b_fdm = file["B FDM"]
k_fdm = file["K FDM"]
b_tacho = file["B tacho"]
k_tacho = file["K tacho"]
b_foaw = file["B FOAW"]
k_foaw = file["K FOAW"]


# In[5]:


# plotting
plt.scatter(b_fdm,k_fdm)
plt.plot(b_fdm,k_fdm,label='FDM')

plt.scatter(b_tacho,k_tacho)
plt.plot(b_tacho,k_tacho,label='Tacho')

plt.scatter(b_foaw,k_foaw)
plt.plot(b_foaw,k_foaw,label='FOAW')

plt.legend()
plt.xlabel('B [(Nm*s)/deg]')
plt.ylabel('K [Nm/deg]')
plt.title('MIKE 3 KB-Plot')
plt.savefig("Mike3_KB_Plot.pdf")
plt.show()

