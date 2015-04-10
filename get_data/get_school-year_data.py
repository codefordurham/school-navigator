from bs4 import BeautifulSoup as BS
import httplib2
import json
import pprint

http = httplib2.Http()

base_url = "http://www.ncschoolreportcard.org/src/"

def main():
    data = {}
    pages = { 1: { "key": "size", "function": page1 },
              2: { "key": "tests", "function": page2 },
              3: { "key": "", "function": page3 },
              4: { "key": "", "function": page4 },
              5: { "key": "", "function": page5 },
              6: { "key": "", "function": page6 },
              7: { "key": "", "function": page7 },
              8: { "key": "", "function": page8 },
              9: { "key": "", "function": page9 },
              10: { "key": "", "function": page10 },
              11: { "key": "", "function": page11 },
              12: { "key": "", "function": page12 },
              13: { "key": "", "function": page13 },
              14: { "key": "", "function": page14 },
              15: { "key": "", "function": page15 } }

    for page in range(1,2):
        schoolCode = '304'
        year = '2012-13'
        url = base_url + 'schDetails.jsp?Page=' + str(page) + '&pSchCode=' + schoolCode + '&pLEACode=320&pYear=' + year
        status, response = http.request(url)
        soup = BS(response)
        data[pages[page]['key']] = pages[page]['function'](soup)

    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(data)

def page1(soup):
    object = { "avg": {},
               "total" : int(soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()) }
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = int(size)
    return object

def page2(schoolCode, year):
    object = { "grades": {}, "groups": { "races": {}, "sexes": {}, "economic": {} } }
    table = soup.find('table',summary="performance of students in each grade on the ABCs end-of-grade tests")
    rows = table.find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page3(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page4(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page5(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page6(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page7(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page8(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page9(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page10(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page11(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page12(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page13(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page14(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

def page15(schoolCode, year):
    object = { "avg": {} }
    object['total'] = soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()
    rows = soup.find('table',summary="average class size").find_all('tr')
    for index in range(0, len(rows[0].find_all('th'))):
        grade = rows[0].find_all('th')[index].text.strip()
        size = rows[1].find_all('td')[index].text.strip()
        object['avg'][grade] = size
    return object

if __name__=="__main__":
    main()
