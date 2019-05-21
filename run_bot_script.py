#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:11:22 2019

@author: LlamaGod
"""

from save_all_birthdata import save_all_birthdata
from save_all_places import save_all_places
from birth_histogram import birth_histogram
from create_map import create_map
from upload_all_figures import upload_all_figures
from add_all_figures import add_all_figures
from login_edit import login_edit
from create_success_file import create_success_file
from get_all_names import get_all_names
from travel_distance_histogram import travel_distance_histogram

# Name of the active database
databasename = 'database.xml'

# Log the bot in
login_obj = login_edit()

# Gather the data
print('Finding all named entities...')
names = get_all_names(login_obj.baseurl, count_limit=2000)
#names = get_all_names(login_obj.baseurl)

print('Saving the name list...')
with open('names.txt', 'w') as f:
    for item in names:
        f.write("%s\n" % item)

print('Getting all birth data...')
save_all_birthdata(names, databasename)

print('Getting all movement information...')
save_all_places(names, databasename)

# Generate the birthdate histogram
print('Generating birth histogram...')
birth_histogram()

print('Generating travel distance distribution...')
travel_distance_histogram()

# Generate the maps
# TODO generate a table of the most popular birth cities
print('Generating maps of birth places....')
create_map()

# UPload the figures to wikipast
print('Uploading the figures to the wikipast page...')
add_all_figures(upload_all_figures(login_obj), login_obj)

# Get the success rate by looking at the quantity of NotFound in the database
print('Creating success rate file...')
create_success_file()