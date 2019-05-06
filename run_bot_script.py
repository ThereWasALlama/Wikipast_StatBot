#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:11:22 2019

@author: LlamaGod
"""

from save_all_birthdata import save_all_birthdata
from birth_histogram import birth_histogram
from create_map import create_map
from upload_all_figures import upload_all_figures
from add_all_figures import add_all_figures
from login_edit import login_edit
from create_success_file import create_success_file

# Log the bot in
login_obj = login_edit()

# Gather the data
print('Getting all birth data...')
save_all_birthdata()

# Generate the birthdate histogram
print('Generating birth histogram...')
birth_histogram()

# Generate the maps
print('Generating maps of birth places....')
create_map()

# UPload the figures to wikipast
print('Uploading the figures to the wikipast page...')
add_all_figures(upload_all_figures(login_obj), login_obj)

# Get the success rate by looking at the quantity of NotFound in the database
create_success_file()