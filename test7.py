# test - scratch


import urllib
import xml.etree.ElementTree as ET
from xml.parsers import expat

# Retrieve, print,  and save xml file via urllib

xmlfile = urllib.urlopen('http://python-data.dr-chuck.net/comments_207067.xml')
xmlcontent = xmlfile.read()

print xmlcontent
length = len(xmlcontent)
print 'Retrieved ', length, ' characters.'

fhand = open('xmldata.xml','w')
fhand.write(xmlcontent)
fhand.close

# Save xml file and conver the data into a tree of nodes

print 'file saved in xmldata.xml ... starting xml tree walk ...'

tree = ET.fromstring(xmlcontent)
print '///Printing tree///'

counts = tree.findall('.//count')
print counts

for  elt in tree.getiterator():
    print "%s: '%s'" % (elt.tag, elt.text.strip())

# Find all of the comment nodes


# -30-