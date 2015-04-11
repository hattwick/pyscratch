'''
Test cycle from textbook exercises
Discard at any time
'''

print  ("Test code")

f = open ('redisdoc.txt','r')

firstline = f.readline()
secondline = f.readline()

print (firstline)
print (secondline)

f.close()
