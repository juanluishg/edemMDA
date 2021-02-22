# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:49:32 2020

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


#%%
#Describir variables cuantitativas estadisticamente
##Describir las ventas
wbr.cnt.mean()
wbr.cnt.min()
res = wbr.cnt.describe()


res[0]

##Crear un histograma
###Seleccionar la variables
x = wbr['cnt'] #wbr.cnt
plt.hist(x)


#plot
plt.hist(x, edgecolor='black', color='green', bins=12) #bins: numero de columnas
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)
plt.title('Figure 1. Daily Gicycle rentals in Washington DC \n by Capital bikeshare. 2011-2012')
plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency')
plt.show()

res[1]
print(round (res[1],1))


#Guardar parametros
n = res[0] 
m = res [1]
des = res[2]

##Añadir parametros al histograma

#Texto en histograma
plt.hist(x, edgecolor='black', color='green', bins=12) #bins: numero de columnas
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)

plt.title('Figure 1. Daily Gicycle rentals in Washington DC \n by Capital bikeshare. 2011-2012')

plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency')

textstr = 'Mean = ' + str(round(m,1)) + '\nS.D = ' + str(round(des,1)) + '\nn = ' + str(round(n,0))
plt.text(6100,95, textstr)#Añadir texto

plt.show()



#Añadir lineas de referencia
plt.hist(x, edgecolor='black', color='green', bins=12) #bins: numero de columnas
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)

plt.title('Figure 1. Daily Gicycle rentals in Washington DC \n by Capital bikeshare. 2011-2012')

plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency')

textstr = 'Mean = ' + str(round(m,1)) + '\nS.D = ' + str(round(des,1)) + '\nn = ' + str(round(n,0))
plt.text(6100,95, textstr)

plt.axvline(x=m, linewidth=1.2, linestyle='solid', color='red', label='Mean')#Linea vertical

plt.show()



#Añadir caja al texto
plt.hist(x, edgecolor='black', color='green', bins=12) #bins: numero de columnas
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)

plt.title('Figure 1. Daily Gicycle rentals in Washington DC \n by Capital bikeshare. 2011-2012')

plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency')

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = 'Mean = ' + str(round(m,1)) + '\nS.D = ' + str(round(des,1)) + '\nn = ' + str(round(n,0))
plt.text(6100,95, textstr, bbox=props)

plt.axvline(x=m, linewidth=1.2, linestyle='solid', color='red', label='Mean')#Linea vertical
plt.show()


#Añadir lineas de desviacion tipica a la linea de la media y añadir leyenda
_, bins, _ = plt.hist(x, edgecolor='black', color='green', bins=12) #bins: numero de columnas
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)

plt.title('Figure 1. Daily Gicycle rentals in Washington DC \n by Capital bikeshare. 2011-2012')

plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency')

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = 'Mean = ' + str(round(m,1)) + '\nS.D = ' + str(round(des,1)) + '\nn = ' + str(round(n,0))
plt.text(6600,95, textstr, bbox=props)

plt.axvline(x=m, linewidth=1.2, linestyle='solid', color='red', label='Mean')#Linea vertical
plt.axvline(x=m-des, linewidth=1.2, linestyle='dashed', color='blue', label='-1 S.D')#Linea vertical
plt.axvline(x=m+des, linewidth=1.2, linestyle='dashed', color='blue', label='+1 S.D')#Linea vertical

std = wbr.rolling(des).std()
std.plot()
plt.show()

#%%
#Describir variables cualitativa/nominal estadisticamente
tabla = wbr.groupby(['weathersit']).size()
print(tabla)

tabla.sum()

n=tabla.sum()
n

#Porcentaje
tabla2 = (tabla/n)*100
print(tabla2)

#Redondear
tabla3 = round(tabla2, 1)
tabla3

#Grafico de barras
plt.bar(tabla2.index, tabla2)


#Grafico de barras con nombres
bar_list = ['Sunny', 'Cloudy', 'Rainy']
colors = ['blue', 'gray', 'black']

plt.bar(bar_list, tabla2, color=colors)
plt.ylabel('Porcentaje')
plt.title('Figura 2.Tiempo en Washingtom. 2011-2012')
props = dict(boxstyle='round')
textstr= 'n = '+str(n)
plt.text(1.7,60, textstr)