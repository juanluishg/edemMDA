# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:39:01 2021

@author: JuanLu
"""

#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#%reset -f


#load basiclibraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math

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
os.chdir("D:\\Master\\edemMDA\\Programacion")
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
print(wbr.shape)
print(wbr.head())
print(wbr.info())
#QC OK

#%% Class
class lista_pro:
    datos = [23,24,25,26]
    
    #Definir metodo media
    def media(self):
        return sum(self.datos) / len(self.datos)


edad = lista_pro()

edad.datos
edad.media()
