import requests
from bs4 import BeautifulSoup

import json
from urllib.request import urlopen

import re

from login import *

#def get_all_names(baseurl):
#    '''Returns a list of all of the biography page names'''
###    baseurl = login()
#
#    result=requests.post(baseurl+'api.php?action=query&titles=Biographies&export&exportnowrap')
#    soup=BeautifulSoup(result.text, "lxml")
#    code=''
#    for primitive in soup.findAll("text"):
#        code+=primitive.string
#    lines=code.split('| [[')
#    names=[]
#    for i in range(1,len(lines)):
#        name=lines[i].split(']]')[0]
#        names.append(name)
#
#    return names

# TODO fix encoding isue in some of the names
def get_all_names(baseurl, count_limit = None, count_start = 0):
    '''Get all the names based on the Q5 wikidata label, curtesy of the Wikidataficator
        if the count_limit is set then this will only return the count_limit first people
        and interupt the search (usually returns 500 more than count_limit),
        if count_start is specified, then it will start form the given offset'''
    
    count_condition = lambda x: True
    if count_limit != None:
        count_condition = lambda x: x < count_limit
    
    print('Starting name search...')
    
    #get all of the entries that have Q5. We need to while loop since there is a max querry size
    wikidata_limit = 500
    wikidate_offset = count_start
    numberOfItemsToTreat = 1
    joblist = []
    while(numberOfItemsToTreat != 0 and count_condition(len(joblist))):
        print('wikioffset = {}'.format(wikidate_offset))
        
        url = "http://wikipast.epfl.ch/wikipast/api.php?action=query&list=search&srwhat=text&srsearch=Q5&format=json"    
        url = url + "&language=en&srlimit="+str(wikidata_limit)+"&sroffset="+str(wikidate_offset)
        url = urlopen(url)
    
        source = json.load(url)
    
        numberOfItemsToTreat = len(source['query']['search'])
    
        for i in range(numberOfItemsToTreat):
#            if str(source['query']['search'][i]['snippet']).find('wikidata') != -1:
            if re.search('wikidata', str(source['query']['search'][i]['snippet']), re.IGNORECASE):
                title = str(source['query']['search'][i]['title'])
                #print(str(source['query']['search'][i]['title'])+"\n\n")
                joblist.append(title.replace(" ","_"))
        wikidate_offset += wikidata_limit
        
    print('Found {} dudes'.format(len(joblist)))
        
    return joblist
#        return source


if __name__ == '__main__':
    baseurl = login()
    print(get_all_names(baseurl))
#    print(get_all_names_2(baseurl))

