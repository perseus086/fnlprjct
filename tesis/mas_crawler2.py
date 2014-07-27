__author__ = 'paulhinojosa'
from bs4 import BeautifulSoup
import re
import urllib2
import couchdb

def get_number(str):
    return int(re.findall(r'\d+', str)[0])

db_name = 'mas_people'

server = couchdb.Server('http://localhost:5984/')
try:
    db_people = server.create(db_name)
except:
    db_people = server[db_name]

print 'Connecting to DB', db_name

first_page = 'http://academic.research.microsoft.com/Organization/17684/university-of-melbourne'
other_pages = 'http://academic.research.microsoft.com/Detail?entitytype=7&searchtype=1&id=17684&start='
response = urllib2.urlopen(first_page)
html_doc = response.read()
html_doc = open("data/mas_uni_1.html", 'r').read()
soup = BeautifulSoup(html_doc)
actual_value = 3900
summary = soup.find(id='ctl00_MainContent_SearchSummary_divSummary')
final_value = get_number(summary.get_text())
print final_value
prefix = 'ctl00_MainContent_ObjectList_ctl'

rank = actual_value

while actual_value < final_value:
    if actual_value == 0:
        pass
    else:
        URL = other_pages + str((actual_value)+1) +'&end='+ str(actual_value + 100)
        print actual_value, final_value/actual_value
        if final_value-actual_value < 100:
            URL = other_pages + str(actual_value+1) +'&end='+ str(final_value)
        print URL
        response = urllib2.urlopen(URL)
        html_doc = response.read()
        print html_doc
        soup = BeautifulSoup(html_doc)

    for i in range(0, 100):
        person_dict = {}

        actual_number = str(i).zfill(2)
        each_person = soup.find(id=prefix+actual_number+'_divContent')

        print rank, '#'*40
        person_dict['name'] = each_person.find('a').get_text()
        # print each_person.find('a').get_text()
        person_dict['url'] = each_person.find('a').get('href')
        # print each_person.find('a').get('href')
        person_dict['_id'] = str(get_number(each_person.find('a').get('href')))
        person_dict['rank'] = rank

        publication = soup.find(id=prefix+actual_number+'_publication')
        person_dict['publication_number'] = get_number(publication.get_text())
        # print publication.get_text()
        person_dict['publication_url'] = publication.get('href')
        # print publication.get('href')

        citation = soup.find(id=prefix+actual_number+'_citedBy')
        # print citation.get_text()
        person_dict['citation_number'] = get_number(citation.get_text())

        # print citation.get('href')
        person_dict['citation_url'] = citation.get('href')

        try:
            divisions = each_person.find_all('div')
            fields = divisions[1].find_all('a')
            field_array = []
            for field in fields:
                dict_field = {}
                # print field.get_text()
                dict_field['field_label'] = field.get_text()
                # print field.get('href')
                dict_field['field_url'] = field.get('href')
                field_array.append(dict_field)
                del dict_field

            person_dict['fields'] = field_array
            del field_array
        except:
            pass
        print(person_dict)
        try:
            db_people.save(person_dict)
        except:
            print 'already'
        del person_dict
        rank += 1

    actual_value += 100