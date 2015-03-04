# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 08:57:18 2015

@author: ibuder
"""

import pandas as pd
import requests

import db

# Select fields to get
params = {'fields': ['language,subtitleLanguagesCsv,isTranslate,universityLogo,targetAudience,instructor,estimatedClassWorkload']}
r = requests.get('https://api.coursera.org/api/catalog.v1/courses', 
                 params=params)

coursera_courses = pd.DataFrame(r.json()['elements'])
del coursera_courses['links']  # This column causes mySQL to choke

engine = db.get_rw_engine()
coursera_courses.to_sql('coursera_courses', engine)