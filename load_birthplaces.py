#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:34:30 2019

@author: LlamaGod
"""

import xml.etree.ElementTree as ET


def load_birthplaces():
    ''' Load the birthplaces from the database. returns in the form of a dictionary {pagename: (latlong, name)}'''
    
    savename = 'database.xml'
    
    tree = ET.parse(savename)
    root = tree.getroot()
    
    
    persons = root.find('people').findall('person')
    return {x.get('pagename'):(x.find('birthplace').get('latlong'), x.find('birthplace').text) for x in persons}



if __name__ == '__main__':
#    print(latlong2tuple('(5.5, -3.5555)'))
    
    print(load_birthplaces())