#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:30:58 2019

@author: LlamaGod
"""

import xml.etree.ElementTree as ET
import xml.dom.minidom 

from login_edit import login_edit
from get_all_places import get_all_places
#from get_all_names import get_all_names

#def get_all_places(baseurl, name):
#    return ['Lausanne', 'Paris', 'Geneva']

# TODO crreate the search based on the names list and then modify the file
def save_all_places(names, databasename):
    '''Save all the places that a person has been to, to the xml database, '''
    
    # Login to the website
    login_obj = login_edit()
    
    # Name of the database
#    databasename = 'database.xml'
    
    # Load the database xml
    tree = ET.ElementTree(file=databasename)
    
    root   = tree.getroot()
    people = root[0]
    
    # Loop over all the people and add the places they've been to to their entry
    for person in people:
        
        # Find the places tag to modify or create a new one
        places = person.find('places')
        if places == None:
            places = ET.SubElement(person, 'places')
        
        try:
            persons_places = get_all_places(login_obj.baseurl, person.get('pagename'))
        except:
            print('{} could not find places'.format(person.get('pagename')))
            continue
        for place in persons_places:
            if place != None:
                tmp  = ET.SubElement(places, 'city')
                tmp.set('name', place)
                
    
    with open(databasename, 'wb') as savefile:
        savefile.write(ET.tostring(root))
    
        
#    dom = xml.dom.minidom.parseString(ET.tostring(root)) # or xml.dom.minidom.parseString(xml_string)
#    print(dom.toprettyxml())
    

    
    
if __name__ == '__main__':
#    login_obj= login_edit()
    login_obj=login_edit()
    databasename = 'database.xml'
    save_all_places(get_all_names(login_obj.baseurl), databasename)