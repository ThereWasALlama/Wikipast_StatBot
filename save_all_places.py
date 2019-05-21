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

from get_latlong import get_latlong

#from get_all_names import get_all_names

#def get_all_places(baseurl, name):
#    return ['Lausanne', 'Paris', 'Geneva']

# TODO crreate the search based on the names list and then modify the file
def save_all_places(names, databasename):
    '''Save all the places that a person has been to, to the xml database,
        Relies on the database already being made by the save_all_birthdata function'''
    
    # Login to the website
    login_obj = login_edit()
    
    bplace_error = 'NotFound'

    
    # Name of the database
#    databasename = 'database.xml'
    
    # Load the database xml
    tree = ET.ElementTree(file=databasename)
        
    
    root   = tree.getroot()
    people = root[0]
    
    # Loop over all the people and add the places they've been to to their entry
    for person in people:
#    for name in names:
        # Try to find the person in the database
#        person = None
#        for dude in people.findall('person'):
#            print('Comparing {} to {}'.format(dude.get('pagename'), name))
#            if dude.get('pagename') == name:
#                person = dude
#                break
#        # Create the person if it wasn't found and add the places        
#        if person == None:
#            print('{} not found creating..'.format(name))
#            person  = ET.SubElement(people, 'person', pagename=name)

                
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
                
                # Find the latlong for each place
                try:
                    latlong = get_latlong(place)                    
                except:
                    latlong = bplace_error
                
                tmp  = ET.SubElement(places, 'city')
                tmp.set('name', place)
                tmp.set('latlong', str(latlong))
                
    
    with open(databasename, 'wb') as savefile:
        savefile.write(ET.tostring(root))
    
        
#    dom = xml.dom.minidom.parseString(ET.tostring(root)) # or xml.dom.minidom.parseString(xml_string)
#    print(dom.toprettyxml())
    

    
    
if __name__ == '__main__':
#    login_obj= login_edit()
    login_obj=login_edit()
    databasename = 'database.xml'
    save_all_places(get_all_names(login_obj.baseurl, count_limit=500), databasename)