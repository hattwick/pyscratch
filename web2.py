# Text browser for monitoring, recording and testing
# Work examples informed by Coursera, Using Python to Access Web Data
# Note: Week 4 Homework 2 following a url trail

import urllib
from BeautifulSoup import BeautifulSoup
import ssl
import json
import sys

# to verify BeautifulSoup version, enter REPL and type:
# print BeautifulSoup.__version__

url = raw_input('Enter starting URL (http://...): ')
position = input('Enter the position we are looking for:')
repeat = input('Enter number of times to iterate:')
tempurl = url

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

html = urllib.urlopen(url, context=scontext)
soup = html.read()

# Retrieve a list of anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

urllist1=[]      #Initialist

for i in range(1,repeat):
    startposition = 1
    print 'Starting pass #:', startposition, 'Reapeating ', repeat, ' times:'
    while startposition < position:
    	for tag in tags:
        	print tag.get('href',None)
        	urllist1.append(tag.get('href',None))
        	startposition +=1

print '#### done with loop'
print urllist1[3]
url = urllist1[3]


######## T E M P O R A R Y B R E A K #######

sys.exit()

# manual loop
urllist2=[]      #Initialist

for i in range(1,repeat):
    startposition = 1
    print 'Starting pass #:', startposition, 'Reapeating ', repeat, ' times:'
    while startposition < position:
    	for tag in tags:
        	print tag.get('href',None)
        	urllist2.append(tag.get('href',None))
        	startposition +=1

print '#### done with loop'
print urllist2[3]
url = urllist2[3]

# manual loop
urllist3=[]      #Initialist

for i in range(1,repeat):
    startposition = 1
    print 'Starting pass #:', startposition, 'Reapeating ', repeat, ' times:'
    while startposition < position:
    	for tag in tags:
        	print tag.get('href',None)
        	urllist3.append(tag.get('href',None))
        	startposition +=1

print '#### done with loop'
print urllist3[3]
url = urllist3[3]

# manual loop
urllist4=[]      #Initialist

for i in range(1,repeat):
    startposition = 1
    print 'Starting pass #:', startposition, 'Reapeating ', repeat, ' times:'
    while startposition < position:
    	for tag in tags:
        	print tag.get('href',None)
        	urllist4.append(tag.get('href',None))
        	startposition +=1

print '#### done with loop'
print urllist4[3]
url = urllist4[3]

#  print soup
# RESULT



