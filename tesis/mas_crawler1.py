__author__ = 'paulhinojosa'


import urllib2
import bs4

mas_unimelb_URL = "http://academic.research.microsoft.com/Detail?entitytype=7&searchtype=1&id=17684"

response = urllib2.urlopen(mas_unimelb_URL)

file_ = open("data/mas_uni_1.html", 'w')
file_.write(response.read())
print response.read()
file_.close()