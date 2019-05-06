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
            place=lines[1].split('[[')[2]
            found = 0
            for i in range(0,len(place)-1):
                if((place[i] == ']') & (not(found))):
                    place = place[0:i]
                    found = 1
                    break
            
            return place
    except:
        raise Exception('No place found')

if __name__ == '__main__':
    baseurl = login()
    print(get_birthplace(baseurl,'Mario Botta'))
