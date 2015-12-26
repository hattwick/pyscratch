import urllib
import json
import urllib2



url = ('http://python-data.dr-chuck.net/comments_42.json')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data

# Now pull it into JSON

# info = json.loads(data)
# print 'name',info["name"]
# print 'Total Names: ', len(info)

request = urllib2.Request(url)
opener = urllib2.build_opener()
file = opener.open(request)
json = json.loads(file.read())

print 'User count: ', len(json)
for item in json:
    print 'Name', item['name']
    print 'Id', item['id']


