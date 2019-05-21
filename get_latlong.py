from geopy.geocoders import Nominatim
import time


def get_latlong(city):
    ''' Get the latitude and longitude of the given location name (string), returns a tuple (lat, long)
    may throw an exception if the city is not found after 30s'''

    # Create the geolocator
    time.sleep(1) # Need this to restrict the request rate to 1/s
    geolocator = Nominatim(timeout=30, user_agent='StatBot2')
    
    location = geolocator.geocode(city)

    
    if location == None:
        raise Exception('({}) location was not found'.format(city))
    
    return (location.latitude, location.longitude)

if __name__ == '__main__':
    city = 'Paris'
    print('({}) is at {}.'.format(city, get_latlong(city)))
