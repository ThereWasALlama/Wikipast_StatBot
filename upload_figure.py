import urllib.request
import requests
from bs4 import BeautifulSoup
from login_edit import *
from pathlib import Path

# upload figure to the fichier page, returns the link to the figure
def upload_figure(filename,obj):

    edit_token = obj.edit_token
    edit_cookie = obj.edit_cookie
    baseurl = obj.baseurl

    upload_file = open(filename,"rb")
    upload_contents = upload_file.read()
    upload_file.close()

    filename = (Path(filename)).name
    
    # setting parameters for upload
    # ref: https://www.mediawiki.org/wiki/API:Upload
    payload={'action':'upload','filename':filename, 'ignorewarnings':1, 'token':edit_token}
    files={'file':upload_contents}

    # upload the image
    print("Uploading file to %s via API..." % (baseurl+"index.php/Fichier:"+filename))
    r4=requests.post(baseurl+'api.php',data=payload,files=files,cookies=edit_cookie)
    return (filename)

    # in case of error print the response
    #print(r4.status_code, r4.reason)

if __name__ == '__main__':
    obj = login_edit()
    filename='G:\\Team Drives\\SHS Digital Humanities\\figures\\birthmap_europe.png'
    upload_figure(filename,obj)


    
