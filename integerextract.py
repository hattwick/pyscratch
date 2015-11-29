# Read file, use regex to pull all integers and sum
# Work examples informed by Coursera, Using Python to Access Web Data
# This test failed... Test8.py was submitted instead

import re
import math

datafile = open('data1.txt')
intlist = list()
total_integer = 0

print('\n*** Prechecks ***')
print(total_integer)
#
print('\n\n\n *** Beginning extract and sum routine: ***\n')

for line in datafile:
	line = line.rstrip()
	intextract = re.findall(('[0-9])+', line)
	num = (intextract[0])
	print(num)
	intlist.append(num)

# print(intlist)
	

# print('done')