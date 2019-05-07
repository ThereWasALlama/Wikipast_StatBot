#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:46:44 2019

@author: LlamaGod
"""

import xml.etree.ElementTree as ET
import xml.dom.minidom 

def view_database(databasename):
    ''' View the database xml in pretty print'''
    
#    databasename = 'database.xml'
    
    tree = ET.ElementTree(file=databasename)
    root = tree.getroot()
    dom  = xml.dom.minidom.parseString(ET.tostring(root)) # or xml.dom.minidom.parseString(xml_string)
    
    print(dom.toprettyxml())
    
if __name__ == '__main__':
    databasename = 'database.xml'
    view_database(databasename)