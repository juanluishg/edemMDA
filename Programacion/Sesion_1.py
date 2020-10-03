# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:35:19 2020
@author: JuanLu
Our first dataset
"""
#%reset -f

#%%
###############################################################################
# Primeros pasos                                                              #
###############################################################################

3+2

a=3
b=2
c=a+b

c

print(c)

a
b
c

print(a)
print(b)
print(c)

a="Hello"
b="World"

print(a)
print(b)

c = a + " " + b
print(c)
print(a,b)
print("{} {}".format(a,b))

del(a,b,c)

#%%
###############################################################################
# Create datasets                                                             #
###############################################################################

# Load basiclibraries
import os # Acceder desde python al S.O
import pandas as pd # Libreria de datasets, matrices de datos desde python
import numpy as np # Operaciones de calculo
import matplotlib.pyplot as plt # Libreria de gráficos


# Create a dataframe

name = ['Yaling', 'Sofia', 'Maria', 'Pablo', 'Ines'] # List
age = [28, 23, 25, 23, 25]
gender = ['Female', 'Female', 'Female', 'Male', 'Female']

print(name, age, gender)

class2020 = pd.DataFrame({'name': name, 'age': age, 'gender': gender})

# Clean up
del (name, age, gender)

# Work with DataFrame

class2020.age

class2020.shape
class2020.head(3)
class2020.tail(2)
#QC OK

# Get working directory
os.getcwd()

# Change working directory
os.chdir("C:/Users/JuanLu/Dropbox/I.Informatica/Master/edemMDA/Programacion")
os.getcwd()


# Save dataframe to CSV and Excel
class2020.to_csv("class2020.csv")
class2020.to_excel("class2020.xlsx")