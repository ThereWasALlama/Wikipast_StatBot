#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:27:41 2019

@author: LlamaGod
"""

from os import listdir
from upload_figure import upload_figure
from login_edit import login_edit
from pathlib import Path

def upload_all_figures(login_obj):
    ''' Uploads all the figures in the figures folder to wikipast
        Returns a list of all the pagenames of these figures '''
        
    folder = Path('figures/')
    figure_pagenames = []
    for file in listdir(folder):
        pagename = upload_figure(folder / file, login_obj)
        figure_pagenames.append(pagename)
        
    return figure_pagenames
        
        
        
        
if __name__=='__main__':
    upload_all_figures(login_edit())