# test - scratch


import urllib
import xml.etree.ElementTree as ET
from xml.parsers import expat

# Retrieve, print,  and save xml file via urllib

xmlfile = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.xml')
xmlcontent = xmlfile.read()

print xmlcontent

fhand = open('xmldata.xml','w')
fhand.write(xmlcontent)
fhand.close

# Save xml file and conver the data into a tree of nodes

print 'file saved in xmldata.xml ... starting xml tree walk ...'

tree = ET.fromstring(xmlcontent)

# Find all of tehe comment nodes

# -30-