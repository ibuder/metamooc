# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:47:39 2015

@author: ibuder
"""

import numpy as np
import re
import itertools
import pandas as pd
import sklearn.preprocessing as skpreprocessing

import db


class CourseraFeatures():
    """
    A class to manage calculation of features for Coursera courses
    """
    def __init__(self):
        self.Xraw = db.get_coursera_ratings()  # Values from scraping

    def extract_workload_hours(self, workload_strings=None):
        if not workload_strings:
            workload_strings = self.Xraw['estimatedClassWorkload']
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
    
    def average_hours(self):
        h = self.extract_workload_hours()
        return (h[0] + h[1])/2.0

    def subtitle_languages(self):
        subtitle_strings = self.Xraw['subtitleLanguagesCsv']
        subtitle_lists = [s.split(',') for s in subtitle_strings]
        # Get the unique languages        
        langs = [l for l in itertools.chain.from_iterable(subtitle_lists)]
        langs = list(np.unique(langs))  # Needs to be a list to remove the ''
        langs.remove('')
        has_lang = dict()  # Map languages to which course has subtitles in it
        for lang in langs:
            has_lang[lang] = [lang in l for l in subtitle_lists]
        return pd.DataFrame(has_lang)
        
    def target_audience(self):
        return self.Xraw['targetAudience']
        
    def rating(self):
        return self.Xraw['rating']
    
    def n_rating(self):
        return self.Xraw['n_rating']
        
    def feature_set1(self, normalize=False):
        """
        normalize : bool
            Fill missing data with mean, 
            then subtract mean and divide by standard deviation
        """
        result = self.subtitle_languages()
        result['average_hours'] = self.average_hours()
        result['targetAudience'] = self.target_audience()
        result['n_rating'] = self.n_rating()
        if normalize:
            for col in ['average_hours', 'targetAudience']:
                result[col] = result[col].fillna(np.mean(result[col]))
            for col in ['average_hours', 'targetAudience', 'n_rating']:
                result[col] = skpreprocessing.scale(
                    result[col].astype('float64'))
            result = result.fillna(0)
        return result
        
    def feature_set(self, **kwds):
        """
        Get current 'best' feature set--may change w/o warning
        """
        return self.feature_set1(**kwds)

    def recommend_content_based(self, theta, n_courses=5):
        """
        Recommend courses based on user preferences
        
        theta : dictionary 
            feature weights. keys must be in feature_set().columns
        
        Returns DataFrame with top n_courses recommendations
        """
        w = pd.Series(theta)
        scores = self.feature_set(normalize=True).multiply(w,
            axis='columns')  # Dot product weights with features
        # if feature is not given a weight, it will be NaN
        scores = scores.fillna(0)  
        scores = np.sum(scores, axis=1)  # sum over features
        scores.sort(ascending=False)
        scores = scores.head(n_courses)
        result = self.Xraw.loc[scores.index]  # Get top course info
        # Make sure we don't modify internal data        
        result = result.copy(deep=True)
        result['score'] = scores
        return result
        