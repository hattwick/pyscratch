# Text browser for monitoring, recording and testing
# Work examples informed by Coursera, Using Python to Access Web Data
# Note: Week 4 Homework 1 reading web pages

import urllib
from BeautifulSoup import *
import ssl
import json


url = raw_input('Enter- ')
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext).read()
data = uh.read()

print data



# RESULT


