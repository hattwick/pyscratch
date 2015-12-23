import urllib
import json
import simplejson
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

info = opener.open(uh)
simplejson.load(info)
