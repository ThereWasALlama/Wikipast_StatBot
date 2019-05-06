import requests
from bs4 import BeautifulSoup
from login import *

def get_birthdate(baseurl,name):
    result=requests.post(baseurl+'api.php?action=query&titles='+name+'&export&exportnowrap')
    soup=BeautifulSoup(result.text, "lxml")
    code=''
    for primitive in soup.findAll("text"):
        code+=primitive.string
    lines=code.split('*')
    try:
        if '[[Naissance]]' in lines[1]:
            date=lines[1].split(']]')[0]
            date = date.split('[[')[1]
            return date
    except:
        raise Exception('No name found')

if __name__ == '__main__':
    baseurl = login()
    print(get_birthdate(baseurl,'Yuri Gagarin'))
