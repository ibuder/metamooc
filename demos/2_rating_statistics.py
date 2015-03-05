# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:01:59 2015

@author: ibuder
"""

import matplotlib.pyplot as plt


sys.path.append(os.path.abspath(".."))
import db

X = db.get_coursera_ratings()

plt.xkcd()
matplotlib.rcParams.update({'font.size': 18})
plt.clf()
plt.hist( (X.loc[X['n_rating'] > 0, 'rating'], X.loc[X['n_rating'] > 10, 
                 'rating'],), normed=True, label=('>0 ratings', 
                 '>10 ratings',) , bins=8)
plt.legend(loc='upper left')
plt.xlabel('Rating')
plt.ylabel('Relative Frequency')
plt.title('Most ratings are good')