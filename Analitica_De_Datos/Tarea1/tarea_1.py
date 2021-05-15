#!/usr/bin/env python
# coding: utf-8

# # House Price

# ## Import Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC, SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
import xgboost as xgb


# In[2]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# ## Load Dataset

# In[3]:


df = pd.read_csv("houseprice.csv", sep=";", decimal=",")
df.head()


# ### Explore Dataset

# In[4]:


df.dtypes


# In[5]:


df.describe()


# In[6]:


df.corr()


# In[7]:


#Distribution of data
df.SalePrice.hist()


# In[202]:


#Search outliers
sns.pairplot(df)


# In[8]:


sns.set_theme(style="white")

# Generate a large random dataset
rs = np.random.RandomState(33)

# Compute the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# In[9]:


#How many NaN
df.isna().sum()


# In[10]:


df.shape


# In[11]:


df.head(1)


# ### Delete NaN

# In[46]:


df_cl = df.copy()


# In[47]:


df_cl = df_cl.dropna(subset=['MSZoning', 'Utilities', 'Exterior1st', 'Exterior2nd', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'KitchenQual', 'Functiol', 'GarageCars', 'GarageArea', 'SaleType'])


# In[48]:


df_cl.shape


# In[49]:


df_cl.isna().sum()


# In[50]:


df_cl = df_cl.drop(["Alley", "PoolQC", "Fence", "MiscFeature"], axis=1)


# In[51]:


cols_nona = df_cl.columns[df_cl.notna().all()]


# In[109]:


df_nona = df_cl[cols_nona].copy()


# In[110]:


df_nona.isna().sum()


# In[111]:


#Type of variables
df_nona.dtypes


# ### Create dummy variables

# In[112]:


df_objects = df_nona.select_dtypes(include='object')


# In[113]:


for c in df_objects.columns.values:
    dummy = pd.get_dummies(df_nona[c])
    df_nona = pd.concat([df_nona, dummy], axis=1)
    df_nona = df_nona.drop(c, axis=1)


# In[114]:


df_nona.dtypes


# In[127]:


len(dummy_columns)


# In[130]:


df_combine = df_nona.groupby(df_nona.columns, axis=1).sum()


# In[133]:


df_combine.head()


# ## Models

# In[134]:


df_combine = df_combine.drop("Id", axis=1)


# ### Standard Data

# In[147]:


std = StandardScaler()
df_scale = std.fit_transform(df_combine)
df_scale = pd.DataFrame(df_scale, columns=df_combine.columns.values)


# In[148]:


df_scale.shape


# In[149]:


df_scale.head()


# ### Train Test Split

# In[150]:


X = df_scale.drop("SalePrice", axis=1)
y = df_scale["SalePrice"]


# In[151]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# In[152]:


X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.15, random_state=42)


# ### Linear Regression

# In[153]:


lr = LinearRegression(normalize=False, n_jobs=-1)
lr.fit(X_train, y_train)
lr.score(X_val, y_val)


# ### Select Variables

# In[154]:


print(X_train.shape)
print(X_train.columns.unique().shape)


# #### XGBoost

# In[156]:


xgbR = xgb.XGBRegressor()
xgbR.fit(X_train, y_train)
xgbR.score(X_val, y_val)


# In[164]:


fig, ax = plt.subplots(1,1, figsize=(20,50))
xgb.plot_importance(xgbR, ax=ax)
plt.show()


# In[174]:


len(xgbR.feature_importances_[np.where(xgbR.feature_importances_>0)])


# #### Best Variables

# In[185]:


selected_variables = X_train.columns.values[np.where(xgbR.feature_importances_>np.median(xgbR.feature_importances_))]


# In[186]:


selected_variables


# In[188]:


std = StandardScaler()
selected_variables = np.append(selected_variables, "SalePrice")
df_scale = std.fit_transform(df_combine[selected_variables])
df_scale = pd.DataFrame(df_scale, columns=selected_variables)
X = df_scale.drop("SalePrice", axis=1)
y = df_scale["SalePrice"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.15, random_state=42)


# ### SVR

# In[189]:


svr = SVR(kernel="linear")
svr.fit(X_train, y_train)
svr.score(X_val, y_val)


# In[190]:


kernel = ['linear', 'poly', 'rbf', 'sigmoid']
C = np.arange(0.1, 1.5, 0.1)
epsilon = [0.01,0.1,0.5]
res = []


# In[191]:


print("Number of iterations: ",(len(kernel)*len(C)*len(epsilon)))


# In[192]:


get_ipython().run_line_magic('time', '')
i=1
for k in kernel:
    for c in C:
        for e in epsilon:
            print("Iteration: {} -- SVR with {} C={} Epsilon={}".format(i,k,c,e))
            svr = SVR(kernel=k, C=c, epsilon=e)
            svr.fit(X_train, y_train)
            print("Score: ",svr.score(X_val, y_val))
            y_pred = svr.predict(X_val)
            res.append({"c":c, "e": e, "kernel":k, "acc":svr.score(X_val, y_val), "mae":mean_absolute_error(y_val, y_pred) ,"mse":mean_squared_error(y_val, y_pred)})
            i+=1


# In[193]:


minMae = 1000000
minConf = 0
for i in res:
    if i["mae"] < minMae:
        minMae = i["mae"]
        minConf = i


# In[194]:


minMae


# In[195]:


minConf


# In[196]:


svrFinal = SVR(C=minConf["c"], epsilon=minConf["e"], kernel=minConf["kernel"])
svrFinal.fit(X_train, y_train)


# In[197]:


y_pred = svrFinal.predict(X_test)
print("Test MAE: ", mean_absolute_error(y_test, y_pred))
print("Test MSE: ", mean_squared_error(y_test, y_pred))


# In[198]:


y_pred = svrFinal.predict(X)
y_pred = pd.DataFrame({"SalePrice":y_pred})
res = pd.concat([y_pred, X], axis=1)
res = std.inverse_transform(res)


# In[201]:


print("Test MAE: ", mean_absolute_error(df_combine["SalePrice"], y_pred))
print("Test MSE: ", mean_squared_error(df_combine["SalePrice"], y_pred))


# In[ ]:




