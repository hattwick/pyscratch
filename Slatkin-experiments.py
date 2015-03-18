#!/usr/bin/python
# __author__ = 'phil'
# Mostly collection of small style routines

import urllib
import urllib2
import urllib3
import urlparse

from urlparse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)

print (repr(my_values))

