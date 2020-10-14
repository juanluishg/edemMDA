# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:49:42 2020

@author: JuanLu
"""
#%reset -f
#%%
###############################################################################
# CO2 Emissions                                                               #
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

co2 = pd.read_csv('co2_emission.csv', sep=",", decimal=".")

co2.shape
co2.head()
co2.tail()
#QC OK

co2.columns = ['entity', 'code', 'year', 'tones']

co2.dtypes

plt.hist(co2.tones, edgecolor='black')
plt.xticks(np.arange(co2.tones.min(),co2.tones.max(), step = 5e9))
plt.title("Figure 1. Tones of CO2")
plt.show()

co2.info()


plt.scatter(co2.year, co2.tones, c=co2.code, cmap='hsv') #No van los colores
plt.title("Tones per year")
plt.xlabel("Year")
plt.ylabel("Tones")
plt.show()
