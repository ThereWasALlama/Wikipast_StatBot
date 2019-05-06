#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:51:32 2019

@author: LlamaGod
"""

import requests
from bs4 import BeautifulSoup
import collections

def login_edit():
    ''' Login the bot and return the tuple (baseuerl, edit_toke, edit_cookie)'''

    user   ='StatBot'
    passw  ='dhbot2019'
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
    
    LoginInfo = collections.namedtuple('LoginInfo', ['baseurl', 'edit_token', 'edit_cookie'])

    return LoginInfo(baseurl=baseurl, edit_token=edit_token, edit_cookie=edit_cookie)

if __name__=='__main__':
    print(login_edit())

