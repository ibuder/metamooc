# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:18:44 2015

@author: ibuder
"""

import matplotlib.pyplot as plt
import numpy as np
import re
import scipy as sp
import scipy.stats

sys.path.append(os.path.abspath(".."))
import db
import plotstyle


def extract_workload_hours(workload_strings):
    min_hours = np.empty(len(workload_strings))
    max_hours = np.empty(len(workload_strings))
    for i, string in enumerate(workload_strings):
        match = re.match(r'([0-9]+)-([0-9]+) hours/week', string)
        if match:
            min_hours[i] = float(match.group(1))
            max_hours[i] = float(match.group(2))
        else:
            min_hours[i] = np.NaN
            max_hours[i] = np.NaN
    return min_hours, max_hours,


def bin_plot(x, y, **kwds):
    """
    Make binned (on x) version of scatterplot
    
    Error bars are std/sqrt(N)
    """
    # Fix data type incompatibility issues by making everything array
    x = np.array(x)    
    y = np.array(y)
    # Eliminate NaNs
    ind = np.logical_and(np.isfinite(x), np.isfinite(y))
    x = x[ind]
    y = y[ind] 
    means, bin_edges, dummy = sp.stats.binned_statistic(x, y, **kwds)
    stds, bin_edges, dummy = sp.stats.binned_statistic(
        x, y, statistic=np.std, **kwds)
    counts, bin_edges, dummy = sp.stats.binned_statistic(
        x, y, statistic='count', **kwds)
    # bin_edges[:-1] are the left edges of bins.
    # The average gives the bin centers
    plt.errorbar((bin_edges[:-1] + bin_edges[1:])/2.0, 
                 means, yerr=stds/np.sqrt(counts))
        
X = db.get_coursera_ratings()
X = X[X['n_rating'] > 0]

h = extract_workload_hours(X['estimatedClassWorkload'])
ind = np.isfinite(h[0])  # Cut missing data

plt.figure(1)
plt.clf()
bin_plot((h[0][ind] + h[1][ind])/2.0, X.loc[ind, 'rating'])
plt.xlabel('Average Expected Workload (hours/week)')
plt.ylabel('Average Rating')
plt.title('More intense courses are better')
# TODO probably want non-linear feature

print '==Language, Average Rating, # of Courses==' 
for lang in np.unique(X['language']):
    ind = X['language'] == lang
    print lang, np.mean(X.loc[ind, 'rating']), np.count_nonzero(ind)
    
plt.figure(2)
plt.clf()
n_subtitle = [s.count(',') for s in X['subtitleLanguagesCsv'] ]
bin_plot(n_subtitle, X['rating'], bins = (-.5, 0.5, 1.5, 2.5, 3.5, 4.5,) )
plt.xlabel('# of Subtitled Languages')
plt.ylabel('Average Rating')

plt.figure(3)
plt.clf()
bin_plot(X['targetAudience'], X['rating'])
plt.xlabel('Target Audience')
plt.ylabel('Average Rating')
plt.title('More advanced courses are lower rated')
# TODO probably want non-linear feature or categorical features

plt.figure(4)
plt.clf()
bin_plot(X['n_rating'], X['rating'], bins=np.linspace(0, 350, num=10) )
plt.xlabel('# of Ratings')
plt.ylabel('Average Rating')
plt.title('More popular classes are highly rated')