# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:01:48 2020

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
######### Regresion Model ############
from statsmodels.formula.api import ols

#With one predictor
model1 = ols('cnt ~ temp_celsius', data=wbr).fit()
print(model1.summary2())


model2 = ols('cnt ~ windspeed_kh', data=wbr).fit()
print(model2.summary2())


#With two predictors
model3 = ols('cnt ~ temp_celsius + windspeed_kh', data=wbr).fit()
print(model3.summary2())



wbr.hum.hist()
wbr.hum.describe()

model4 = ols('cnt ~ hum', data=wbr).fit()
print(model4.summary2())

model5 = ols('cnt ~ temp_celsius + windspeed_kh + hum', data=wbr).fit()
print(model5.summary2())


#With nominal variable
model6 = ols('cnt ~ workingday', data=wbr).fit()
print(model6.summary2())

model7 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday', data=wbr).fit()
print(model7.summary2())

model8 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr', data=wbr).fit()
print(model8.summary2())

#%%
######Dummy Variable / 1 hot encoding
dummies = pd.get_dummies(wbr.weathersit)

colnames = {1:'sunny', 2:'cloudy', 3:'rainy'} #Diccionario

dummies.rename(columns= colnames, inplace=True)

wbr_dummies = pd.concat([wbr, dummies], axis=1)

pd.crosstab(wbr_dummies.weathersit, wbr_dummies.sunny)
pd.crosstab(wbr_dummies.weathersit, wbr_dummies.cloudy)
pd.crosstab(wbr_dummies.weathersit, wbr_dummies.rainy)
#QC OK

wbr = wbr_dummies

model9 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + rainy + cloudy', data=wbr).fit()
print(model9.summary2())


#Season
dummies = pd.get_dummies(wbr.season)
colname = {1:'winter', 2:'spring', 3:'summer', 4:'autum'}
dummies.rename(columns=colname, inplace=True)
wbr = pd.concat([wbr,dummies], axis=1)


model10 = ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + rainy + cloudy + spring + summer + autum', data=wbr).fit()
print(model10.summary2())


#Variable Squared
wbr['temperature_square'] = wbr.temp_celsius * wbr.temp_celsius

model11 = ols('cnt ~ temp_celsius + temperature_square + windspeed_kh + hum + workingday + yr + rainy + cloudy + spring + summer + winter', data=wbr).fit()
print(model11.summary2())

#%%
#####Generate Reports#####
#!pip install stargazer
from stargazer.stargazer import Stargazer

stargazer = Stargazer([model1, model2, model4, model3, model5])
html = stargazer.render_html()

from bs4 import BeautifulSoup as bs
soup = bs(html)                #make BeautifulSoup
prettyHTML = soup.prettify()   #prettify the html
print(prettyHTML)
