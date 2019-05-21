#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:04:25 2019

@author: LlamaGod
"""

import numpy as np
import matplotlib.pyplot as plt
from load_birthdays import load_birthdays
from pathlib import Path
import datetime
from load_all_places import load_all_places
import itertools

from max_distances import max_distances

def latlongstr2latlong(x):
    y    = x.split(',')
    lat  = float(y[0][1:])
    long = float(y[1][:-1])
    
    return (lat, long)

def travel_distance_histogram():
    ''' Create a histogram of the average maximum travel distance per birthyear'''
    
    startyear = 0
    
    bdata = load_birthdays()
    
    pdata = load_all_places()
    
    # Filter the Not Founds from the birthdata
    bdata = {x:y for x,y in bdata.items() if y!='NotFound'}
    
    # Filter out the not found elemens in all the lists and convert them to tuples
    pdata = {x:[latlongstr2latlong(y) for y in filter(lambda x : x!='NotFound', pdata[x])] for x in pdata}
    
    # Filter out the empty position lists
    pdata = {x:y for x, y in pdata.items() if y}
    
    # Get the max distances for each person    
    max_dist_data = max_distances(pdata)
    

    data_filtered  = list(filter(lambda x : x!='NotFound', bdata.values()))
    byears         = [int(x.split('.')[0]) for x in data_filtered]
    
    max_dist_avg = []
    bin_par = 20 # bin parameter
    
    year_range = range(startyear, datetime.datetime.now().year, bin_par)
    for year in year_range:
        count = 0
        d_avg = 0
#        for byear in byears: #all the good birthyears
#            if abs(byear-year)< bin_par: #bin around year
##                for birthdate, max_dist in zip(bdata.values(), pdata.values()): #find all the max distances corresponding to byear
        for name, birthdate in bdata.items():
            if abs(int(birthdate.split('.')[0]) - year) < bin_par:
#                       d_avg = d_avg + max_dist
                # Consider the element if it's in both dictionaries
                if name in max_dist_data:
                    d_avg = d_avg + max_dist_data[name]
                    count = count + 1
        
        d_avg = d_avg/count if count else 0
        max_dist_avg.append(d_avg)
                
                
    
    # Create the figure
    plt.figure()
    plt.bar(year_range, max_dist_avg, width=20)
#    plt.stem(year_range, max_dist_avg)
    plt.title("Mean travel dsitance distribution from year {}".format(startyear))
    plt.xlabel('year')
    plt.ylabel('mean maximum travel distance [m]')
    plt.savefig(Path('figures/') / 'travel_histogram.png')
    
if __name__ == '__main__':
    travel_distance_histogram()
