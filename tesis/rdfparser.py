__author__ = 'paulhinojosa'
import urllib2

#URI = "http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=6365155"
# URI = "http://dx.doi.org/10.1109/SURV.2012.111412.00045"
# URL = urllib.urlopen(URI)
# print URL.read()

response = urllib2.urlopen('http://dx.doi.org/10.1109/LCN.2009.5355169')
print response.info()
url = response.geturl()
html = response.read()
print url
print html
