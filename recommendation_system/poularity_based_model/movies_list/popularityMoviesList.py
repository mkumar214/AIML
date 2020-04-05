#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:51:05 2020

@author: mukesh
"""
"""importing libraries"""

import numpy as np
import pandas as pd

"""loading files movies files"""

movies_list=pd.read_csv('movies.csv')
ratings_list=pd.read_csv('ratings.csv')

"""top five list of movies"""
print(movies_list.head())

#rating list

print(ratings_list.head())

def mergeList(mainList,scondaryList,col):
    return pd.merge(mainList,scondaryList,on=col)
    

#movies_data=pd.merge(ratings_list, movies_list,on='movieId')
movies_data=mergeList(ratings_list, movies_list,'movieId')
movies_data.head()

ratingavg =pd.DataFrame(movies_data.groupby('title')['rating'].mean())
ratingavg['rating_counts'] = pd.DataFrame(movies_data.groupby('title')['rating'].count())
topSortedCountRating = ratingavg.head()
    