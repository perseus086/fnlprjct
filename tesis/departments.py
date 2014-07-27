import json
import urllib
import couchdb


server = couchdb.Server('http://localhost:5984/')
try:
    db = server.create('departments')
except:
    db = server['departments']


filename = open("data/orgs.json")
json_file = filename.read()

json_data = json.loads(json_file)
line = json_data["results"]["bindings"]

for each_line in line:
    print each_line
    db.save(each_line)