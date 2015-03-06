# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:01:16 2015

@author: ibuder
"""

import sklearn.preprocessing
from sklearn.cross_validation import train_test_split
import sklearn.linear_model
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(".."))
import features
import plotstyle

c = features.CourseraFeatures()
x = c.feature_set1()
y = c.rating()

# Train on classes with rating
ind = x['n_rating'] > 0
y = y[ind]
x = x[ind]

# Fill missing data and normalize features
for col in ['average_hours', 'targetAudience']:
    x[col] = x[col].fillna(np.mean(x[col]))
for col in ['average_hours', 'targetAudience', 'n_rating']:
    x[col] = sklearn.preprocessing.scale(x[col].astype('float64'))
x = x.fillna(0)

# Try non-linear features
x['average_hours2'] = x['average_hours'] ** 2.0
x['targetAudience2'] = x['targetAudience'] ** 2.0
x['n_rating2'] = x['n_rating'] ** 2.0
x['n_rating3'] = x['n_rating'] ** 3.0
x['n_rating4'] = x['n_rating'] ** 4.0

x_train, x_test, y_train, y_test, = train_test_split(x, y, random_state=42)
mod = sklearn.linear_model.LinearRegression()

mod.fit(x_train, y_train)
y_pred = mod.predict(x_test).ravel()

plt.figure(1)
plt.clf()
plt.hist((mod.predict(x_train) - y_train, np.mean(y_train) - y_train ,), 
         range=(-5, 5,), label=['Model errors', 'Training data'])
plt.xlabel('Rating Error')
plt.ylabel('# of Courses')
plt.title('These features cannot predict the average rating')
plt.legend()

plt.figure(2)
plt.clf()
plt.hist((y_pred - y_test, np.mean(y_test) - y_test ,), 
         range=(-5, 5,), label=['Model errors', 'Test data'])
plt.legend()

