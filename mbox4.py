import re

# name = raw_input("Enter file:")
name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

hour_regex= re.compile(r'(\d\d):')

for line in handle:
    if not line.startswith('From') : continue
    time = line.split('Jan')
    hourfind = hour_regex.search(time)
    hrs = hourfind.group(1) 
    print 'time:', time
    print 'hour:', hrs
    for word in time:
        counts[word] =counts.get(word,0) + 1

print '\nPrinting last time after loop\n'
print time
print '\n now printing counts....'
print counts.items()
