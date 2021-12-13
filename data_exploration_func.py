# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 19:33:49 2021

@author: siewm
"""

import os 
import pandas as pd

path = "C:\\Users\\siewm\\OneDrive\\Desktop\\DNN practice\\data\\"
datafile = 'Video_games_esrb_rating.csv'
testdata = 'test_esrb.csv'

os.chdir(path)

d = pd.read_csv(path+datafile)
td = pd.read_csv(path+testdata)

def getsum(data):
    '''compute all the necessary stats'''
    '''must import pandas as pd beforehand'''
    
    pd.set_option("display.max.columns", None)
    
    row, col = data.shape
    print('\nThis data has ', row, 'rows and', col, 'columns.\n')
    
    '''data info & description'''
    # data.select_dtypes(['object']).columns
    print(data.info())
    print('\nData description :- \n', data.describe(include='all'))
    print('\nCheck how many null values in data:\n', data.isnull().sum())
    
getsum(d) 
    
d.esrb_rating.value_counts()

    