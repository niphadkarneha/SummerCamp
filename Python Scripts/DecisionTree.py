# Decision Trees

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

# load a dataset of data from a balance
# Details of dataset are available here
# https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.names
# available for download here: https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data

balance_data = pd.read_csv(
'https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',
                           sep= ',', header= None)

# view details about the dataset
print ("Dataset Lenght:: ", len(balance_data))      
print ("Dataset Shape:: ", balance_data.shape)

# view the first few records from dataset
print (balance_data.head())

# Identify which variables will be used to predict what output
# The “X ” variables will be the predictor variables. It consists of data from 2nd column to 5th column. 
# The “Y” variable will be the outcome variable. It consists of data in the 1st column.
X = balance_data.values[:, 1:5]
Y = balance_data.values[:,0]

# Separate data into a training set and a testing set
# Training set will be used to train the model
# Testing data should NOT be used for training
# The parameter test_size is given value 0.3; it means test sets will be 30% of whole dataset  
# Training dataset’s size will be 70% of the entire dataset
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

# Decision Tree classifier using gini index
# for more infomation on gini index:
# https://en.wikipedia.org/wiki/Gini_coefficient
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

# Make prediction for a single hypothetical record. Note result.
clf_gini.predict([[4, 4, 3, 3]]) 

# Make prediction for entire test dataset. Note result.
y_pred = clf_gini.predict(X_test)
y_pred

# Calculating Accuracy Score

# The function accuracy_score() will be used to print accuracy. 
# Accuracy = ratio of the correctly predicted data points to all the predicted data points. 
print ("Accuracy is ", accuracy_score(y_test,y_pred)*100)
