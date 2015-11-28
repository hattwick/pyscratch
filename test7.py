# test - delete

import re

hand = open('data1.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('([0-9]+)', line)
	print(stuff)