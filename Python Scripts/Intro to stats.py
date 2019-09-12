# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:06:39 2018

@author: User
"""

# Basic Metrics
# When we think about summarizing data, what are the metrics that we look at? 
# We will look in the price of weed dataset along with the demographic information of the United States.

import numpy as np
import pandas as pd

prices_pd = pd.read_csv("C:/Users/User/Documents/ACK Data Science Camp/Machine Learning and Data Science Camp - Course Materials/prices.csv")
demography_pd = pd.read_csv("C:/Users/User/Documents/ACK Data Science Camp/Machine Learning and Data Science Camp - Course Materials/demographics.csv")
population_pd = pd.read_csv("C:/Users/User/Documents/ACK Data Science Camp/Machine Learning and Data Science Camp - Course Materials/population.csv")

prices_pd.head()

prices_pd.tail()

demography_pd.head()

population_pd.head()

prices_pd.dtypes



# Finding mean, median, mode, variance, standard deviation for California
# arithmetic average of a range of values or quantities, computed by dividing the total of all values by the number of values.

california_pd = prices_pd[prices_pd.State == "California"].copy(True)
california_pd.head()

ca_sum = california_pd['HighQ'].sum()

ca_count = california_pd['HighQ'].count()

ca_mean = ca_sum / ca_count
print ("Mean weed price in CA is:", ca_mean)



# Variance = the average distance of the data values from the mean
california_pd['HighQ_dev'] = (california_pd['HighQ'] - ca_mean) ** 2
ca_HighQ_variance = california_pd.HighQ_dev.sum() / (ca_count - 1)
print ("Variance of High Quality weed prices in CA is:", ca_HighQ_variance)

# Standard deviation = is the square root of variance. This will have the same units as the data and mean
ca_HighQ_SD = np.sqrt(ca_HighQ_variance)
print ("Standard Deviation of High Quality weed prices in CA is:", ca_HighQ_SD)

#Pandas built-in functions
california_pd.describe()
california_pd.HighQ.mode()
