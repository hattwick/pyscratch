from xml.etree import ElementTree as ET

tree = ET.parse('data-text.xml')
root = tree.getroot()
# print dir(root)
print '****'
# print list(root)

data = root.find('Data')
print list(data)

for observation in data:
    for item in observation:
        print item
        print item.text
        print list(item)
        print item.attrib

print '*********\n'

all_data=[]

for observation in data:
    record = {}
    for item in observation:
        print item.attrib
