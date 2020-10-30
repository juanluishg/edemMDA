# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:03:28 2020

@author: JuanLu
"""


#%reset -f
#%%
###############################################################################
# Washinton Denormalized                                                      #
###############################################################################
# Load basic libraries
import os # Acceder desde python al S.O
import pandas as pd # Libreria de datasets, matrices de datos desde python
import numpy as np # Operaciones de calculo
import matplotlib.pyplot as plt # Libreria de gráficos

# Expandir terminal
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


os.getcwd()

# Change working directory
os.chdir("C:/Users/JuanLu/Dropbox/I.Informatica/Master/edemMDA/Programacion")
os.getcwd()

#Load dataframe
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=";", decimal=",")

print(wbr.head())

#Add calculate columns
wbr['casual_ratio'] = wbr.casual/wbr.registered


#See related variables
wbr.casual_ratio.describe()

plt.hist(wbr.casual_ratio) # Se ve claramente que hay dos regiones. ¿PQ?

#Dias festivos tienen algo q ver?
#Groupby workings days
wbr.groupby(['workingday']).casual_ratio.describe()

wbr.groupby(['workingday']).casual_ratio.hist()

#%%
#Recoding

#Cambiar numero (1,2,3,4) por la estación en nombre(Winter, Summer,...)
print(wbr.groupby(['season']).size())


wbr.loc[:, 'season_cat'] = None #Filas : Columnas

wbr = wbr.drop(columns="season_cat")

wbr.head()

#Recoding always new column
wbr.loc[ (wbr.season == 1), "season_cat"] = "Winter"
wbr.loc[ (wbr.season == 2), "season_cat"] = "Spring"
wbr.loc[ (wbr.season == 3), "season_cat"] = "Summer"
wbr.loc[ (wbr.season == 4), "season_cat"] = "Autum"

print(wbr[100:110])

#Quality control
pd.crosstab(wbr.season, wbr.season_cat)
#QC OK


x = wbr.cnt
m = wbr.cnt.mean()
std = wbr.cnt.std() 
n = wbr.cnt.count()

#Recondig using ranges
plt.hist(x, edgecolor='black', color='green') #bins: numero de columnas
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)

plt.title('Figure 1. Daily Gicycle rentals in Washington DC \n by Capital bikeshare. 2011-2012')

plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency')

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = 'Mean = ' + str(round(m,1)) + '\nS.D = ' + str(round(std,1)) + '\nn = ' + str(round(n,0))
plt.text(6600,95, textstr, bbox=props)

plt.axvline(x=m, linewidth=1.2, linestyle='solid', color='red', label='Mean')#Linea vertical
plt.axvline(x=m-std, linewidth=1.2, linestyle='dashed', color='blue', label='-1 S.D')#Linea vertical
plt.axvline(x=m+std, linewidth=1.2, linestyle='dashed', color='blue', label='+1 S.D')#Linea vertical

plt.show()

#Using quartiles
wbr.cnt.describe()

print("Lower limit: "+str(round(m-std,1)))
print("Average limit: "+str(m))
print("Upper limit: "+str(round(m+std,1)))
lw = m-std
ul = m+std

##Recode 1
wbr.loc[ (wbr['cnt'] < lw) , "cnt_cat2"] = "Low rentals"
wbr.loc[ ((wbr['cnt'] >= lw) & (wbr['cnt'] < ul)), "cnt_cat2"] = "Average rentals"
wbr.loc[ (wbr['cnt'] >= ul) , "cnt_cat2"] = "High rentals"

wbr.head()

#frequencies
mytable = pd.crosstab(index=wbr['cnt_cat2'], columns="counts")
print(mytable)

n=mytable.sum()
mytable2 = (mytable/n) * 100
print(mytable2)

plt.bar(mytable2.index, mytable2['counts'])

wbr.info()


#Quality control?
plt.scatter(wbr.cnt, wbr.cnt_cat2, s=1)
plt.axvline(x=lw, linewidth=1.2, linestyle='dashed', color='red', label="Lower Limit")
plt.axvline(x=ul, linewidth=1.2, linestyle='dashed', color='green', label="Upper limit")
plt.title("Check recoding rentals")
plt.xlabel("Rentals per day")
plt.legend()
plt.show()
#QC OK

#Crate categorical variable
##Not good method
wbr["cnt_cat3"] = wbr.cnt_cat2.astype("category")
wbr.info()
#Drop column
wbr = wbr.drop('cnt_cat3', axis=1)


##Good method
from pandas.api.types import CategoricalDtype
#Define specific order
my_order = ["Low rentals", "Average rentals", "High rentals"]
#Create object categorical type
my_rentals_type = CategoricalDtype(categories=my_order, ordered=True)

#Set type on dataframe
wbr["cnt_cat4"] = wbr.cnt_cat2.astype(my_rentals_type)


wbr.info()

#frequencies
mytable = pd.crosstab(index=wbr['cnt_cat4'], columns="counts")
print(mytable)

n=mytable.sum()
mytable2 = (mytable/n) * 100
print(mytable2)

plt.bar(mytable2.index, mytable2['counts'])
