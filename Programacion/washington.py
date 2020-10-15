# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:51:13 2020

@author: JuanLu
Capital Bikeshare Washington
"""
#%reset -f

#%%
###############################################################################
# Import datasets                                                             #
###############################################################################
# Load basiclibraries
import os # Acceder desde python al S.O
import pandas as pd # Libreria de datasets, matrices de datos desde python
import numpy as np # Operaciones de calculo
import matplotlib.pyplot as plt # Libreria de gráficos

os.getcwd()
os.chdir("C:/Users/JuanLu/Dropbox/I.Informatica/Master/edemMDA/Programacion")

#Load rentals
rentals_2011 = pd.read_csv("washington_bike_rentals_2011.csv", sep=";", decimal=",")

rentals_2011.shape
rentals_2011.head()
rentals_2011.tail()
#QC OK

# Select the variable
casual = rentals_2011.casual
reg = rentals_2011.registered
cnt = rentals_2011.cnt

#Plot
plt.hist(cnt)

plt.hist(casual)

plt.hist(reg, edgecolor='black') #Poner las lineas negras de las barras
plt.xticks(np.arange(0, 7000, step=1000)) # Mostrar del 0 al 6000 con saltos de 1000
plt.title("Figure 1. Registered rentals in Washington")
plt.show()

plt.hist(casual, edgecolor='black') #Poner las lineas negras de las barras
plt.xticks(np.arange(0, 7000, step=1000)) # Mostrar del 0 al 6000 con saltos de 1000
plt.title("Figure 2. Casuals rentals in Washington")
plt.show()

del(casual, cnt, reg)

#Load wather
weather_2011 = pd.read_csv('weather_washington_2011.csv', sep=";", decimal=",")

weather_2011.shape

weather_2011.dtypes

weather_2011.head()
weather_2011.tail()
#QC OK


# Merge two dataframes
rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on="day") #Por clave "day". Es uniqueId que identifica los casos

#Check
rentals_weather_2011.shape
rentals_weather_2011.head()
#QC NO

#Date is duplicate. Drop column dteday_y
rentals_weather_2011 = rentals_weather_2011.drop(columns=['dteday_y'])

#Rename a column. dteday_x as dteday
rentals_weather_2011 = rentals_weather_2011.rename(columns={'dteday_x' : 'dteday'})

rentals_weather_2011.shape
rentals_weather_2011.head()
#QC OK

plt.scatter(rentals_weather_2011.temp_celsius, rentals_weather_2011.cnt)
plt.xticks(np.arange(0, 35, step=5))
plt.title("Figure 3. Temperature vs Rentals")
plt.xlabel("Temperature ºC")
plt.ylabel("Number Rentals")
plt.show()

#Add new cases
#Load rental_weather_2012
rentals_weather_2012 = pd.read_csv('rentals_weather_2012.csv', sep=";", decimal=",")

rentals_weather_2011.shape
rentals_weather_2012.shape

rentals_weather_2012.head()
#QC OK

#Merge two dataframes
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index=True)

rentals_weather_11_12.shape

rentals_weather_11_12.head()
rentals_weather_11_12.tail()
#QC OK

#Change column order
orden = rentals_weather_2011.columns
rentals_weather_11_12 = rentals_weather_11_12[rentals_weather_2011.columns]
orden2 = ['dteday', 'day', 'weathersit', 'temp_celsius', 'windspeed_kh', 'atemp',
       'hum', 'season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday',
       'casual', 'registered', 'cnt']
rentals_weather_11_12 = rentals_weather_11_12[orden2]


rentals_weather_11_12.shape
rentals_weather_11_12.head()
rentals_weather_11_12.tail()
#QC OK