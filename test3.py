#! /usr/bin/python

# Test from Python hardening book - ping sweep

import os
response = os.popen('ping -c 3 10.0.1.1')


networkdevice  = {"Cisco Nexus 2K":"Access", "Cisco Nexux 5K":"Access Switching","Cisco Nexus 7K":"Core Routing", "Cisco Catalyst 4507":"Access Routing", "Cisco Catalyst 6500":"Aggregate Routing"}

print('Enter whether device should be reachable?')
reachable = input()

#  print(networkdevice)

for line in response.readlines():
    print(line)
    # add counter for IPs successfully reached
    # and a list of successful IPs.

# -30-
