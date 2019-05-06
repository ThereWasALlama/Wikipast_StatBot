from geopy.geocoders import Nominatim


def get_latlong(city):
    ''' Get the latitude and longitude of the given location name (string), returns a tuple (lat, long)
    may throw an exception if the city is not found after 30s'''

    # Create the geolocator
    geolocator = Nominatim(timeout=30, user_agent='wikipast_statbot')

    location = geolocator.geocode(city)
    if location == None:
        raise Exception('({}) location was not found'.format(city))
    
    return (location.latitude, location.longitude)

if __name__ == '__main__':
    city = 'Paris'
    print('({}) is at {}.'.format(city, get_latlong(city)))
