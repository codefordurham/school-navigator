from bs4 import BeautifulSoup as BS
import httplib2
import json
import pprint
import re

http = httplib2.Http()

base_url = "http://www.ncschoolreportcard.org/src/"

def get_string(x):
    return x

def get_integer(x):
    if x == "N/A":
        return -1
    else:
        return int(x)

def p2f(x):
    if x == "N/A":
        return -1
    else:
        return round(float(x.strip('%'))/100, 3)

convert_data = {
        "string" : get_string,
        "integer" : get_integer,
        "percent" : p2f
        }

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
              15: { "key": "", "function": page15 },
              16: { "key": "", "function": page16 },
              17: { "key": "", "function": page17 } }

    for page in range(1,3):
        schoolCode = '304'
        year = '2012-13'
        url = base_url + 'schDetails.jsp?Page=' + str(page) + '&pSchCode=' + schoolCode + '&pLEACode=320&pYear=' + year
        status, response = http.request(url)
        soup = BS(response)
        data[pages[page]['key']] = pages[page]['function'](soup)

    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(data)

def singleHeadTable(rows, type):
    object = {}
    for index in range(0, len(rows[0].find_all('th'))):
        head = rows[0].find_all('th')[index].text.strip()
        body = rows[1].find_all('td')[index].text.strip()
        object[head] = convert_data[type](body)
    return object

def demographicTable(rows, type):
    object = { "sex": {}, "race": {}, "money": {}, "other": {} }
    category = {
            "Male": "sex", "Female": "sex",
            "White": "race", "Black": "race", "Hispanic": "race", "AmericanIndian": "race", "Asian": "race", "PacificIslander": "race", "Multi": "race",
            "E.D.": "money", "N.E.D.": "money",
            "L.E.P.": "other", "Migrant": "other", "Disabilities": "other"
    }
    for index in range(0, len(rows[0].find_all('th'))):
        head = re.sub("Twoor.*", "Multi", rows[0].find_all('th')[index].text.strip().replace("\r\n","").replace(" ","").replace("Students","").replace("with",""), flags=re.DOTALL)
        body = rows[1].find_all('td')[index].text.strip()
        if body != "N/A":
            if head == "All":
                object["All"] = convert_data[type](body)
            else:
                object[category[head]][head] = convert_data[type](body)
    return object

def page1(soup):
    rows = soup.find('table',summary="average class size").find_all('tr')
    return { "avg": singleHeadTable(rows, "integer"),
            "total" : int(soup.find_all('table',summary="school size")[1].find('tr').find_all('td')[1].text.strip()) }

def page2(soup):
    ESEArows = soup.find('table',summary="End-of-Grade Science Tests for ESEA").find_all('tr')
    EOGrows = soup.find('table',summary="percentage of each student group on the North Carolina end-of-grade tests").find_all('tr')
    object = { "ESEA": singleHeadTable(ESEArows, "percent"),
            "EOG": demographicTable(EOGrows, "percent") }
    return object

#    object = { "grades": {}, "groups": { "races": {}, "sexes": {}, "economic": {} } }
#    table = soup.find('table',summary="performance of students in each grade on the ABCs end-of-grade tests")
#    rows = table.find_all('tr')
#    for index in range(0, len(rows[0].find_all('th'))):
#        grade = rows[0].find_all('th')[index].text.strip()
#        size = rows[1].find_all('td')[index].text.strip()
#        object['avg'][grade] = size
#    return object

def page3(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page4(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page5(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page6(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page7(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page8(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page9(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page10(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page11(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page12(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page13(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page14(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page15(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page16(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

def page17(soup):
    rows = soup.find('table',summary="").find_all('tr')
    return { "key": singleHeadTable(rows, "type") }

if __name__=="__main__":
    main()
