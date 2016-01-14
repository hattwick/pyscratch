import collections

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

print counts.items()

timeinorder = collections.OrderedDict(sorted(counts.items()))
print timeinorder

lazyorder = sorted(counts.keys())

for key in lazyorder:
    print(key,counts[key])
    mykey = key
    mycount = counts[key]
    print mykey, mycount
