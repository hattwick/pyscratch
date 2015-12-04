# Text browser for monitoring, recording and testing
# Work examples informed by Coursera, Using Python to Access Web Data
# Note:



import urllib.request as urlreq
filehandler = urlreq.urlopen ('http://www.py4info.com/code/romeo.txt')
count = dict()

for line in filehandler:
	words = line.split()
	for word in words:
		count[word] = count.get(word,0) + 1
	print(line.strip())
print('Printing dictionary contents:\n',count)


# --30--