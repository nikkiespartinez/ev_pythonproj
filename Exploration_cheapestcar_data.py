#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[23]:


# Importing the file

df = pd.read_csv('Cheapestelectriccars-EVDatabase.csv')


# In[24]:


# Reading the first 5 rows

df.head()


# In[4]:


df.info()


# In[5]:


# last 10 items

df.tail(10)


# In[6]:


df.Range


# In[7]:


range = df.Range[0]
range

range.split(', ')
range
# In[8]:


range_int = range.split(' ')[0]
range_int


# In[25]:


# Function for splitting range data

def convert_range(range):
    range_int = range.split(' ')[0]
    return range_int    


# In[26]:


new_range = df.Range.apply(convert_range)


# In[27]:


new_range.value_counts()


# In[28]:


new_range.head()


# In[29]:


new_range.tail(10)


# In[14]:


df.head()


# In[30]:


# Adding a new column

df['Range Integers'] = df.Range.apply(convert_range)


# In[16]:


df.head()


# In[31]:


# Converting column (str) into an integer
df['Range Integers'] = df['Range Integers'].astype(int)


# In[18]:


df.info()


# In[32]:


conv_fac = 0.621371

# Calc for converting KM to Miles
df['Range Integers'] = (df['Range Integers'] * conv_fac.round(2)


# In[ ]:


df.head()


# In[33]:


df['Range (ml)'] = df['Range Integers']


# In[34]:


df.head()


# In[35]:


df.pop('Range Integers')


# In[36]:


df.info()


# In[37]:


df.head()


# In[38]:


df.info()


# In[39]:


df['Range (ml)'] = df['Range (ml)'].astype(int)


# In[40]:


df.info()


# In[41]:


df.head()


# In[42]:


df.Acceleration


# In[43]:


acceleration = df.Acceleration[0]
acceleration


# In[44]:


acc_int = acceleration.split(' ')[0]
acc_int


# In[45]:


def convert_acceleration(acceleration):
    acc_int = acceleration.split(' ')[0]
    return acc_int


# In[46]:


new_acc = df.Acceleration.apply(convert_acceleration)


# In[47]:


df['Acceleration Int'] = df.Acceleration.apply(convert_acceleration)


# In[48]:


df.info()


# In[49]:


# Converting Acceleration to float from str

df['Acceleration Int'] = df['Acceleration Int'].astype(float)


# In[50]:


df.head()


# In[51]:


df.tail(10)


# In[52]:


# Deleting the old row

df = df.drop('Acceleration', 1)


# In[ ]:


df.head()


# In[53]:


# Renaming columns

df = df.rename(columns={'Acceleration Int': 'Acceleration Per/Sec', 'Range Integers': 'Range (Miles)'})


# In[54]:


df.head()


# In[55]:


# Converting Top Speed into integers

topspeed = df.TopSpeed[0]
topspeed


# In[56]:


# Removing KM/H

topspeed_int = topspeed.split(' ')[0]
topspeed_int


# In[57]:


# Function for splitting range data

def convert_topspeed(topspeed):
    topspeed_int = topspeed.split(' ')[0]
    return topspeed_int 


# In[58]:


new_topspeed = df.TopSpeed.apply(convert_topspeed)


# In[59]:


new_topspeed.head()


# In[60]:


df.head()


# In[61]:


# Adding a new column

df['Top Speed'] = df.TopSpeed.apply(convert_topspeed)
df.head()


# In[62]:


# Deleting TopSpeed old column (KM/H)

df = df.drop(['TopSpeed', 'Range'], 1)
df = df.rename(columns={'Top Speed': 'Top Speed (KM/H)'})
df.head()


# In[63]:


# Rearranging the column positions

df = df[['Name', 
         'Subtitle', 
         'Range (Miles)', 
         'Acceleration Per/Sec', 
         'Top Speed (KM/H)', 
         'Efficiency', 
         'FastChargeSpeed',
         'Drive',
         'NumberofSeats',
         'PriceinGermany',
         'PriceinUK']]

df.head()


# In[64]:


df.Drive


# In[ ]:


df.info()


# In[ ]:


df.head()


# In[65]:


# Indexing front wheel drives

df.Drive == 'Front Wheel Drive'


# In[66]:


# 71 = Front Wheel Drive

df[df.Drive == 'Front Wheel Drive']


# In[67]:


# 64 = All Wheel Drive

df[df.Drive == 'All Wheel Drive']


# In[68]:


df[df.Drive == 'Rear Wheel Drive']


# In[69]:


# Adding up Rear Wheel Drive + Front Wheel Drive + All Wheel Drive

total_rows_rwd = len(df[df.Drive == 'Rear Wheel Drive'])
total_rows_fwd = len(df[df.Drive == 'Front Wheel Drive'])
total_rows_awd = len(df[df.Drive == 'All Wheel Drive'])

sum_total = total_rows_awd + total_rows_fwd + total_rows_rwd

print(f'Sum total of cars with\n Rear Wheel Drive: {total_rows_rwd} \n Front Wheel Drive: {total_rows_fwd} \n All Wheel Drive: {total_rows_awd}')
print(f'All cars total: {sum_total}')


# In[70]:


df = df.rename(columns={'Drive': 'Power'})


# In[71]:


df.head()


# In[ ]:




