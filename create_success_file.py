#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:17:33 2019

@author: LlamaGod
"""

from load_birthdays import load_birthdays
from load_birthplaces import load_birthplaces


def create_success_file():
    ''' Create a text file containing the success rate of the bot in obtaining both birth dates and locations'''
    savename = 'success_rate.txt'
    
    # Load the data
    birthdays = load_birthdays()
    places    = load_birthplaces()
    
    # Count the number of NotFound in each as well as total
    Nerr_birthdays = sum(x=='NotFound' for x in birthdays.values())
    Nerr_places    = sum('NotFound' in x for x in places.values())
    
    err_rate_birthdays = Nerr_birthdays/len(birthdays)
    err_rate_places    = Nerr_places/len(places)
    
    bdaystr  = '{} fail rate for dates for sample of {}'.format(err_rate_birthdays, len(birthdays))
    placestr = '{} fail rate for places for sample of {}'.format(err_rate_places, len(places))
    print(bdaystr)
    print(placestr)
    
    with open(savename, 'w') as file:
        print(bdaystr, file=file)
        print(placestr, file=file)
        
        
if __name__=='__main__':
    create_success_file()