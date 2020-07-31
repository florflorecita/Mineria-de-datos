#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import missingno as msno


# In[4]:


datitosRL=pd.read_csv('C:\\Users\\amand\\Desktop\\DIPLOMADO\\MINERÍA DE DATOS\\Practica 01\\bank.csv',sep=';')


# In[5]:


datitosRL.head()


# In[6]:


datitosRL.shape


# In[7]:


datitosRL.columns.values


# In[8]:


datitosRL.dtypes


# In[9]:


msno.matrix(datitosRL)


# In[10]:


datitosRL["education"] = np.where(datitosRL["education"]=="basic.4y", "Basic", datitosRL["education"])
datitosRL["education"] = np.where(datitosRL["education"]=="basic.6y", "Basic", datitosRL["education"])
datitosRL["education"] = np.where(datitosRL["education"]=="basic.9y", "Basic", datitosRL["education"])

datitosRL["education"] = np.where(datitosRL["education"]=="high.school", "High School", datitosRL["education"])
datitosRL["education"] = np.where(datitosRL["education"]=="professional.course", "Professional Course", datitosRL["education"])
datitosRL["education"] = np.where(datitosRL["education"]=="illiterate", "Illiterate", datitosRL["education"])
datitosRL["education"] = np.where(datitosRL["education"]=="unknown", "Unknown", datitosRL["education"])


# In[11]:


datitosRL.describe()


# In[12]:


datitosRL.groupby("y").count()


# In[13]:


datitosRL.groupby("y").mean()


# In[48]:


datitosRL.groupby("education").mean()


# In[49]:


get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(datitosRL.education, datitosRL.y).plot(kind="bar")
plt.title("Frecuencia de compra en función del nivel de educación")
plt.xlabel("Nivel de educación")
plt.ylabel("Frecuencia de compra del producto")


# In[50]:


datitosRL.groupby("marital").mean()


# In[51]:


get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(datitosRL.marital, datitosRL.y).plot(kind="bar")
plt.title("Frecuencia de compra en función del estado civil")
plt.xlabel("Estado civil")
plt.ylabel("Frecuencia de compra del producto")


# In[52]:


datitosRL.groupby("month").mean()


# In[53]:


get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(datitosRL.month, datitosRL.y).plot(kind="bar")
plt.title("Frecuencia de compra en función del mes")
plt.xlabel("Mes")
plt.ylabel("Frecuencia de compra del producto")


# In[54]:


datitosRL.groupby("age").mean()


# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(datitosRL.age, datitosRL.y).plot(kind="bar")
plt.title("Frecuencia de compra en función de la edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia de compra del producto")


# In[56]:


plt.hist(datitosRL['age'])


# In[57]:


datitosRL.groupby("job").mean()


# In[58]:


datitosRL.groupby("job").count()


# In[59]:


get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(datitosRL.job, datitosRL.y).plot(kind="bar")
plt.title("Frecuencia de compra en función del trabajo")
plt.xlabel("Trabajo")
plt.ylabel("Frecuencia de compra del producto")


# In[60]:


datitosRL.groupby("housing").mean()


# In[61]:


get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(datitosRL.housing, datitosRL.y).plot(kind="bar")
plt.title("Frecuencia de compra en función desi tienen un crédito hipotecario")
plt.xlabel("Crédito hipotecario")
plt.ylabel("Frecuencia de compra del producto")


# In[37]:


datitosRL.groupby("loan").mean()


# In[38]:


get_ipython().run_line_magic('matplotlib', 'inline')
pd.crosstab(datitosRL.loan, datitos.y).plot(kind="bar")
plt.title("Frecuencia de compra en función desi tienen un crédito personal")
plt.xlabel("Crédito personal")
plt.ylabel("Frecuencia de compra del producto")


# In[62]:


datitosRL["y"] = (datitosRL["y"]=="yes").astype(int)


# In[63]:


datitosRL["y"]


# In[65]:





# In[66]:


data_corr=datitosRL[["age","duration","campaign","pdays","previous","emp.var.rate","cons.price.idx","cons.conf.idx","euribor3m","nr.employed","y"]]


# In[68]:


plt.figure(figsize=(20,10))
sn.heatmap(data_corr.corr(), annot=True)
plt.show()


# In[71]:


datitosRL.groupby(["age", "marital", "education"]).count()


# In[74]:


plt.boxplot(datitosRL['age'], showmeans=True, meanline=True)
plt.ylabel('Edad')
plt.title('Box Plot de edad')


# In[ ]:





# In[ ]:




