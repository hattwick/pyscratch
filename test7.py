# test - delete

import re

intlist = list()


def listsum(numlist):
   sum = 0
   for i in numlist:
       sum = sum + i
   return sum


hand = open('data1.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('([0-9]+)', line)
	if len(stuff) <1 : continue
	print(stuff)


#	intlist.append(stuff)


#convert to int
#convertedlist = [];
#for n in intlist:
#	n = int(n[0])
#	convertedlist.append(n)
#print(convertedlist)
#print(listsum(convertedlist))