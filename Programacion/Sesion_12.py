# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:57:02 2020

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

#%%
#Loops
##For

# Loop standard
for i in range(0, 11, 1):
    print("i:",i)

# Loop from list
for i in [1,2,3,4]:
    print("i:",i)

# Loop from string list
for i in ['red', 'yellow', 'blue']:
    print("Y el color es:",i)

#%%
x = wbr.cnt
plt.hist(x, bins=10, edgecolor="black")
plt.show()

for i in range(0,11,1):
    print('i:',i)

    x = wbr.cnt
    plt.hist(x, bins=10, edgecolor="black")
    plt.show()

#%%
for i in range(10, 101, 1):
    x = wbr.cnt
    plt.hist(x, bins=i, edgecolor="black")
    plt.show()
    print(i)

#%%
#Draw all circle in diagonal

ax = plt.subplots(figsize=(9,9))
ax = plt.gca()

ax.set_xlim((0,10))
ax.set_ylim((0,10))

for i in range(0,11,1):
    c1 = plt.Circle((i,i), 0.5, color='r')#((x,y), radio, color)
    ax.add_artist(c1)
    
    
# %%
#Draw an animate circle

ax = plt.subplots(figsize=(9,9))
ax = plt.gca()

ax.set_xlim((0,10))
ax.set_ylim((0,10))

for i in range(0,11,1):
    if i>0:
        c2 = plt.Circle((i-1,i-1), 0.4, color='w')#((x,y), radio, color)
        ax.add_artist(c2)
    
    c1 = plt.Circle((i,i), 0.5, color='r')#((x,y), radio, color)
    ax.add_artist(c1)
    
    
#%%
#Draw two lines of circle, two diagonal 
ax = plt.subplots(figsize=(9,9))
ax = plt.gca()

ax.set_xlim((0,10))
ax.set_ylim((0,10))

for i in range(0,11,1):
    c1 = plt.Circle((i,i), 0.5, color='r')#((x,y), radio, color)
    ax.add_artist(c1)
    
    c2 = plt.Circle((i,10-i), 0.5, color='b')
    ax.add_artist(c2)
    
    
#%%
#Draw one lines of circle, incremental size
ax = plt.subplots(figsize=(9,9))
ax = plt.gca()

ax.set_xlim((0,10))
ax.set_ylim((0,10))

for i in range(0,11,1):
    c1 = plt.Circle((i,i), (i*0.1)+(0.0001*math.exp(i)), color='r')#((x,y), radio, color)
    ax.add_artist(c1)
    
#%%
#Draw diagonal circle changing colors
ax = plt.subplots(figsize=(9,9))
ax = plt.gca()

ax.set_xlim((0,10))
ax.set_ylim((0,10))

colors = ['r','b','g','y','c', 'm', 'orange', 'maroon', 'darkgreen', 'aquamarine', 'black']

for i in range(0,11,1):
    c1 = plt.Circle((i,i), (i*0.1), color=colors[i])#((x,y), radio, color)
    ax.add_artist(c1)
    
#%%
#Same but with opacity(alpha)
ax = plt.subplots(figsize=(9,9))
ax = plt.gca()

ax.set_xlim((0,10))
ax.set_ylim((0,10))

colors = ['r','b','g','y','c', 'm', 'orange', 'maroon', 'darkgreen', 'aquamarine', 'black']

for i in range(0,11,1):
    c1 = plt.Circle((i,i), (i*0.1), alpha=(i*0.1), color=colors[i])#((x,y), radio, color)
    ax.add_artist(c1)
    
#%%
#Draw diagonal circle changing colors
ax = plt.subplots(figsize=(9,9))
ax = plt.gca()

ax.set_xlim((0,10))
ax.set_ylim((0,10))

colors = ['r','b','g','y','c', 'm', 'orange', 'maroon', 'darkgreen', 'aquamarine', 'black']

for i, c in zip(range(0,11,1), colors):
    c1 = plt.Circle((i,i), (i*0.1), color=c)#((x,y), radio, color)
    ax.add_artist(c1)
    
#%%
##While
count=1
while(count < 4):
    print(count, "Calidad")
    count +=1
    
#%%
#CONDITIONALS
##If/Else
test_covid = 'negativo'
if test_covid == 'negativo':
    print("Puede usted salir de casa")
else test_covid == 'positivo':
    print("Debe quedarse en casa")
    
#%%
#Loop and Conditionals
for i in range(0,11,1):    
    if i > 5:
        print("Mi nota es: ",i,"Aprobado")
    else:
        print("Mi nota es: ",i,"Suspenso")
        
#%%
for i in range(0,11,1):
    if i >= 0 and i < 5:
        grade = "Suspenso"
    elif i < 8:
        grade = "Notable"
    elif i <= 10:
        grade = "Sobresaliente"
        
    print("Mi nota es: ", i, grade)
    
#%%
#FUNCTIONS
#Define a function plus
def plus(a,b):
    print("Let's add these two numbers")
    return a + b

plus(2,3)

"""Funcion dividir
@param a {number} - Divisor
@param b {number} - Dividendo (Default: 2)
@return {number} - Resultado division
"""
def divide(a,b=2):
    print("Let's divide these two numbers")
    return a/b
    
divide(3,8)

divide(3)


#%%
#Define an histogram
def hist(a, bins=10):
    res = a.describe()
    m = res[1]
    sd = res[2]
    n = res[0]
    
    plt.hist(a, bins=bins, edgecolor='black')
    plt.axvline(x=m, linewidth=1, linestyle='solid', color='red', label='Mean')
    
    plt.show()

"""Deberes: hacer funcion con el histograma completo(lines media y desvicion, 
    leyenda, titulo, nombre ejes)"""
    
    
hist(wbr.cnt)