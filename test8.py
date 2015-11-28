# test - delete
# refining test 7 to include elements which are not making it into the converted list

import re

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


hand = open('data1.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) <1 : continue
    print(stuff)
    countitup = (listsum(stuff))
    linetotal=linetotal+countitup
    print(linetotal)
    intlist.append(stuff)


#convert to int
#print('Stuff before we change it:\n', stuff)
convertedlist = [];
for n in intlist:
    n = int(n[0])
    convertedlist.append(n)
print(convertedlist)
print(listsum(convertedlist))