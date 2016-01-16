fname = ('mbox-short.txt')
fhand = open(fname)

counts = dict()
for line in fhand:
    if not line.startswith('From ') : continue
    pieces = line.split()
    time = pieces[5]
    times = time.split(':')
    hour = times[0]
    counts[hour] = counts.get(hour,0) + 1


lazyorder = sorted(counts.keys())    
    
for key in lazyorder:
    mykey = key
    mycount = counts[key]
    print mykey, mycount
