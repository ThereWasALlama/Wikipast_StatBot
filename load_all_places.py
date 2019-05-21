#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:22:34 2019

@author: LlamaGod
"""

import xml.etree.ElementTree as ET

def latlongstr2latlong(x):
    y    = x.split(',')
    lat  = float(y[0][1:])
    long = float(y[1][:-1])
    
    return (lat, long)

def load_all_places():
    '''Load all the places that people have visitied from the database.
        Returns a dictionary of pagename:(lat, long), first one is naissance'''
    
    
    savename = 'database.xml'
    
    tree = ET.parse(savename)
    root = tree.getroot()

    # Take the pagenames as the names of the people and take the birthdates as strings and form dictionary
    persons = root.find('people').findall('person')
    return {x.get('pagename'):[y.get('latlong') for y in x.find('places').findall('city')] for x in persons}
    

if __name__ == '__main__':
    print(load_all_places())    