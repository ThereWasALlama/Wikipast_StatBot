# This script takes all the names given by get_all_names and saves the birthdate
# data given by get_birthdate into an xml file specified in the parameter savename

from login import login
from get_all_names import get_all_names
from get_birthdate import get_birthdate

import xml.etree.ElementTree as xml


# The name of the database being used
# TODO put the savename in some configuration file somewhere
savename = 'database.xml'


# TODO figure out what's wrong with the bet_birthdate function, seems to be returning none on easy to identify peeps
baseurl = login()

names = get_all_names(baseurl)

bdate = []
for name in names:
    try:
        bday = get_birthdate(baseurl, name)
        if bday == None:
            print('{} returned none'.format(name))
            bdat.append('0')
            continue
        
        bdate.append(bday)
        
    except:
        bdate.append('0')
        print('{} was set to 0'.format(name))
        
print(bdate)


# Prepare the xml to be saved
# Base elements of the xml to be prepared
# TODO make this update the existing database instead of writing over it
root   = xml.Element('data')
people = xml.SubElement(root, 'people')

bdaydict = dict(zip(names, bdate))
for name, date in bdaydict.items():
    pagename  = xml.SubElement(people, 'person', pagename=name)
    birthdate = xml.SubElement(pagename, 'birthdate')
    birthdate.text = date

# Save the final file
with open(savename, 'wb') as savefile:
    savefile.write(xml.tostring(root))
