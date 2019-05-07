#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:46:44 2019

@author: LlamaGod
"""

def view_database():
    ''' View the database xml in pretty print'''
    
    databasename = 'database.xml'
    
    tree = ET.ElementTree(file=databasename)
    root = tree.getroot()
    dom  = xml.dom.minidom.parseString(ET.tostring(root)) # or xml.dom.minidom.parseString(xml_string)
    
    print(dom.toprettyxml())
    
if __name__ == '__main__':
    view_database()