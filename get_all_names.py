import requests
from bs4 import BeautifulSoup

from login import *

def get_all_names(baseurl):
    '''Returns a list of all of the biography page names'''
##    baseurl = login()

    result=requests.post(baseurl+'api.php?action=query&titles=Biographies&export&exportnowrap')
    soup=BeautifulSoup(result.text, "lxml")
    code=''
    for primitive in soup.findAll("text"):
        code+=primitive.string
    lines=code.split('| [[')
    names=[]
    for i in range(1,len(lines)):
        name=lines[i].split(']]')[0]
        names.append(name)

    return names


if __name__ == '__main__':
    baseurl = login()
    print(get_all_names(baseurl))

