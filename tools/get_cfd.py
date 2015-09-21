import requests
import json
import os
import sys
import csv
import time

API_KEY = os.environ['GOOGLE_API_KEY']

def geolocate(address):
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
    
    ret = {}
    for school in r.json():
        if school['eligibility'] == 'assigned':
            if school['preference'] == 'neighborhood':
                pref = 'neighborhood'
            else:
                pref = school['preference_type']
            ret[(school['level'], pref)] = school['name']
            #print('\t'.join([school['level'], school['preference_type'], school['name']]))
    return ret

if __name__ == '__main__':
    writer = csv.writer(sys.stdout)
    writer.writerow(('address','lookup','middle school','high school','elementary school','year round elementary','year round middle school','elementary walk zone','holt easley traditional option'))
    for i, line in enumerate(sys.stdin):
        address = line.strip()
        sys.stderr.write('{} {}'.format(i, address))
        sys.stderr.write('\n')
        loc = geolocate(address + ' durham nc')

        d = get_schools(loc)

        writer.writerow((
            address,
            '',
            d.get(('middle', 'neighborhood'), ''),
            d.get(('high', 'neighborhood'), ''),
            d.get(('elementary', 'neighborhood'), ''),
            d.get(('elementary', 'year round option'), ''),
            d.get(('middle', 'year round option'), ''),
            d.get(('elementary', 'walk zone'), ''),
            '',
        ))
        time.sleep(0.2)
