#!/usr/bin/env python
# coding: utf-8

# #Categorical data

# In[1]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/codebasics/py/master/ML/5_one_hot_encoding/Exercise/carprices.csv')
df.head()


# In[3]:


newdf = df.rename(columns= {'Car Model':'carsmodel','Sell Price($)':'sellprice','Age(yrs)':'age'})
newdf


# In[4]:


newdf1 = pd.get_dummies(newdf.carsmodel)
newdf1


# In[5]:


dataframe = pd.concat([newdf,newdf1],axis=1)
dataframe


# In[6]:


dataframe = dataframe.drop(['carsmodel','Audi A5'],axis=1)
dataframe

