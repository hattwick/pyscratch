import urllib
import xml.etree.ElementTree as ET


url = ('http://python-data.dr-chuck.net/comments_207067.xml')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)

results = tree.findall('comments')
print results
for items in results:
    count = results[0].find('comment').find('count').text
    print count
    print tree.findtext('count')

for  elt in tree.getiterator():
    print "%s: '%s'" % (elt.tag, elt.text.strip())
