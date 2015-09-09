import requests
import json
import os

API_KEY = os.environ['GOOGLE_API_KEY']

def geolocate(address):
    url = 'https://maps.googleapis.com/maps/api/js/GeocodeService.Search?4s2806 snow hill rd Durham NC&7sES&9sen-US&callback=_xdc_._fwo2zc&token=130444'

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': address,
        'key': API_KEY,
    }
    r = requests.get(url, params=params)
    #print(r)
    #print(json.dumps(r.json(), indent=2))
    
    d = r.json()['results'][0]['geometry']['location']

    return {'latitude': d['lat'], 'longitude': d['lng']}

def get_schools(location):
    url = 'https://schools.codefordurham.com/api/schools/'
    r = requests.get(url, params=location)

    #print(r)
    #print(json.dumps(r.json(), indent=2))
    
    for school in r.json():
        if school['eligibility'] == 'assigned':
            print(school['name'], school['level'], school['eligibility'], school['type'], school['preference_type'])


if __name__ == '__main__':
    import sys

    loc = geolocate(' '.join(sys.argv[1:]) + ' durham nc')
    print(loc)

    get_schools(loc)
