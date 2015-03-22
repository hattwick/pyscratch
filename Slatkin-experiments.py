#!/usr/bin/python
# __author__ = 'phil'
# Mostly collection of small style routines
# Slatkin on Helper Functions over complex expressions   March 16,2015

import urllib
import urllib2
import urllib3
import urlparse

from urlparse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)

print "base computation:"
print (repr(my_values))
print
print "Complex Expression forces an integer value and 0 value for Green"

# complex expression
print "green test1"
green = int(my_values.get('red',[''])[0] or 0)
print green
print

# helper function achieves same result, more readable
red = my_values.get('red',[''])
red = int(red[0]) if red[0] else 0
green = my_values.get('green',[''])
green = int(green[0]) if green[0] else 0
print "added functions to recognize blank or false value:"
print('Red:     ',my_values.get('red'))
print('Green    ',green)
print('Opacity  ',my_values.get('opacity'))



