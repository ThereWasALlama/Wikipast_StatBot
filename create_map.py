# Creat the map for a given array of coordinates

from itertools import chain

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from load_birthplaces import load_birthplaces


def latlongstr2longlat(x):
    y    = x.split(',')
    lat  = float(y[0][1:])
    long = float(y[1][:-1])
    
    return (long, lat)

def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)
    
    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)
    
    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')

def graph_map(data, lonrange, latrange, title, savename):
    ''' Graph a map of given data within a certain range of lattitude longitude, save it as savename'''

    # Create basemap on which to plot everything
    fig = plt.figure(figsize=(8, 6), edgecolor='w')
    m   = Basemap(projection='cyl', resolution=None,
                llcrnrlat=latrange[0], urcrnrlat=latrange[1],
                llcrnrlon=lonrange[0], urcrnrlon=lonrange[1], )
    
    # Add points for each place
    for name, place in data.items():
        
        if place[0]!='NotFound':
    #        print('{} born in {}'.format(name, place))
            x, y = m(*latlongstr2longlat(place[0]))
            
            plt.plot(x, y, 'or', markersize=5)
    #        plt.text(x, y, '{}, {}'.format(name, place[1]), fontsize=12);
    
    
    plt.title(title)
    
    # Draw the finished map
    draw_map(m)
    
    # Save the final figure
    plt.savefig(savename)

def create_map():
    '''Create the map all entries in the database, and bounds on longitude and lat'''
    
    # Get all the birthplaces in the database
    place_data = load_birthplaces()
    
    
    # Create the world map
    graph_map(place_data, [-180, 180], [-90, 90], 'Birth place distribution of Wikipast (world)', 'figures/birthmap_world.png')
    
    # Create map of europe
    graph_map(place_data, [-20, 30], [30, 70], 'Birth place distribution of Wikipast (europe)', 'figures/birthmap_europe.png')

#    # Create map of Switzerland
#    graph_map(place_data, [7, 10], [45, 48], 'Birth place distribution of Wikipast (Switzerland)', 'figures/birthmap_switzerland.png')




    
if __name__ == '__main__':
    create_map()
    
    





