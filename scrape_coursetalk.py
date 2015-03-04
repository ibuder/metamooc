# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:42:27 2015

@author: ibuder
"""

import lxml.html
import requests
import pandas as pd


titles, ratings, n_reviews = [], [], []
for ipage in range(1, 35):  # FIXME Hardcoded number of pages in search result!
    params = {'page': ipage}
    page = requests.get('http://www.coursetalk.com/coursera', params=params)
    tree = lxml.html.fromstring(page.text)
    table = tree.xpath('//table[@class="table course_list"]')
    assert len(table) == 1  # Only expect 1 unless HTML format changed
    # Each row in table corresponds to 1 class    
    children = table[0].iterchildren()
    children.next()  # Skip first row (header)

    for row in children:
        # Hardcoded the data structure -- all the indices below depend on it
        # and can change if the web page source does
        title = row[1][0].text
        rating = int(row[3][0][0].get('class')[7:])
        n_review = int(row[3][0][2].text)
        titles.append(title)
        ratings.append(rating)
        n_reviews.append(n_review)

coursetalk_ratings = pd.DataFrame({'title': titles, 'rating': ratings,
                                   'n_rating': n_reviews})
                                   
engine = db.get_rw_engine()
coursetalk_ratings.to_sql('coursetalk_avg_ratings', engine)