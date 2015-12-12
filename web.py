# Text browser for monitoring, recording and testing
# Work examples informed by Coursera, Using Python to Access Web Data
# Note: Week 4 Homework 1 reading web pages

import urllib
from BeautifulSoup import BeautifulSoup


# to verify BeautifulSoup version, enter REPL and type:
# print BeautifulSoup.__version__

url = raw_input('Enter- ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')


for tag in tags:
        print tag.get('href',None)


# RESULT



