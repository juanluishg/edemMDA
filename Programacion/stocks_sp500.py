# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:26:49 2020

@author: JuanLu
"""
#%reset -f
#%%
###############################################################################
# S&P 500 - 5 years                                                           #
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

#Load dataset
sp500 = pd.read_csv("all_stocks_5yr.csv", sep=",", decimal=".")

#Check shape
sp500.shape
sp500.head()
sp500.tail()
#QC OK

#Select variable
name = sp500.Name

#Plot histogram
plt.hist(name)
plt.title("Figure 1. Histogram Name S&P 500 Companies")
plt.show()

#Show types
sp500.dtypes

#Plot a Scatter
plt.scatter(sp500.open, sp500.volume)
plt.title("Figure 2. Open vs Volume")
plt.xlabel("Open Value $")
plt.ylabel("Volume")
plt.show()


#Google evolution
googl = sp500.loc[sp500.Name == 'GOOGL']

plt.hist(googl.volume)
plt.title("Figure 3. Volume Google 2013-2018")
plt.show()

googl = googl.astype({'date':'datetime64[D]'})

googl.dtypes

googl.date.min()

plt.scatter(googl.date, googl.close, c=np.sign(googl.close-googl.open), cmap='RdYlGn')
plt.ylabel("Close Value $")
plt.xlabel("Date")
#Quiero un tick por cada mes
plt.show()

del(googl, name, sp500)
