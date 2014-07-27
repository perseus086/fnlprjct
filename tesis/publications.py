import json
import urllib
import couchdb

server = couchdb.Server('http://localhost:5984/')
try:
    db_publications = server.create('publications')
except:
    db_publications = server['publications']

db_department = server['people']

i = 0
for each_line in db_department.view('people/all'):
    department_prefix = each_line["value"]["department_prefix"]
    print department_prefix

    person_code = each_line["value"]["person"]["value"][50:]
    print person_code

    URI = "http://128.250.202.125:7001/joseki/oracle?query=PREFIX+dc%3A++++%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+rdf%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+rdfs%3A++%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+xsd%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+owl%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+fn%3A++++%3Chttp%3A%2F%2Fwww.w3.org%2F2005%2Fxpath-functions%23%3E%0D%0APREFIX+ouext%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Fuser-def-function%23%3E%0D%0APREFIX+oext%3A++%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Ffunction%23%3E%0D%0APREFIX+ORACLE_SEM_FS_NS%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%23timeout%3D100%2Cqid%3D123%2CSTRICT_DEFAULT%3DF%2CGRAPH_MATCH_UNNAMED%3DT%3E%0D%0APREFIX+fae%3A+%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Fontology%2F%3E%0D%0APREFIX+vivo%3A+%3Chttp%3A%2F%2Fvivoweb.org%2Fontology%2Fcore%23%3E%0D%0APREFIX+bibo%3A+%3Chttp%3A%2F%2Fpurl.org%2Fontology%2Fbibo%2F%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0A+++SELECT+%3Fpublication+%3Fpubtitle+%3Fpubtype+%3FdateValue+%3Fdoi+%3FpageStart+%3FpageEnd+%3Fedition+%3Fisbn13+%3Fvolume+++%0D%0AWhere+%7B+%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+person_code+"%3E+vivo%3AauthorInAuthorship+%3Fauthorship+.%0D%0A+++++++%3Fauthorship+vivo%3AlinkedInformationResource+%3Fpublication+.%0D%0A+++++++%3Fpublication+rdfs%3Alabel+%3Fpubtitle+.+++%0D%0A+++++++%3Fpublication+rdf%3Atype+%3Fpubtype+.+++++++++%0D%0A+++++++%3Fpublication+vivo%3AdateTimeValue+%3FdateTimeValue+.+++++++++%0D%0A+++++++%3FdateTimeValue+vivo%3AdateTime+%3FdateValue+.++++++++++%0D%0A+++++++OPTIONAL+%7B%3Fpublication+bibo%3Adoi+%3Fdoi+%7D++++++++++%0D%0A+++++++OPTIONAL+%7B%3Fpublication+bibo%3ApageStart+%3FpageStart+%7D++++++++++%0D%0A+++++++OPTIONAL+%7B%3Fpublication+bibo%3ApageEnd+%3FpageEnd+%7D++++++++++%0D%0A+++++++OPTIONAL+%7B%3Fpublication+bibo%3Aedition+%3Fedition+%7D++++++++++%0D%0A+++++++OPTIONAL+%7B%3Fpublication+bibo%3Aisbn13+%3Fisbn13+%7D++++++++++%0D%0A+++++++OPTIONAL+%7B%3Fpublication+bibo%3Avolume+%3Fvolume+%7D+++++++++++%0D%0A+++++++FILTER+regex%28%3Fpubtype%2C+%22findanexpert%22%29++++++++++%7D&stylesheet=%2Fjoseki%2Fxml-to-html.xsl&output=json"

    URL = urllib.urlopen(URI)
    json_people = json.loads(URL.read())
    # print json_people
    publication = json_people["results"]["bindings"]
    for each_publication in publication:
        print each_publication
        each_publication.update({"person_code:": person_code})
        # print each_agreement
        db_publications.save(each_publication)
    i+=1
    print i