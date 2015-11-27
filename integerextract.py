# Read file, use regex to pull all integers and sum

import re
import math

datafile = open('data1.txt')
total_integer = 0

print('\n*** Prechecks ***')
print(total_integer)
for line in datafile:
	print(line)

print('\n\n\n *** Beginning extract and sum routine: ***\n')


for line in datafile:
	line = line.rstrip()
    # intextract = re.findall('([0-9]+)', line)
    #  print(intextract)

# print('done')