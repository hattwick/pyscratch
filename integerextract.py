# Read file, use regex to pull all integers and sum

import re
import math

datafile = open('data1.txt')
intlist = list()
total_integer = 0

print('\n*** Prechecks ***')
print(total_integer)
# for line in datafile:
#	print(line)

print('\n\n\n *** Beginning extract and sum routine: ***\n')


for line in datafile:
    intextract = re.findall('[0-9]+', line)
    if len(intextract) !=1 : continue
    num = float(intextract[0])
    print(num)
    intlist.append(num)
    

# print('done')