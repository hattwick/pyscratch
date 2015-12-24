# Read file, use regex to pull all integers and sum
# Work examples informed by Coursera, Using Python to Access Web Data
# Hattwick-style

import re
import urllib

intlist = list()
linetotal = 0


# Takes a line of string integers, convert to int and subtotal
def listsum(numlist):
   sum = 0
   for i in numlist:
        try:
            i=(int(i))
        except ValueError:
            pass
        sum = sum + i
   return sum


hand = open('xmldata.xml')
numlist = list()
for line in hand:
    line = line.rstrip()
    print line
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) <1 : continue
    print(stuff)
    countitup = (listsum(stuff))
    linetotal=linetotal+countitup
    print(linetotal)
 
 # -30- 
