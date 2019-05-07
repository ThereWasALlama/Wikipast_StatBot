# This script creates a histogram of the birthyear distribution in the database
# from year 0 to the current year as per the datetime library
import numpy as np
import matplotlib.pyplot as plt
from load_birthdays import load_birthdays
from pathlib import Path
import datetime


def birth_histogram():
    ''' Create histograms of the birth distribution of named entities in wikipast and save them '''
    # load all the bday data
    data = load_birthdays()
    
    data_filtered  = list(filter(lambda x : x!='NotFound', data.values()))
    byear = [int(x.split('.')[0]) for x in data_filtered]
    
    create_histogram(byear, 0, 'birthyear_histogram.png')
    create_histogram(byear, 1500, 'birthyear_histogram_recent.png')
    
#    # Histogram is formed only of positive years
#    # Anybody before Jesus does not exist
#    plt.hist(byear,50, (0, datetime.datetime.now().year))
#    plt.title("Yeah of birth distribution of Wikipast entities")
#    plt.xlabel('year')
#    plt.ylabel('count')
#    plt.savefig('figures/birthyear_histogram.png')
    
def create_histogram(data, startyear, savename):
    ''' Create a histogram of the birth distribution of named entities in wikipast '''

    # Histogram is formed only of positive years
    # Anybody before Jesus does not exist
    plt.figure()
    plt.hist(data,50, (startyear, datetime.datetime.now().year))
    plt.title("Birth distribution of Wikipast entities from year {}".format(startyear))
    plt.xlabel('year')
    plt.ylabel('count')
    plt.savefig(Path('figures/') / savename)


if __name__ == '__main__':
    birth_histogram()