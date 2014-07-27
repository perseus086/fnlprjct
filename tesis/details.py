import json
import urllib
import couchdb

server = couchdb.Server('http://localhost:5984/')
try:
    db_details = server.create('details')
except:
    db_details = server['details']

db_department = server['people']

i = 0
for each_line in db_department.view('people/all'):
    department_prefix = each_line["value"]["department_prefix"]
    print department_prefix

    person_code = each_line["value"]["person"]["value"][50:]
    print person_code

    URI = "http://128.250.202.125:7001/joseki/oracle?query=PREFIX+dc%3A++++%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+rdf%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+rdfs%3A++%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+xsd%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+owl%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+fn%3A++++%3Chttp%3A%2F%2Fwww.w3.org%2F2005%2Fxpath-functions%23%3E%0D%0APREFIX+ouext%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Fuser-def-function%23%3E%0D%0APREFIX+oext%3A++%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Ffunction%23%3E%0D%0APREFIX+ORACLE_SEM_FS_NS%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%23timeout%3D100%2Cqid%3D123%2CSTRICT_DEFAULT%3DF%2CGRAPH_MATCH_UNNAMED%3DT%3E%0D%0APREFIX+fae%3A+%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Fontology%2F%3E%0D%0APREFIX+vivo%3A+%3Chttp%3A%2F%2Fvivoweb.org%2Fontology%2Fcore%23%3E%0D%0APREFIX+bibo%3A+%3Chttp%3A%2F%2Fpurl.org%2Fontology%2Fbibo%2F%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0ASELECT+%3FavailableForSup+%3FsupervisorText1+%3FoverviewText1+%3Fwebpage+%3FresearchOverview+%3FhasMediaOnlyContact+%3Femail%0D%0AWhere+%7B%0D%0A++++++++%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E+rdf%3Atype+vivo%3AFacultyMember.%0D%0A+++++++OPTIONAL%7B%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E+fae%3AavailableForSupervision+%3FavailableForSup%7D%0D%0A+++++++OPTIONAL%7B%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E++fae%3AsupervisorText1+%3FsupervisorText1%7D%0D%0A+++++++OPTIONAL%7B%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E++fae%3AoverviewText1+%3FoverviewText1%7D%0D%0A+++++++OPTIONAL%7B%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E++fae%3Awebpage+%3Fwebpage%7D%0D%0A+++++++OPTIONAL%7B%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E++vivo%3AresearchOverview+%3FresearchOverview+%7D%0D%0A+++++++OPTIONAL%7B%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E++fae%3AhasMediaOnlyContact+%3FhasMediaOnlyContact+%7D%0D%0A+++++++OPTIONAL%7B%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E++vivo%3Aemail+%3Femail+%7D%0D%0A++++++++%7D&stylesheet=%2Fjoseki%2Fxml-to-html.xsl&output=json"
    URL = urllib.urlopen(URI)
    json_people = json.loads(URL.read())
    # print json_people
    details = json_people["results"]["bindings"]
    for each_detail in details:
        print each_detail
        # each_agreement.update({"department_prefix:": department_prefix})
        # print each_agreement
        db_details.save(each_detail)
    i+=1
    print i