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
            elif school['preference'] == 'traditional calendar option':
                pref = 'traditional calendar option'
            else:
                pref = school['preference_type']
            ret[(school['level'], pref)] = school['name']
        if school['eligibility'] == 'option':
            pref = school['preference']
            if pref in ('priority', 'year round option'):
                ret[(school['level'], pref)] = school['name']


        #print('\t'.join([school['level'], school['preference_type'], school['name']]))
    return ret

MAP = {
    'address': 'address',
    ('middle', 'neighborhood'): 'middle school',
    ('high', 'neighborhood'): 'high school',
    ('elementary', 'neighborhood'): 'elementary school',
    ('elementary', 'year round option'): 'year round elementary',
    ('middle', 'year round option'): 'year round middle school',
    ('secondary', 'year round option'): 'year round middle school',
    ('elementary', 'walk zone'): 'elementary walk zone',
    ('elementary', 'choice zone'): 'elementary choice zone',
    ('elementary', 'priority'): 'elementary priority zone',
    ('elementary', 'traditional calendar option'): 'holt easley traditional option',
}

if __name__ == '__main__':
    fields = ('address', 'lookup', 'middle school', 'high school',
              'elementary school', 'year round elementary',
              'year round middle school', 'elementary walk zone',
              'elementary priority zone',
              'elementary choice zone',
              'holt easley traditional option')
    writer = csv.DictWriter(sys.stdout, fields, extrasaction='ignore')
    writer.writeheader()
    for i, line in enumerate(sys.stdin):
        address = line.strip()
        sys.stderr.write('{} {}'.format(i, address))
        sys.stderr.write('\n')
        if 'durham' in address.lower():
            loc = geolocate(address)
        else:
            loc = geolocate(address + ' durham county nc')

        d = get_schools(loc)
        d['address'] = address
        writer.writerow({MAP[k]: d.get(k, '') for k in d})
        time.sleep(0.2)
