
# coding: utf-8

# In[19]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_CONTAINER = "data/"


# In[20]:


def load_csv_data(file_name, data_container=DATA_CONTAINER):
    csv_path = os.path.join(data_container, file_name)
    return pd.read_csv(csv_path)

def max_latency(core1_max, core2_max, core3_max, core4_max):
    i1_max = 0
    i2_max = 0
    i3_max = 0
    i4_max = 0
    for i in range(len(core1_max)-1,0,-1):
        if(core1_max[i] != 0):
            i1_max = i
            break
    for i in range(len(core2_max)-1,0,-1):
        if(core2_max[i] != 0):
            i2_max = i
            break
    for i in range(len(core3_max)-1,0,-1):
        if(core3_max[i] != 0):
            i3_max = i
            break
    for i in range(len(core4_max)-1,0,-1):
        if(core4_max[i] != 0):
            i4_max = i
            break
    max_latency = np.max([i1_max, i2_max, i3_max, i4_max])
    return max_latency


# In[21]:


latency_std = load_csv_data(file_name='histogram_stdkernel.csv')
latency_rt = load_csv_data(file_name='histogram_rtkernel.csv')
latency_rt_docker = load_csv_data(file_name='histogram_rtkernel_docker.csv')


# In[22]:


latency_std = latency_std.set_index('time')
latency_rt = latency_rt.set_index('time')
latency_rt_docker = latency_rt_docker.set_index('time')


# In[23]:


max_latency_std = max_latency(latency_std.core1.values,latency_std.core2.values,latency_std.core3.values,latency_std.core4.values)
max_latency_rt = max_latency(latency_rt.core1.values,latency_rt.core2.values,latency_rt.core3.values,latency_rt.core4.values)
max_latency_rt_docker = max_latency(latency_rt_docker.core1.values,latency_rt_docker.core2.values,latency_rt_docker.core3.values,latency_rt_docker.core4.values)


# In[24]:


mnplt = 0
mxplt = 400
plt.semilogy(latency_std.index[mnplt:mxplt], latency_std.core1[mnplt:mxplt], 'r', label='core1')
plt.semilogy(latency_std.index[mnplt:mxplt], latency_std.core2[mnplt:mxplt], 'b', label='core2')
plt.semilogy(latency_std.index[mnplt:mxplt], latency_std.core3[mnplt:mxplt], 'g', label='core3')
plt.semilogy(latency_std.index[mnplt:mxplt], latency_std.core4[mnplt:mxplt], 'k', label='core4')
plt.title('Latency using Standard Raspbian Kernel (4.14.21-v7+)')
plt.ylabel('Number of latency samples')
plt.xlabel('Latency (us), max %i us' % max_latency_std)
plt.legend()
plt.grid(True)


# In[25]:


mnplt = 0
mxplt = 400
plt.semilogy(latency_rt.index[mnplt:mxplt], latency_rt.core1[mnplt:mxplt], 'r', label='core1')
plt.semilogy(latency_rt.index[mnplt:mxplt], latency_rt.core2[mnplt:mxplt], 'b', label='core2')
plt.semilogy(latency_rt.index[mnplt:mxplt], latency_rt.core3[mnplt:mxplt], 'g', label='core3')
plt.semilogy(latency_rt.index[mnplt:mxplt], latency_rt.core4[mnplt:mxplt], 'k', label='core4')
plt.title('Latency using RT-Preempt Raspbian Kernel (4.14.21-rt17-v7+)')
plt.ylabel('Number of latency samples')
plt.xlabel('Latency (us), max %i us' % max_latency_rt)
plt.legend()
plt.grid(True)


# In[26]:


mnplt = 0
mxplt = 400
plt.semilogy(latency_rt_docker.index[mnplt:mxplt], latency_rt_docker.core1[mnplt:mxplt], 'r', label='core1')
plt.semilogy(latency_rt_docker.index[mnplt:mxplt], latency_rt_docker.core2[mnplt:mxplt], 'b', label='core2')
plt.semilogy(latency_rt_docker.index[mnplt:mxplt], latency_rt_docker.core3[mnplt:mxplt], 'g', label='core3')
plt.semilogy(latency_rt_docker.index[mnplt:mxplt], latency_rt_docker.core4[mnplt:mxplt], 'k', label='core4')
plt.title('Latency using Docker on RT-Preempt Raspbian Kernel (4.14.21-rt17-v7+)')
plt.ylabel('Number of latency samples')
plt.xlabel('Latency (us), max %i us' % max_latency_rt_docker)
plt.legend()
plt.grid(True)


# In[27]:


latency_std.sort_values('core1', ascending=False, inplace=False, kind='quicksort').head()


# In[29]:


latency_rt.sort_values('core1', ascending=False, inplace=False, kind='quicksort').head()


# In[30]:


latency_rt_docker.sort_values('core1', ascending=False, inplace=False, kind='quicksort').head()

