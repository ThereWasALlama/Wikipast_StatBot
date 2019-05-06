import requests
from bs4 import BeautifulSoup

def login():
    ''' Login the bot and return the base url to be used in future requests'''

    user='StatBot'
    passw='dhbot2019'
    baseurl='http://wikipast.epfl.ch/wikipast/'
    
    payload={'action':'query','format':'json','utf8':'','meta':'tokens','type':'login'}
    r1=requests.post(baseurl + 'api.php', data=payload)
    login_token=r1.json()['query']['tokens']['logintoken']
    payload={'action':'login','format':'json','utf8':'','lgname':user,'lgpassword':passw,'lgtoken':login_token}
    r2=requests.post(baseurl + 'api.php', data=payload, cookies=r1.cookies)
    params3='?format=json&action=query&meta=tokens&continue='
    r3=requests.get(baseurl + 'api.php' + params3, cookies=r2.cookies)
    
    edit_token=r3.json()['query']['tokens']['csrftoken']
    
    edit_cookie=r2.cookies.copy()
    edit_cookie.update(r3.cookies)

    return baseurl
