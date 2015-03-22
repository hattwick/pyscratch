#! /usr/bin/python

# Test from Python hardening book - ping sweep

import os
response = os.popen('ping -c 3 10.0.2.1')
for line in response.readlines():
    print line
