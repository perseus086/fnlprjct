import json
import urllib
import couchdb

server = couchdb.Server('http://localhost:5984/')
try:
    db_agreement = server.create('agreements')
except:
    db_agreement = server['agreements']

db_department = server['people']

for each_line in db_department.view('people/all'):
    department_prefix = each_line["value"]["department_prefix"]
    print department_prefix

    people_prefix = each_line["value"]["person"]["value"][50:]
    print people_prefix

    URI = "http://128.250.202.125:7001/joseki/oracle?query=PREFIX+dc%3A++++%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+rdf%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+rdfs%3A++%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+xsd%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+owl%3A+++%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+fn%3A++++%3Chttp%3A%2F%2Fwww.w3.org%2F2005%2Fxpath-functions%23%3E%0D%0APREFIX+ouext%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Fuser-def-function%23%3E%0D%0APREFIX+oext%3A++%3Chttp%3A%2F%2Foracle.com%2Fsemtech%2Fjena-adaptor%2Fext%2Ffunction%23%3E%0D%0APREFIX+ORACLE_SEM_FS_NS%3A+%3Chttp%3A%2F%2Foracle.com%2Fsemtech%23timeout%3D100%2Cqid%3D123%3E%0D%0APREFIX+fae%3A+%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Fontology%2F%3E%0D%0APREFIX+vivo%3A+%3Chttp%3A%2F%2Fvivoweb.org%2Fontology%2Fcore%23%3E%0D%0APREFIX+bibo%3A+%3Chttp%3A%2F%2Fpurl.org%2Fontology%2Fbibo%2F%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0ASELECT+%3FpersonLabel+%3Fagreement+%3FagreementLabel+%3Fscheme+%3FschemeLabel+%3ForgLabel+%3FagreementType+%3FsponsorAwardId+%3Fvstart+%3Fvend%0D%0AWHERE%7B+%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F" + people_prefix + "%3E+vivo%3AhasInvestigatorRole+%3Frole.%0D%0A+++++++%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+people_prefix+"%3E+rdfs%3Alabel+%3FpersonLabel.%0D%0A+++++++%3Frole+vivo%3AroleContributesTo+%3Fagreement.%0D%0A+++++++%3Fagreement+rdfs%3Alabel+%3FagreementLabel.%0D%0A+++++++%3Fagreement+vivo%3AgrantAwardedBy+%3Forg.%0D%0A+++++++%3Chttp%3A%2F%2Fwww.findanexpert.unimelb.edu.au%2Findividual%2F"+department_prefix+"%3E+rdfs%3Alabel+%3ForgLabel.%0D%0A+++++++%3Fagreement+rdf%3Atype+%3FagreementType.%0D%0A+++++++%3Fagreement+vivo%3AsponsorAwardId+%3FsponsorAwardId.%0D%0A+++++++OPTIONAL+%7B%3Fagreement+vivo%3AdateTimeInterval+%3FdateTimeInterval.%0D%0A+++++++++++++++++%3FdateTimeInterval+vivo%3Astart+%3FvstartI.%0D%0A+++++++++++++++++%3FvstartI+vivo%3AdateTime+%3Fvstart%0D%0A++++++++++++++++%7D%0D%0A++++++OPTIONAL+%7B%3Fagreement+vivo%3AdateTimeInterval+%3FdateTimeInterval.%0D%0A+++++++++++++++++%3FdateTimeInterval+vivo%3Aend+%3FvendI.%0D%0A+++++++++++++++++%3FvendI+vivo%3AdateTime+%3Fvend%0D%0A++++++++++++++++%7D%0D%0A++++++++OPTIONAL+%7B%3Fagreement+fae%3Ascheme+%3Fscheme.%0D%0A++++++++++++++++%3Fscheme+rdfs%3Alabel+%3FschemeLabel%7D%0D%0A++++++++%7D&stylesheet=%2Fjoseki%2Fxml-to-html.xsl&output=json"

    URL = urllib.urlopen(URI)
    json_people = json.loads(URL.read())
    # print json_people
    agreement = json_people["results"]["bindings"]
    for each_agreement in agreement:
        print each_agreement
        # each_agreement.update({"department_prefix:": department_prefix})
        # print each_agreement
        db_agreement.save(each_agreement)
