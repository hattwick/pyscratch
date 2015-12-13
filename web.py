# Text browser for monitoring, recording and testing
# Work examples informed by Coursera, Using Python to Access Web Data
# Note: Week 4 Homework 2 following a url trail

import urllib
from BeautifulSoup import BeautifulSoup


# to verify BeautifulSoup version, enter REPL and type:
# print BeautifulSoup.__version__

url = raw_input('Enter starting URL (http://...): ')
position = input('Enter the position we are looking for:')
repeat = input('Enter number of times to iterate:')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

for i in range(1,repeat):
    startposition = 1
    print 'Starting pass #:', startposition, 'Reapeating ', repeat, ' times:'
    while startposition < position:
    	for tag in tags:
        	print tag.get('href',None)
        	startposition +=1


# RESULT



