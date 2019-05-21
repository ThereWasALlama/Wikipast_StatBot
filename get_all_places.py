import requests
from bs4 import BeautifulSoup
from login import *

def get_all_places(baseurl,name):
    result=requests.post(baseurl+'api.php?action=query&titles='+name+'&export&exportnowrap')
    soup=BeautifulSoup(result.text, "lxml")
    code=''
    for primitive in soup.findAll("text"):
        code+=primitive.string
    lines=code.split('*')
    
    places = []
    place = ""
    for line in lines:
        try:
            if '[[' in line:
                place=(line.split('/')[1]).strip()
                if not((place[0] == '-') or (place == 'Mention')):
                    place = place.split('[[')[1]
                    place = place.split(']]')[0]
                    places.append(place)
        except:
            pass
    if(len(places) == 0):
        raise Exception('No places found')
            
    return places
        
    

if __name__ == '__main__':
    baseurl = login()
    print(get_all_places(baseurl,'Poul Anderson'))
