# Text browser for monitoring, recording and testing
# Work examples informed by Coursera, Using Python to Access Web Data
# Note:

import socket
site = ('csb.stanford.edu')


# Establish connection
mainsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainsock.connect((site,80))

# Request page
mainsock.send(b'GET http://csb.stanford.edu HTTP/1.0\n\n')

while True:
	data = mainsock.recv(512)
	if ( len(data) < 1 ) :
		break
	print(data)

# Close connection
mainsock.close()


# Now simplify with urllib

import urllib.request as urlreq
filehandler = urlreq.urlopen ('http://www.py4info.com/code/romeo.txt')
count = dict()

for line in filehandler:
	words = line.split()
	for word in words:
		count[word] = count.get(word,0) + 1
	print(line.strip())
print('Printing dictionary contents:\n',count)