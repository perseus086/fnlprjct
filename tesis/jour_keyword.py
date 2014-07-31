file_ = open('data/journal.csv')
lines = file_.readlines()

for line in lines:
    journal = {}
    line_splited = line.split('"')
    journal['_id'] = line_splited[1]
    journal['ShortName'] = line_splited[3]
    journal['FullName'] = line_splited[5]
    journal['Homepage'] = line_splited[7]

    URL = 'http://65.54.113.26/Detail?entitytype=4&searchtype=9&id='+journal['_id']
    html =

