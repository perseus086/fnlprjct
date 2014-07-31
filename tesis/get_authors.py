import urllib
import couchdb
import json


db_name = 'mas_authors'

server = couchdb.Server('http://localhost:5984/')
try:
    db_publication = server.create(db_name)
except:
    db_publication = server[db_name]
print "connected to", db_name

value = 0
URL = 'https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Author?$filter=AffiliationID%20eq%2017684&$skip='+ str(value) +'&$format=json'
data = urllib.urlopen(URL).read()
json_data = json.loads(data)
i = 0
while json_data['d']['results'] != []:

    URL = 'https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Author?$filter=AffiliationID%20eq%2017684&$skip='+ str(value) +'&$format=json'
    data = urllib.urlopen(URL).read()
    json_data = json.loads(data)

    for each_json in json_data['d']['results']:
        dictionary = each_json
        try:
            del dictionary['__metadata']
        except:
            pass
        dictionary['_id'] = str(each_json['ID'])
        print i, dictionary
        try:
            db_publication.save(dictionary)
        except:
            print 'error saving'
        i+=1
    value += 100