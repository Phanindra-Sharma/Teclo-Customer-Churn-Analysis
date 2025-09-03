#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[32]:


df=pd.read_csv("telco python.csv")


# In[33]:


df = pd.get_dummies(df, columns=['Contract', 'InternetService', 'PaymentMethod'], drop_first=True)

for col in df.select_dtypes(include='bool').columns:
    df[col] = df[col].astype(int)


# In[34]:


service_cols_numeric = ['PhoneServiceFlag'] 
service_cols_object = [ 'MultipleLines','OnlineSecurity','OnlineBackup',
                       'DeviceProtection','TechSupport','StreamingTV','StreamingMovies']


# In[35]:


for col in service_cols_object:
    df[col+'_Flag'] = df[col].map({'Yes':1, 'No':0, 'No internet service':0})


# In[36]:


all_service_flags = service_cols_numeric + [col+'_Flag' for col in service_cols_object]

df['TotalServices'] = df[all_service_flags].sum(axis=1)


# In[37]:


df['HighMonthlyChargesFlag'] = (df['MonthlyCharges'] > 80).astype(int)
df['LongTenureFlag'] = (df['tenure'] > 24).astype(int)


# In[38]:


# Check dtypes
print(df.dtypes)

# Ensure only numeric columns
print(df.select_dtypes(include=['object']).columns)  # should return empty


# In[39]:


obj_cols= ['customerID', 'gender', 'Partner', 'Dependents', 'PhoneService',
       'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
       'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling',
       'Churn']
df= df.drop(columns=obj_cols)


# In[46]:


df.info()


# In[41]:


df['MultipleLines_Flag'] = df['MultipleLines_Flag'].fillna(0)


# In[42]:


df["AvgChargesPerMonth"] = df["TotalCharges"] / (df["tenure"].replace(0, 1))


# In[43]:


df["tenure group"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 60, 72],  
    labels=["0–12", "13–24", "25–48", "49–60", "61–72"]
)


# In[44]:


df = pd.get_dummies(df, columns=["tenure group"], drop_first=True)


# In[45]:


df.to_csv("telco Numeric.csv", index=False)

