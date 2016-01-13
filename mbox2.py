#db1   Using Databases with Python - homework for week 2

import sqlite3
import re



# fname = raw_input('Enter file name: ')
fname = 'mbox-short.txt'
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    orgtemp = re.search("@([\w.]+)",email).group(0)
    orgstring = str(orgtemp)
    org = re.sub('@','', orgstring)
#   org = pieces[1]
    print email
    print org
 

# org = re.search("@([\w.]+)",email).group(0)
#     org = re.findall('@([\w.]+)', email)
