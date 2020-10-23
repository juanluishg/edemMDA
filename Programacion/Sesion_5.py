# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:06:05 2020

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

os.getcwd()

# Change working directory
os.chdir("C:/Users/JuanLu/Dropbox/I.Informatica/Master/edemMDA/Programacion")
os.getcwd()

#Load dataframe
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=";", decimal=",")

#Check
print(wbr.shape)
print(wbr.head())
print(wbr.tail())
#QC OK


plt.hist(wbr.cnt)

#%%

# Select subsamples from a dataframe

# Explore variable year
year = wbr.groupby(['yr']).size()
print(year)

#Percentages
n = year.sum()
year_percentage = (year/n)*100
print(year_percentage)


## Subset by year

# Subset year 0
wbr_2011 = wbr[wbr.yr == 0]

plt.hist(wbr_2011.cnt)
wbr_2011.cnt.describe()

# Subset year 1
wbr_2012 = wbr[wbr.yr == 1]

plt.hist(wbr_2012.cnt)
wbr_2012.cnt.describe()

# Exercise 1A: histogram Bike rentals on Winter of 2012
wbr_winter_2012 = wbr[(wbr.yr == 1) & (wbr.season == 1)]
plt.hist(wbr_winter_2012.cnt)

wbr_winter_2012.cnt.describe()

# Exercise 1B: histogram Bike rentals on Winter and Fall
wbr_winter_fall = wbr[(wbr.season == 1) | (wbr.season == 4)]
plt.hist(wbr_winter_fall.cnt)

wbr_winter_fall.cnt.describe()

#######
wbr_winter_fall.groupby(['season']).size()
#QC OK

wbr_winter_fall.hist()


#%%
# Exercise 2: wbr_ue.csv

#%reset -f
###############################################################################
# Washinton UE                                                                #
###############################################################################
# Load basic libraries
import os # Acceder desde python al S.O
import pandas as pd # Libreria de datasets, matrices de datos desde python
import numpy as np # Operaciones de calculo
import matplotlib.pyplot as plt # Libreria de gráficos

os.getcwd()

# Change working directory
os.chdir("C:/Users/JuanLu/Dropbox/I.Informatica/Master/edemMDA/Programacion")
os.getcwd()

##Load dataframe
wbr_ue= pd.read_csv('wbr_ue.csv', sep=";", decimal=",")

print(wbr_ue.head())
print(wbr_ue.shape)

#Select variables
my_vars = ['temp_celsius', 'cnt']

#Select columns of variables
wbr_minimal = wbr_ue[my_vars]
print(wbr_minimal.shape)
print(wbr_minimal.head())
#QC OK

#Save dataframe
wbr_minimal.to_csv('wbr_ue_minimal.csv')


##############################################################################

#Exercise 2: Describe average temperature and std

print(wbr_ue.temp_celsius.mean())

print(wbr_ue.temp_celsius.std())


plt.hist(wbr_ue.temp_celsius) #Always plot your data

print(wbr_ue.temp_celsius.describe())

#QC KO

## Clean data
wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99,np.nan)

wbr_ue.temp_celsius_c.describe()

#QC OK

plt.hist(wbr_ue.temp_celsius_c)

#Drop NaN
wbr_ue.temp_celsius_c.dropna() #### Missing values

plt.hist(wbr_ue.temp_celsius_c.dropna())


plt.hist(wbr_ue.temp_celsius_c.dropna(), edgecolor="black")


wbr_ue2 = wbr_ue.dropna()

print(wbr_ue.shape)
print(wbr_ue2.shape)

## Dataframe fail
print(wbr_ue.shape) # 365 * 2 = 730 != 732 

print(wbr_ue.instant)

#Select duplicate row
print(wbr_ue[wbr_ue.duplicated(['instant'])])
duplicate = wbr_ue[wbr_ue.duplicated(['instant'])]

#Delete duplicate row
wbr_ue_noD = wbr_ue.drop(duplicate.index)

wbr_ue_noD.shape

print(wbr_ue[wbr_ue.instant==397])
print(wbr_ue_noD[wbr_ue_noD.instant==397])
