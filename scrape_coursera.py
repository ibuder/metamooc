# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 08:57:18 2015

@author: ibuder
"""

import pandas as pd
import requests

#courses = pd.read_json(
#    'https://api.coursera.org/api/catalog.v1/courses?ids=2,3',
#    orient='records')

params = {'ids': ['2,3'], 'fields': ['language,subtitleLanguagesCsv,isTranslate,universityLogo,targetAudience,instructor,estimatedClassWorkload']}
r = requests.get('https://api.coursera.org/api/catalog.v1/courses', params=params)
