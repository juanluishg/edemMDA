# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:04:59 2020
False Discovery Rate
@author: Alberto Sanz
"""

#reset -f 

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 
from scipy.stats import pearsonr


#Set sumber of columns
n=100

#create a dataset with 1000 random integer numbers (from 0 to 100) stored in n variables (columns)
df1 = pd.DataFrame(np.random.randint(0,100,size=(1000, n)), columns=np.arange(1,n+1,1))
print (df1)

pearsonr(df1[1], df1[2])
plt.scatter(df1[1], df1[2])

#Compute the correlations between all variables 
c_m= df1.corr()
print (c_m)

#represent the correlation matrix in a heatmap
sns.heatmap(c_m, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(20, 220, n=200), square=True)

#Fine-tune graphic parameter (ranges of color scale)
sns.heatmap(c_m, vmin=-0.2, vmax=0.2, center=0, cmap= 'coolwarm', square=True)


#Now compute the p-values for every correlation to learn wich correlations are significant.

#For doing so I create a specific function for that (functions will be discussed later in the course)
def calculate_pvalues(df):
    df = df.dropna()._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = round(pearsonr(df[r], df[c])[1], 4)
    return pvalues

#Get the p_values matrix and transform it to numeric, so we can rank them later
p_val_matrix = calculate_pvalues(df1)
col=np.arange(1,n+1,1)
p_val_matrix[col] = pd.to_numeric(p_val_matrix[col].stack(), errors='coerce').unstack()


#Lets take all the p_values and let's rank them in a list
list_pval = (p_val_matrix.where(np.triu(np.ones(c_m.shape), k=1).astype(np.bool))
                  .stack()
                  .sort_values(ascending=False))

#sns.heatmap(p_val_matrix, vmin=0, vmax=1, center=0.5, cmap=sns.diverging_palette(20, 220, n=200), square=True)

