import mysql.connector
import thread
from threading import Thread
import urllib
import couchdb
import json
from multiprocessing.pool import ThreadPool

def save_data(db_key, i, test):
    URL = 'https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper_Keyword?$skip='+str(i)+'&$format=json'
    data = urllib.urlopen(URL).read()
    json_data = json.loads(data)
    print i, '/'
    for each_json in json_data['d']['results']:
        dictionary = each_json
        try:
            del dictionary['__metadata']
        except:
            pass
        # dictionary['_id'] = str(each_json['ID'])
        try:
            db_key.save(dictionary)
        except:
            print 'error saving'

    if json_data['d']['results'] == []:
        print 'CLOSEEEEEE'

db_name = 'mas_paper_keyword'
db_save = 'mas_author_publication'
server = couchdb.Server('http://localhost:5984/')
try:
    db_keywords = server[db_name]
except:
    print 'error connecing to DB'
    exit()
print "Connected to", db_name




try:
    t = []
    j = 0
    res = []
    test = True
    while j < 105245000:
        for i in range(32):
            t.append(Thread(target=save_data, args=(db_keywords, j, test)))
            t[i].start()
            j += 100
        for i in range(32):
            t[i].join()
        t = []
    # t1 = Thread(target=save_data,args=(0,))
    # t1.start()
    # t2 = Thread(target=save_data,args=(100,))
    # t2.start()
    # t2.join()
    # t1.join()

except Exception, text:
    print text



# cursor2 = cnx.cursor()
#
# query = ("SELECT * FROM Test ")
#
# cursor.execute(query)
#
# for data in cursor:
#     print data
#
# cursor.close()
# cnx.close()