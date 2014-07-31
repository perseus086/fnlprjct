import mysql.connector
import thread
from threading import Thread


def save_data(cnex, init, final):
    print 'inside'
    cursor = cnex.cursor()
    for i in range(init,final):
        add_record = ("INSERT INTO Test"
                "(ID, datas)"
                "VALUES ("+str(i)+", 'testhdhdsshshs shshs') ")
        try:
            cursor.execute(add_record)
            cnex.commit()
        except:
            print 'Error saving'


config = {
  'user': 'root',
  'password': 'perseus086',
  'host': '127.0.0.1',
  'database': 'unimelb',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
try:
    # thread.start_new_thread(save_data, (cnx, 300, 400))
    # thread.start_new_thread(save_data, (cnx, 325, 450))
    t1 = Thread(target=save_data,args=(cnx, 300, 400))
    t1.start()
    t2 = Thread(target=save_data,args=(cnx, 300, 400))
    t2.start()
    t2.join()
    t1.join()
except:
    print 'error'



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