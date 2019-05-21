import requests
from bs4 import BeautifulSoup
from login import *

def get_birthplace(baseurl,name):
    result=requests.post(baseurl+'api.php?action=query&titles='+name+'&export&exportnowrap')
    soup=BeautifulSoup(result.text, "lxml")
    code=''
    for primitive in soup.findAll("text"):
        code+=primitive.string
    lines=code.split('*')
    try:
        if '[[Naissance]]' in lines[1]:
            place=(lines[1].split('/')[1]).strip()
            if not((place[0] == '-') or (place == 'Mention')):
                    place = place.split('[[')[1]
                    place = place.split(']]')[0]
            return place
    except:
        raise Exception('No place found')

if __name__ == '__main__':
    baseurl = login()
    print(get_birthplace(baseurl,'Poul Anderson'))
