from xml.etree import ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()
print dir(root)
print '****'
print list(root)

data = root.find('')