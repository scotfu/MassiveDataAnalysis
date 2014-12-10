import sys
import itertools
import operator

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n').split('\t')
        yield line


def reducer():
    print 'time, num_of_trips'
    agg = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        day = int(key)
        count = sum(map(int, zip(*values)[1]))
        print '%s\t%s' % (day, count)

if __name__ == '__main__':
    reducer()