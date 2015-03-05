# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:50:31 2015

@author: ibuder
"""

import sqlalchemy
import pandas as pd

import password


def get_ro_engine():
    return sqlalchemy.create_engine(
    'mysql+mysqldb://metamooc_ro:' + password.password + 
    '@localhost/metamooc?charset=utf8&use_unicode=0')


def get_rw_engine():
    return sqlalchemy.create_engine(
    'mysql+mysqldb://metamooc_rw:' + password.password +
    '@localhost/metamooc?charset=utf8&use_unicode=0')


def get_coursera_ratings():
    return pd.read_sql(
    'SELECT * FROM coursera_courses AS t1 JOIN coursetalk_avg_ratings' +
    ' AS t2 ON t1.name = t2.title',
    get_ro_engine())
