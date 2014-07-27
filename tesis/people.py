import json
import urllib
import couchdb

server = couchdb.Server('http://localhost:5984/')
try:
    db_people = server.create('people')
except:
    db_people = server['people']

db_department = server['departments']

for each_line in db_department.view('department/all'):
    department_prefix = each_line["value"]["org"]["value"][50:]
    URI = "http://128.250.202.125:7001/joseki/oracle?query=PREFIX+dc%3A++++%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+rdf%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+rdfs%3A++%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+xsd%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+owl%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+fn%3A++++%3Chttp%3A%2F%2Fwww.w3.org%2F2005%2Fxpath-functions%23%3E%0D%0APREFIX+ouext%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Fuser-def-function%23%3E%0D%0APREFIX+oext%3A++%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Ffunction%23%3E%0D%0APREFIX+ORACLE_SEM_FS_NS%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%23timeout%3D100%2Cqid%3D123%2CSTRICT_DEFAULT%3DF%2CGRAPH_MATCH_UNNAMED%3DT%3E%0D%0APREFIX+fae%3A+%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Fontology%2F%3E%0D%0APREFIX+vivo%3A+%3Chttp%3A%2F%2Fvivoweb.org%2Fontology%2Fcore%23%3E%0D%0APREFIX+bibo%3A+%3Chttp%3A%2F%2Fpurl.org%2Fontology%2Fbibo%2F%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0ASELECT+%3Fperson+%3FpersonLabel+%3FpositionLabel++%3ForgLabel+%3Fvstart+%3Fvend%0D%0AWHERE+%7B%0D%0A+++++++%3Fperson+vivo%3ApersonInPosition+%3Fposition+.%0D%0A+++++++%3Fposition+vivo%3ApositionInOrganization+%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+department_prefix+"%3E.%0D%0A+++++++%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+department_prefix+"%3E+rdfs%3Alabel+%3ForgLabel.%0D%0A+++++++%3Fposition+rdfs%3Alabel+%3FpositionLabel.%0D%0A+++++++%3Fperson+rdfs%3Alabel+%3FpersonLabel%0D%0A+++++++OPTIONAL+%7B%3Fperson+vivo%3AdateTimeInterval+%3FdateTimeInterval.%0D%0A+++++++++++++++++%3FdateTimeInterval+vivo%3Astart+%3FvstartI.%0D%0A+++++++++++++++++%3FvstartI+vivo%3AdateTime+%3Fvstart%0D%0A++++++++++++++++%7D%0D%0A++++++OPTIONAL+%7B%3Fperson+vivo%3AdateTimeInterval+%3FdateTimeInterval.%0D%0A+++++++++++++++++%3FdateTimeInterval+vivo%3Aend+%3FvendI.%0D%0A+++++++++++++++++%3FvendI+vivo%3AdateTime+%3Fvend%0D%0A++++++++++++++++%7D%0D%0A++++++++%7D&stylesheet=%2Fjoseki%2Fxml-to-html.xsl&output=json"
    URL = urllib.urlopen(URI)
    json_people = json.loads(URL.read())
    # print json_people
    people = json_people["results"]["bindings"]
    for each_people in people:
        # print each_people
        each_people.update({"department_prefix": department_prefix})
        print each_people
        db_people.save(each_people)
