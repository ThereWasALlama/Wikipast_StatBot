import xml.etree.ElementTree as ET

def load_birthdays():
    ''' Load all the birthday information from the database and return it as a pagename bday dictionary'''
    
    savename = 'database.xml'
    
    tree = ET.parse(savename)
    root = tree.getroot()

    # Take the pagenames as the names of the people and take the birthdates as strings and form dictionary
    persons = root.find('people').findall('person')
    return {x.get('pagename'):x.find('birthdate').text for x in persons}
    
if __name__ == '__main__':
    print(load_birthdays())
