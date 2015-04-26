from bs4 import BeautifulSoup as BS
import httplib2
import json
import pprint

class School:
    def __init__(self, id):
        self.id = id
    def __eq__(self, other):
        return self.id == other.id

http = httplib2.Http()

base_url = "http://www.ncschoolreportcard.org/src/"
status, response = http.request(base_url + 'search.jsp?pList=1&pListVal=320')

soup = BS(response)

district_data = {}
school_first_ids = []
school_first = []

years = soup.find(id='yearSelect').find_all('option')[1:]

for option in years:

    year = option.string[0:4]
    url = option._attr_value_as_string('value')

    district_data[year] = {}
    district_data[year]['url'] = url
    status, response = http.request(base_url + url)
    year_soup = BS(response)
    schools = year_soup.find('table',summary="search results").find_all('tr')[1:]
    school_list = []

    for school in schools:

        id = int(school.a.get('href')[-3:])
        name = school.a.text.strip()
        url = school.a.get('href')
        type = school.find_all('td')[3].text.strip()

        school_obj = {}
        school_obj['id'] = id
        school_obj['name'] = name
        school_obj['url'] = url
        school_obj['type'] = type
        school_list.append(school_obj)

        sf_obj = {}
        sf_obj['id'] = id
        sfy_obj = {}
        sfy_obj['year'] = year
        sfy_obj['name'] = name
        sfy_obj['url'] = url
        sfy_obj['type'] = type

        if id in school_first_ids:
            i = school_first_ids.index(id)
        else:
            i = len(school_first_ids)
            school_first_ids.append(id)
            sf_obj['years'] = []
            school_first.append(sf_obj)
        school_first[i]['years'].append(sfy_obj)

    district_data[year]['schools'] = school_list

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(school_first)
#pp.pprint(district_data)
