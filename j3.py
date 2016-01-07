import json
from collections import OrderedDict
import urllib
import request

sampledata = '''
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }'''

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = json.loads(sampledata)
    #data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        for item in js:
          print 'name', item['name']
        continue


print json.dumps(js, indent=4)
print type(js) is dict

total = 0
for item in info:
    print 'Name', item['name']
    print 'Count', item['count']
    total = total + item['count']

print 'Count Total: ', total