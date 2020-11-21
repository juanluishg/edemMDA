# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:59:44 2020

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

#Recoding DV for analysis
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(m+sd)) ,"cnt_str"]= "High rentals"

### Recode cnt to ordinal
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

#frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])
plt.show()

#######################
# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No","Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 1. Percentage of Working Days')
plt.show()

#%%
#Comparacion de porcentajes
##CrossTabulation
pd.crosstab(wbr.cnt_cat, wbr.wd_cat, margins=True)

##Porcentajes de columnas
my_ct = pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize='columns', margins=True)*100
print(my_ct)

my_ct = round(my_ct, 1) # my_ct.round(1)


#Statistical Test

ct = pd.crosstab(wbr.cnt_cat, wbr.wd_cat) #tabla de contingencia solo con las variables, sin total y sin porcentanjes

##Prueba de Chi2
stats.chi2_contingency(ct) #OJO! leer comentario ct
#(digito_control, pvalue, etc..)

st = stats.chi2_contingency(ct)


# Graphical Representation
my_ct2 = my_ct.transpose()

my_ct2.plot(kind='bar', edgecolor ='black', colormap='Blues')
plt.ylim(0,100)
text = "Chi2: " +  str(round(st[0],2)) + "\nn: " + str(wbr.cnt_cat.count()) + "\nP-Value: "+ str(round(st[1],2))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(0, 80, text, bbox=props)
plt.xlabel("Working Day")
plt.ylabel("Percentage of rentals")
plt.title('Figure 2. Number of rentals depend on Working Day')
plt.show()


#%%
# By Weather situation
# Recode weather situation
wbr["ws_st"] = wbr.weathersit
wbr.ws_st = wbr.ws_st.replace(to_replace=1, value="Sunny")
wbr.ws_st = wbr.ws_st.replace(to_replace=2, value="Cloudy")
wbr.ws_st = wbr.ws_st.replace(to_replace=3, value="Rainy")
#To category
my_categories = ["Sunny", "Cloudy", "Rainy"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["ws_cat"] = wbr.ws_st.astype(my_datatype)
wbr.info()

#Describe
# Barchart for Weather Situation
mytable = pd.crosstab(index=wbr["ws_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Weather Situation')
plt.title('Figure 3. Percentage of Weather Situation')
plt.show()

# Barchart for Rentals
mytable = pd.crosstab(index=wbr["cnt_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Rentals')
plt.title('Figure 4. Percentage of Rentals')
plt.show()


#Comparacion de porcentajes
my_ct = pd.crosstab(wbr.cnt_cat, wbr.ws_cat, normalize='columns', margins=True)*100
print(my_ct)
my_ct = round(my_ct, 1) # my_ct.round(1)


#Statistical Test

ct = pd.crosstab(wbr.cnt_cat, wbr.ws_cat) #tabla de contingencia solo con las variables, sin total y sin porcentanjes

##Prueba de Chi2
st = stats.chi2_contingency(ct) #OJO! leer comentario ct
#(digito_control, pvalue, etc..)

# Graphical Representation
my_ct2 = my_ct.transpose()

my_ct2.plot(kind='bar', edgecolor ='black', colormap='Blues')
plt.ylim(0,100)
text = "Chi2: " +  str(round(st[0],2)) + "\nn: " + str(wbr.cnt_cat.count()) + "\nP-Value: "+ str(round(st[1],2))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(0, 80, text, bbox=props)
plt.xlabel("Weather Situation")
plt.ylabel("Percentage of rentals")
plt.title('Figure 5. Number of rentals depend on Weather Situation')
plt.show()

#%%
#V de Cramer
## Mas cerca de 1 mayor relación. 0 ninguna
def cramers_corrected(confusion_matrix):
    chi2 = stats.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))    
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))

## Test with Weather situation
#Statistical Test

ct = pd.crosstab(wbr.cnt_cat, wbr.ws_cat) #tabla de contingencia solo con las variables, sin total y sin porcentanjes

# Prueba de V de Cramer
v = cramers_corrected(ct)
print("Number of rentals and weather situation")
print("Cramer's V: " + str(v))


## Test with Working Day
#Statistical Test

ct = pd.crosstab(wbr.cnt_cat, wbr.wd_cat) #tabla de contingencia solo con las variables, sin total y sin porcentanjes

# Prueba de V de Cramer
v = cramers_corrected(ct)
print("Number of rentals and working day")
print("Cramer's V: " + str(v))
#%%
# Graficos de mosaicos
from statsmodels.graphics.mosaicplot import mosaic

mosaic(wbr, ['cnt_cat', 'ws_cat'], title='Figure 6. Mosaic Graph of Number of Rentals and Weather Situation')

mosaic(wbr, ['cnt_cat', 'wd_cat'], title='Figure 6. Mosaic Graph of Number of Rentals and Working Day')
#%%
#Guardar entorno
#!pip install dill

#import dill

#dill.dump_session("entorno_sesion_8.pkl")

#Recuperar sesion
#dill.load_session("entorno_sesion_8.pkl")