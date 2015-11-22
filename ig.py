# Interating and Generating

import json
import pyperclip

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
