#!/usr/bin/python
# __author__ = 'phil'
# Mostly collection of small style routines

import urllib

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)

