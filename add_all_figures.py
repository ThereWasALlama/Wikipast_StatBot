import urllib.request
import requests
from bs4 import BeautifulSoup
from login_edit import *
from upload_all_figures import *

def add_all_figures(images, obj):
    ''' Add all the figures the statbot stats page on wikipast'''
    
    edit_token = obj.edit_token
    edit_cookie = obj.edit_cookie
    baseurl = obj.baseurl
    summary='StatBot update'
    name = ""
    #content = "[["+name+"]]<br>"+'<div style="display:inline-block;">'+'</div>'
    content = ""
    for img in images:
        content += "[[Fichier: "+ img +"|left]]"
    title = 'statbot_stats'
    #pageToChange = requests.post(baseurl+'api.php?action=query&titles='+title+'&export&exportnowrap')
    payload={'action':'edit','assert':'user','format':'json','utf8':'','text':content,'summary':summary,'title':title,'token':edit_token}
    r4=requests.post(baseurl+'api.php',data=payload,cookies=edit_cookie)
    #print(r4.text)


if __name__ == '__main__':
    obj = login_edit()
    images=upload_all_figures(obj)
    add_all_figures(images, obj)
