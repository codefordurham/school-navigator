from bs4 import BeautifulSoup as BS
import httplib2
import json
import pprint

http = httplib2.Http()

base_url = "http://www.ncschoolreportcard.org/src/"
data = { "size": {} }

for page in range(1,2):
    status, response = http.request(base_url + 'schDetails.jsp?Page=' + str(page) + '&pSchCode=304&pLEACode=320&pYear=2012-2013')
    soup = BS(response)
    data['size']['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    table = soup.find('table',summary="average class size").findChildren()
    header = table[0]
    for grade in header.find('th'):
        data['size'][grade.text.strip()] = grade

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(data)
