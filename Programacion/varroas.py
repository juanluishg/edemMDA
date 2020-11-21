# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:10:59 2020

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
wbr = pd.read_csv ("varroas.csv", sep=',', decimal='.')
print(wbr.shape)
print(wbr.head())
print(wbr.info())
#QC OK


#Recode class
wbr["class_st"] = wbr['class']
wbr.class_st = wbr.class_st.replace(to_replace=0, value="No Varroa")
wbr.class_st = wbr.class_st.replace(to_replace=1, value="Varroa")
#To category
my_categories=["Varroa", "No Varroa"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["class_cat"] = wbr.class_st.astype(my_datatype)
wbr.info()

#frequencies
mytable = pd.crosstab(index=wbr["class_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Varroas')
plt.title('Figure 1. Percentage of Varroas')


#%%
#Mean Comparison
wbr['area (px)'].describe()

plt.hist(wbr['area (px)'])
plt.show()

plt.bar(mytable2.index, mytable2['count'])
plt.show()


#Mean of each group
wbr.groupby('class_cat')['area (px)'].mean()

wbr.groupby('class_cat')['area (px)'].std()

#t test
##Extract two groups
area_v = wbr.loc[wbr.class_cat == 'Varroa', "area (px)"]
area_nv = wbr.loc[wbr.class_cat == 'No Varroa', "area (px)"]

##Statistical test
ttest = stats.ttest_ind(area_v, area_nv, equal_var = False)

m = wbr['area (px)'].mean()
n = wbr['area (px)'].count()
std = wbr['area (px)'].std()

#Plot the test
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="class_cat", y="area (px)", data=wbr, ci=95, join=0)
plt.ylabel(' ')
plt.xlabel("Class")
plt.axhline(y=m, linewidth=1, linestyle='dashed', color="green")
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = 'Mean: ' + str(round(m,1)) + '\nn: ' + str(round(n,0)) + '\nt: ' + str(round(ttest.statistic, 3)) + '\nPValue: ' + str(round(ttest.pvalue, 3))
plt.text(0.85,0.00000450, textstr, bbox=props)
plt.title("Figure 1. Average area by Class.")
plt.show()

#%% Recode Area

twentyfiveQ = wbr['area (px)'].quantile(0.25)
midQ = wbr['area (px)'].quantile(0.5)
seventyfive = wbr['area (px)'].quantile(0.75)


wbr.loc[  (wbr['area (px)']<=(twentyfiveQ)) ,"area_str"]= "Small"
wbr.loc[ ((wbr['area (px)']>(twentyfiveQ)) & (wbr['area (px)']<=(midQ))) ,"area_str"]= "Mid-low"
wbr.loc[ ((wbr['area (px)']>(midQ)) & (wbr['area (px)']<=(seventyfive))) ,"area_str"]= "Mid-High"
wbr.loc[  (wbr['area (px)']>(seventyfive)) ,"area_str"]= "High"

my_categories=["Small", "Mid-low", "Mid-High", "High"]
my_area_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["area_cat"] = wbr.area_str.astype(my_area_type)
wbr.info()

#%%
#Comparacion de porcentajes
##CrossTabulation
pd.crosstab(wbr.area_cat, wbr.class_cat, margins=True)

##Porcentajes de columnas
my_ct = pd.crosstab(wbr.area_cat, wbr.class_cat, normalize='columns', margins=True)*100
print(my_ct)

my_ct = round(my_ct, 1) # my_ct.round(1)


#Statistical Test

ct = pd.crosstab(wbr.area_cat, wbr.class_cat) #tabla de contingencia solo con las variables, sin total y sin porcentanjes

##Prueba de Chi2
stats.chi2_contingency(ct) #OJO! leer comentario ct
#(digito_control, pvalue, etc..)

st = stats.chi2_contingency(ct)


# Graphical Representation
my_ct2 = my_ct.transpose()

my_ct2.plot(kind='bar', edgecolor ='black', colormap='Blues')
plt.ylim(0,100)
text = "Chi2: " +  str(round(st[0],2)) + "\nn: " + str(wbr.area_cat.count()) + "\nP-Value: "+ str(round(st[1],2))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(0, 80, text, bbox=props)
plt.xlabel("Varroa")
plt.ylabel("Area")
plt.title('Figure 2. Area on pixels depend on if its Varroa or not')
plt.show()
