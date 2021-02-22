# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:57:02 2020

@author: JuanLu
"""


#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#%reset -f   

#load basiclibraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# New libraries
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import scipy.stats as stats  # For statistical inference 
import seaborn as sns  # For hi level, Pandas oriented, graphics
from statsmodels.formula.api import ols #Lineal regresions


# Expandir terminal
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Get working directory
os.getcwd()

# Change working directory
os.chdir("C:/Users/JuanLu/Dropbox/I.Informatica/Master/edemMDA/Programacion")
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
print(wbr.shape)
print(wbr.head())
print(wbr.info())
#QC OK

#%%
model1 = ols("cnt ~ temp_celsius", data=wbr).fit()
print(model1.summary2())

model2 = ols("cnt ~ temp_celsius + windspeed_kh", data=wbr).fit()
print(model2.summary2())

model3 = ols("cnt ~ windspeed_kh", data=wbr).fit()
print(model3.summary2())

model4 = ols("cnt ~ temp_celsius + windspeed_kh + yr", data=wbr).fit()
print(model4.summary2())

wbr['temp_square'] = wbr.temp_celsius ** 2

model5 = ols("cnt ~ temp_celsius + windspeed_kh + temp_square", data=wbr).fit()
print(model5.summary2())

#Hot encoding
dummies = pd.get_dummies(wbr.weathersit)
colname = {1:'sunny', 2:'cloudy', 3:'rainy'}
dummies.rename(columns=colname, inplace=True)
wbr = pd.concat([wbr,dummies], axis=1)

#QC?
pd.crosstab(wbr.weathersit, wbr.sunny)
pd.crosstab(wbr.weathersit, wbr.cloudy)
pd.crosstab(wbr.weathersit, wbr.rainy)
#QC OK

model6 = ols("cnt ~ temp_celsius + windspeed_kh + cloudy + rainy", data=wbr).fit()
print(model6.summary2())

#%%
###### Logistic Regresion #####
print(wbr.cnt.mean())
wbr.cnt.hist()

#Recoding
wbr.loc[(wbr.cnt > wbr.cnt.mean()), 'goal'] = 1
wbr.loc[(wbr.cnt <= wbr.cnt.mean()), 'goal'] = 0

plt.scatter(wbr.cnt, wbr.goal)
#QC OK

from statsmodels.formula.api import logit
model_l1 = logit('goal ~ temp_celsius', data=wbr).fit()
print(model_l1.summary2())


model_l2 = logit('goal ~ temp_celsius + temp_square', data=wbr).fit()
print(model_l2.summary2())

model_l3 = logit('goal ~ temp_celsius + temp_square + windspeed_kh + cloudy + rainy', data=wbr).fit()
print(model_l3.summary2())

model_l4 = logit('goal ~ temp_celsius + temp_square + windspeed_kh + cloudy + rainy + yr', data=wbr).fit()
print(model_l4.summary2())
