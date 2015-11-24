# Interating and Generating

import json
import pyperclip
import re

from pprint import pprint

router_models = ['7010','7018','9372', '5448','3604','2232','6509','4507R+E','1001']

for router in router_models:
    print('Product: ' + router)

# Try it with json input file

data = json.load(open('igdata.json'))

print('Raw data\n',data,'\n')

print('Formatted no spaces data\n')
pprint(data)

print('\nFormatted with spaces data\n')
pprint(data, indent=4, width=40)



# Separate approach using Dictionary


router_dictionary = {'7010': 'Data Center',
					'7018': 'Data Center',
					'9372': 'Data Center', 
					'5448': 'Data Center',
					'3064': 'Data Center',
					'2232': 'Data Center',
					'6509': 'Edge',
					'4507R+E': 'Campus',
					'1001': 'Edge'}


# Display dictionary contents
print('Router Keys')
print('===========')
print(list(router_dictionary.keys()))
print('\n')
print('Dictionary')
print('==========')

for k , v in router_dictionary.items():
	print(k, v)

# Second method - print the tuple

print('\nDictionary in Tuple Form')
print('=======================')
for i in router_dictionary.items():
	print(i)


# Method for checking if key exists

print('\nChecking for older 7200-series routers')
print(str(router_dictionary.get('7200', 0)))	