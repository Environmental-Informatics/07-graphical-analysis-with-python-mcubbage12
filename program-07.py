#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:45:11 2020
this code takes data downloaded from the USGS website on earthquakes around the world within the last 30 days and preformes exploratory grahical  analysis on the data
@author: mcubbage ( Marissa Cubbage)
"""
#import paCKAGES needed for analysis
import pandas
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats 

#read in data 
quake_data=pandas.read_table('all_month.csv',sep="," )

#create histogram of magnitudes of earthquakes 
plt.hist(quake_data['mag'], bins=10, range=(0,10),color='blue')
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.show


#create KDE plot with kernel width=0.5 and kernel type=scott

pandas.quake=quake_data['mag']
pandas.quake.plot.kde(bw_method=0.5)
plt.xlabel("Magnitude")
plt.show()

#plot longitude on x axis and latitiude on y axis 

plt.plot(quake_data["longitude"], quake_data["latitude"], 'b^', label='Mean')
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.show()

#create normal cumulative distribution plot of earthquake depths
plt.hist(quake_data['depth'], bins=200, cumulative=True,color='black')
plt.xlabel("depth")
plt.ylabel("cumulative frequency")
plt.show()

#create a scatterplot with x axis= earthquake magnitude and y axis= depth
plt.plot(quake_data["mag"], quake_data["depth"], 'r^')
plt.xlabel("Magnitude")
plt.ylabel("Depth")

#create a Q-Q plot of earthquake magnitudes.
#our Q-Q plot assumes a normal distribution of the data
scipy.stats.probplot(quake_data["mag"], dist='norm', plot=plt)

