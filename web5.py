# raw html extract and parse

import urllib
import re

sock = urllib.urlopen("http://python-data.dr-chuck.net/comments_207067.html ")
htmlSource = sock.read()
sock.close()
print htmlSource

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



for line in htmlSource:
    #line = line.rstrip()
    stuff = re.findall('<span([0-9]+)', line)
    if len(stuff) <1 : continue
    print('Found ',stuff)
    countitup = (listsum(stuff))
    linetotal=linetotal+countitup
    print(linetotal)
 
