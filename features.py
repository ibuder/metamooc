# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:47:39 2015

@author: ibuder
"""

import numpy as np
import re
import itertools
import pandas as pd

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
        langs = list(unique(langs))  # Needs to be a list to remove the ''
        langs.remove('')
        has_lang = dict()  # Map languages to which course has subtitles in it
        for lang in langs:
            has_lang[lang] = [lang in l for l in subtitle_lists]
        return pd.DataFrame(has_lang)