__author__ = 'paulhinojosa'
import urllib
import json

URL = 'https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper_Keyword?$filter=CPaperID%20eq%2056920942&$format=json'

data = urllib.urlopen(URL).read()
print data
json_data = json.loads(data)
print json_data
for each_result in json_data['d']['results']:
    print each_result['KeywordID']
    keyword = json.loads(urllib.urlopen('https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Keyword('+str(each_result['KeywordID'])+')?$format=json').read())
    print keyword
    print keyword['d']['DisplayName']
