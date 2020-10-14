# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:28:24 2020

@author: JuanLu
"""
#%reset -f
#%%
###############################################################################
# Google Play Reviews                                                         #
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

gplay = pd.read_csv('googleplaystore.csv', sep=",", decimal=".")

gplay.shape
gplay.head()
gplay.tail()

plt.hist(gplay.Rating, edgecolor='black')
plt.title("Figure 1. Rating")
plt.xticks(np.arange(0,5.5, step=0.5))
plt.show()

gplay.info()