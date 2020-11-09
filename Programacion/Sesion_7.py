# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:55:42 2020

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

# Recode working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No", "Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()


# Recode weather situation
wbr["ws_st"] = wbr.weathersit
wbr.ws_st = wbr.ws_st.replace(to_replace=1, value="Sunny")
wbr.ws_st = wbr.ws_st.replace(to_replace=2, value="Cloudy")
wbr.ws_st = wbr.ws_st.replace(to_replace=3, value="Rainy")
#To category
my_categories = ["Sunny", "Cloudy", "Rainy"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["ws_cat"] = wbr.ws_st.astype(my_datatype)
wbr.info()

#frequencies
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

#%%
#Mean Comparison
wbr.cnt.describe()

plt.hist(wbr.cnt)
plt.show()

plt.bar(mytable2.index, mytable2['count'])
plt.show()


#Mean of each group
wbr.groupby('wd_cat').cnt.mean()

wbr.groupby('wd_cat').cnt.std()

#t test
##Extract two groups
cnt_wd = wbr.loc[wbr.wd_cat == 'Yes', "cnt"]
cnt_nwd = wbr.loc[wbr.wd_cat == 'No', "cnt"]

##Statistical test
ttest = stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)

m = wbr.cnt.mean()
n = wbr.cnt.count()
std = wbr.cnt.std()

#Plot the test
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="wd_cat", y="cnt", data=wbr, ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800, 6200)
plt.ylabel(' ')
plt.xlabel("Working Day")
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle='dashed', color="green")
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = 'Mean: ' + str(round(m,1)) + '\nn: ' + str(round(n,0)) + '\nt: ' + str(round(ttest.statistic, 3)) + '\nPValue: ' + str(round(ttest.pvalue, 3))
plt.text(0.85,5400, textstr, bbox=props)
plt.title("Figure 1. Average rentals by Working Day.")
plt.show()

#pValue = 0.11 > 0.05 -> Rechazo la hipotesis que las medias son distintas. 
#Las medias no son si significativamente diferentes


#########################################
#Example By Year

wbr.groupby('yr').cnt.mean()

cnt_2011 = wbr.loc[wbr.yr == 0, "cnt"]
cnt_2012 = wbr.loc[wbr.yr == 1, "cnt"]


ttest = stats.ttest_ind(cnt_2011, cnt_2012, equal_var = False)
print(ttest)

#Plot the test
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="yr", y="cnt", capsize=0.05, data=wbr, ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800, 6200)
plt.ylabel(' ')
plt.xlabel("Year")
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle='dashed', color="green")
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = 'Mean: ' + str(round(m,1)) + '\nn: ' + str(round(n,0)) + '\nt: ' + str(round(ttest.statistic, 3)) + '\nPValue: ' + str(round(ttest.pvalue, 3))
plt.text(-0.30,5400, textstr, bbox=props)
plt.title("Figure 2. Average rentals by Year.")
plt.show()


#%%
## Variance Analysis -> Anova

#Describe comparasion
wbr.groupby('ws_cat').cnt.mean()

#Statistical comparasion
cnt_sunny = wbr.loc[wbr.ws_cat == 'Sunny', "cnt"]
cnt_cloudy = wbr.loc[wbr.ws_cat == 'Cloudy', "cnt"]
cnt_rainy = wbr.loc[wbr.ws_cat == 'Rainy', "cnt"]


anova = stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)
print(anova)

m = wbr.cnt.mean()
n = wbr.cnt.count()
std = wbr.cnt.std()

#Plot the test
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="ws_cat", y="cnt", capsize=0.05, data=wbr, ci=95, join=0)
plt.yticks(np.arange(1500, 7000, step=500))
plt.ylim(1000, 5800)
plt.ylabel(' ')
plt.xlabel("Weather Situation")
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle='dashed', color="green")
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = 'STD: ' + str(round(std,1)) + '\nn: ' + str(round(n,0)) + '\nt: ' + str(round(anova.statistic, 3)) + '\nPValue: ' + str(round(anova.pvalue, 3))
plt.text(1.6,4650, textstr, bbox=props)
plt.title("Figure 3. Average rentals by Weather Situation.")
plt.show()
