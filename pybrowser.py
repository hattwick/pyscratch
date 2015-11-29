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