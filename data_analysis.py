# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 00:00:24 2017

@author: Lily
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

df = pd.read_csv('book_data_2.csv')
df1 = df.dropna(axis=0,how='any')

#describe the data 
d_p =  df['PRICE'].describe()
d_wp = df['WEB_PRICE'].describe()
d_s = df['SCORE'].describe()
d_pl = df['PL'].describe()

#delete:0 instead of nan, useless
d_wp = df['WEB_PRICE'].describe()


describe = pd.DataFrame({'PRICE':d_p,
                         'PL':d_pl,
                         'WEB_PRICE':d_wp,
                         'SCORE':d_s})
describe.to_csv('books_describe.csv')

#box plots
plt.figure()
df['SCORE'].plot.box(legend='Score')
plt.figure()
df['PL'].plot.box(legend='PL')
plt.figure()
df['WEB_PRICE'].plot.box(legend='Web_price')
plt.figure()
df['PRICE'].plot.box(legend='Price')


#Histograms
plt.figure()
ax1 = df1['SCORE'].hist(alpha=0.8,bins=50,figsize=(6,4))
ax1.legend(['Score'])
plt.figure()
df1['SCORE'].diff().hist(alpha=0.8,bins=50,figsize=(6,4))


plt.figure()
ax2 = df1['PRICE'].hist(alpha=0.8,bins=50,figsize=(6,4))
ax2.legend(['Price'])
plt.figure()
df1['PRICE'].diff().hist(alpha=0.8,bins=50,figsize=(6,4))

plt.figure()
ax3 = df1['WEB_PRICE'].hist(alpha=0.8,bins=50,figsize=(6,4))
ax3.legend(['Web_price'])
plt.figure()
df1['WEB_PRICE'].diff().hist(alpha=0.8,bins=50,figsize=(6,4))

plt.figure()
ax4 = df1['PL'].hist(alpha=0.8,bins=50,figsize=(6,4))
ax4.legend(['Pl'])
plt.figure()
df1['PL'].diff().hist(alpha=0.8,bins=50,figsize=(6,4))


#regression analysis
sns.lmplot('PRICE', 'SCORE', df1)
sns.lmplot('WEB_PRICE','SCORE',df1)
sns.lmplot('SCORE','PL',df1)


result1= sm.OLS(df1['SCORE'], df1['PL']).fit()
print "The result of Score_Pl regression analysis is:"
print result1.summary()

result2 = sm.OLS(df1['PRICE'], df1['SCORE']).fit()
print "The result of Price-Score regression analysis is:"
print result2.summary()

result3 = sm.OLS(df1['WEB_PRICE'], df1['SCORE']).fit()
print "The result of Web_price-Score regression analysis is:"
print result3.summary()
