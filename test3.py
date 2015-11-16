#! /usr/bin/python

# Test from Python hardening book - ping sweep

import os
response = os.popen('ping -c 3 10.0.2.1')


etworkdevice  = {"Cisco Nexus 2K":"Access", "Cisco Nexux 5K":"Access Switching","Cisco Nexus 7K":"Core Routing", "Cisco Catalyst 4507":"Access Routing", "Cisco Catalyst 6500":"Aggregate Routing"}

#  print(networkdevice)

for line in response.readlines():
    print(line)

# -30-
