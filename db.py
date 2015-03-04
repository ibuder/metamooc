# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:50:31 2015

@author: ibuder
"""

import sqlalchemy

import password


def get_ro_engine():
    return sqlalchemy.create_engine(
    'mysql+mysqldb://metamooc_ro:' + password.password + 
    '@localhost/metamooc?charset=utf8&use_unicode=0')


def get_rw_engine():
    return sqlalchemy.create_engine(
    'mysql+mysqldb://metamooc_rw:' + password.password +
    '@localhost/metamooc?charset=utf8&use_unicode=0')
