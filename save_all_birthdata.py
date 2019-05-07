# This script takes all the names given by get_all_names and saves the birthdate
# data given by get_birthdate into an xml file specified in the parameter savename

from login import login
from get_all_names import get_all_names
from get_birthdate import get_birthdate
from get_birthplace import get_birthplace
from get_latlong import get_latlong

import xml.etree.ElementTree as xml


# The name of the database being used
# TODO put the savename in some configuration file somewhere
savename = 'database.xml'

bplace_error = 'NotFound'
bdate_error  = 'NotFound'


# TODO make sure this function actually updates the file instead of creating a new one completly
def save_all_birthdata(names):
    '''Use get_all_names to get the target pages, then just save all their birthdata information, names must be a lit of pagenames to target'''
    
    baseurl = login()
    
#    names = get_all_names(baseurl)
    
    bdate  = []
    bplace = []
    for name in names:
        try:
            bday = get_birthdate(baseurl, name)
            if bday == None:
                print('{} birthdate returned none'.format(name))
                bdat.append(bdate_error)
                continue
            
            bdate.append(bday)
            
        except:
            bdate.append(bdate_error)
            print('{} birthdate was set to {}'.format(name, bdate_error))
    
        try:
            bloc = get_birthplace(baseurl, name)
            if bloc == None:
                print('{} birthplace returned none'.format(name))
                bplace.append(bplace_error)
                continue
    
            bplace.append(bloc)
    
        except:
            bplace.append(bplace_error)
            print('{} birthplace caused exception'.format(name))
    
    
    
    # Prepare the xml to be saved
    # Base elements of the xml to be prepared
    # TODO make this update the existing database instead of writing over it
    root   = xml.Element('data')
    people = xml.SubElement(root, 'people')
    
    print('Saving data for {} people'.format(len(names)))
    
    for name, date, place in zip(names, bdate, bplace):
        pagename  = xml.SubElement(people, 'person', pagename=name)
        birthdate = xml.SubElement(pagename, 'birthdate')
        birthdate.text = date
    
        try:
            latlong = get_latlong(place)
        except:
            latlong = bplace_error
            
        birthplace = xml.SubElement(pagename, 'birthplace', latlong=str(latlong))
        birthplace.text = place
        
    
    # Save the final file
    with open(savename, 'wb') as savefile:
        savefile.write(xml.tostring(root))
        
if __name__ == '__main__':
    names = get_all_names(baseurl)
    save_all_birthdata(names)
