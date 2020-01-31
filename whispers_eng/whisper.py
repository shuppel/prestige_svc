from collections import Counter

def readwords( filename ):
    f = open(filename)
    words = [ line.rstrip() for line in f.readlines()]
    return words

positive = readwords('positive.txt')
negative = readwords('negative.txt')

paragraph = 'this is really bad and in fact awesome. really awesome.'

count = Counter(paragraph.split())

pos = 0
neg = 0
for key, val in count.iteritems():
    key = key.rstrip('.,?!\n') # removing possible punctuation signs
    if key in positive:
        pos += val
    if key in negative:
        neg += val

print pos, neg
