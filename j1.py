import urllib
import json



url = ('http://python-data.dr-chuck.net/comments_42.json')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data



for  elt in data.getiterator():
    print "%s: '%s'" % (elt.tag, elt.text.strip())
