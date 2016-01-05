# Simple JSON transform routine

import json
import pprint

with open('json-raw-in.json') as json_data:
    ping = json.load(json_data)
    json_data.close()

with open('json-transform-to.json') as json_data:
    postform = json.load(json_data)
    json_data.close()

print('inboundjson')
print(ping)
print('\nMaps to new json')
print(postform)

x=type(postform)
print('Type of loaded JSON objects is',x)









'''


{

            "device": "nydc-pod-h-n5k-a-mgmt [Cisco Device]",

            "group": "NYDC-NonProd Data Center",

            "lastvalue": "820 Mbit/s",

            "lastvalue_raw": 102559336.0512,

            "message": "<div class=\"status\">OK<div class=\"moreicon\"></div></div>",

            "message_raw": "OK",

            "objid": 10003,

            "priority": 3,

            "probe": "Probe on AWS : 10.93.152.104",

            "sensor": "(436289536) POD-H-A-FEX161_Uplink1 Traffic",

            "status": "Up",

            "status_raw": 3







{

   "applicationIdentifier":"NonProd Data Center",

   "applicationCodes":[

      "nydc-pod-h...",



   ],

   "name":"NTS Equity",

   "status":"WARNING",

   "dashboardLink":"http://stage:13080/dashboard",

   "nextUpdateSeconds":"60",

   "messages":[

      "Compliance calls are slow",

      "Load balancer instance is offline"

   ]

}

'''