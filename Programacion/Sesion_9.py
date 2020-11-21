# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:57:38 2020

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

###########Histogram of rentals

x = wbr.cnt
n = wbr.cnt.count()
m = wbr.cnt.mean()
std = wbr.cnt.std()


plt.hist(x, edgecolor='black', color='green', bins=12) #bins: numero de columnas
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)

plt.title('Figure 1. Histogram number of rentals')

plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency')

textstr = 'Mean = ' + str(round(m,1)) + '\nS.D = ' + str(round(std,1)) + '\nn = ' + str(round(n,0))
plt.text(6100,95, textstr)

plt.axvline(x=m, linewidth=1.2, linestyle='solid', color='red', label='Mean')#Linea vertical

plt.show()



###########Histogram of temperature
x = wbr.temp_celsius
n = x.count()
m = x.mean()
std = x.std()


plt.hist(x, edgecolor='black', color='green', bins=12) #bins: numero de columnas
ticks = np.arange(0, 40, 5)
plt.xticks(ticks)

plt.title('Figure 2. Histogram temperature')

plt.xlabel('Temperature ºC')
plt.ylabel('Frecuency')

textstr = 'Mean = ' + str(round(m,1)) + '\nS.D = ' + str(round(std,1)) + '\nn = ' + str(round(n,0))
plt.text(2,75, textstr)

plt.axvline(x=m, linewidth=1.2, linestyle='solid', color='red', label='Mean')#Linea vertical

plt.show()

#QC OK

#%%
#Scatter Plot

###Temperature X Number Rentals
x = wbr.temp_celsius
y = wbr.cnt
n=y.count()

plt.scatter(wbr.temp_celsius, wbr.cnt)

plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', edgecolors='C0')
plt.title("Figure 3. Daily bicycle rentals, by temperature\n")
textstr = 'n = ' + str(round(n,0))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(3,7000, textstr, bbox=props)
plt.yticks(np.arange(0,10000, 1000))
plt.xticks(np.arange(0,40,5))
plt.ylabel("Daily rentals")
plt.xlabel("Temperature ºC")
plt.show()

### Wind speed X Number Rentals
x = wbr.windspeed_kh
y = wbr.cnt
n=y.count()

plt.scatter(wbr.windspeed_kh, wbr.cnt)

plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', edgecolors='C0')
plt.title("Figure 3. Daily bicycle rentals, by windspeed\n")
textstr = 'n = ' + str(round(n,0))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(30,7000, textstr, bbox=props)
plt.yticks(np.arange(0,10000, 1000))
#plt.xticks(np.arange(0,40,5))
plt.ylabel("Daily rentals")
plt.xlabel("Wind Speed (Km/h)")
plt.show()

#%%
#Correlation
from scipy.stats.stats import pearsonr

pearsonr(wbr.temp_celsius, wbr.cnt)

###Temperature X Number Rentals
x = wbr.temp_celsius
y = wbr.cnt
n=y.count()

res = pearsonr(x, y)
r1, p_val2 = pearsonr(x, y) #r1: coeficiente de correlacion; p_val2: p-value
print(r1, p_val2)

plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', edgecolors='C0')
plt.title("Figure 4. Correlation Daily bicycle rentals, by temperature\n")
textstr = 'r = '+ str(round(r1, 2)) + '\nP.Value = '+ str(round(p_val2, 4)) +'\nn = ' + str(round(n,0))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(3,7000, textstr, bbox=props)
plt.yticks(np.arange(0,10000, 1000))
plt.xticks(np.arange(0,40,5))
plt.ylabel("Daily rentals")
plt.xlabel("Temperature ºC")
plt.show()

###WindSpeed X Number Rentals
x = wbr.windspeed_kh
y = wbr.cnt
n=y.count()

res = pearsonr(x, y)
r1, p_val2 = pearsonr(x, y) #r1: coeficiente de correlacion; p_val2: p-value
print(r1, p_val2)

plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', edgecolors='C0')
plt.title("Figure 5. Correlation Daily bicycle rentals, by wind speed\n")
textstr = 'r = '+ str(round(r1, 2)) + '\nP.Value = '+ str(round(p_val2, 4)) +'\nn = ' + str(round(n,0))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(25,7000, textstr, bbox=props)
plt.yticks(np.arange(0,10000, 1000))
plt.xticks(np.arange(0,40,5))
plt.ylabel("Daily rentals")
plt.xlabel("Wind Speed (Km/h)")
plt.show()

#%%
#By Year
###Temperature X Number Rentals

plt.figure(figsize=(5,5))
plt.scatter('temp_celsius', 'cnt', data=wbr, c='yr')
plt.show()


#By Season
###Temperature X Number Rentals

plt.figure(figsize=(5,5))
plt.scatter('temp_celsius', 'cnt', data=wbr, c='season')
plt.show()

#%%
#Graphic Representation
x = wbr.temp_celsius
y = wbr.cnt
n=y.count()

r1, p_val2 = pearsonr(x, y) #r1: coeficiente de correlacion; p_val2: p-value


plt.figure(figsize=(5,5))
plt.scatter(wbr.temp_celsius[wbr.yr == 0], wbr.cnt[wbr.yr == 0], s=20, 
            marker='s', facecolor='none', edgecolor='C0', label='2011')
plt.scatter(wbr.temp_celsius[wbr.yr == 1], wbr.cnt[wbr.yr == 1], s=20, 
            marker='^', facecolor='none', edgecolor='C1', label='2012')
plt.legend(loc="upper right")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = 'r = '+ str(round(r1, 2)) + '\nP.Value = '+ str(round(p_val2, 4)) +'\nn = ' + str(round(n,0))
plt.text(3, 7500, textstr, bbox=props)
plt.title("Figure 6. Daily bicycle by temperature.\n")
plt.ylabel("Daily rentals")
plt.xlabel("Temperature ºC")
plt.yticks(np.arange(0,10000,1000))
plt.savefig("figures/twoYearsByTempAndRentals.svg")
plt.show()

