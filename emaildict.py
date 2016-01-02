# Take histogram and find the largest sample


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
highest = 0

for line in handle:
    if not line.startswith("From:") : continue
    subsplit = line.split()
    sender = subsplit[1]
    counts[sender] = counts.get(sender,0) + 1
    if counts[sender] > highest:
        bigsender = sender
        highest = counts[sender]

print bigsender, highest
