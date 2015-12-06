# Text browser for monitoring, recording and testing
# Work examples informed by Coursera, Using Python to Access Web Data
# Note: Week 3 Homework 2 modified search


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data)

mysock.close()






# RESULT

# server:pyscratch phil$ python3 chuck-hw3.py
# b'HTTP/1.1 200 OK\r\nDate: Fri, 04 Dec 2015 04:11:23 GMT\r\nServer: Apache\r\nLast-Modified: Mon, 12 Oct 2015 14:55:29 GMT\r\nETag: "20f7401b-1d3-521e9853a392b"\r\nAccept-Ranges: bytes\r\nContent-Length: 467\r\nCache-Control: max-age=604800, public\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Headers: origin, x-requested-with, content-type\r\nAccess-Control-Allow-Methods: GET\r\nConnection: close\r\nContent-Type: text/plain\r\n\r\nWhy should you learn to write programs?\n\nWriting programs (or programming) is a very creative '
# b'\nand rewarding activity.  You can write programs for \nmany reasons, ranging from making your living to solving\na difficult data analysis problem to having fun to helping\nsomeone else solve a problem.  This book assumes that \neveryone needs to know how to program, and that once \nyou know how to program you will figure out what you want \nto do with your newfound skills.  \n'