from geopy.distance import vincenty
import load_all_places

def max_distances(dict_all):
    
    return {key:max_distance(value) for key,value in dict_all.items()}

def max_distance(list_locs):
    
    dmax = 0
    bplace = list_locs[0]
    for loc in list_locs:
        dnow = vincenty(bplace,loc).meters
        if(dnow > dmax):
            dmax = dnow
            
    return dmax
    
