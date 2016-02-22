# Short function to open and parse mailbox header data by hour

fname = ('mbox-short.txt')
fhand = open(fname)
c = dict()
for line in fhand:
    if not line.startswith('From ') : continue
    pieces = line.split()
    time = pieces[5]
    times = time.split(:)
    hour = times[1]
    c[hour] = c.get(hour,0) + 1

print c

# -30-
