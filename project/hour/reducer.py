#!/usr/bin/env python
import itertools, operator, sys

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    current_day = None
    current_count = 0
    day = None
    for day,count in parseInput():
        try:
            count = int(count)
        except ValueError:
            continue
        if current_day == day:
            current_count += count
        else:
            if current_day:
                print '%s\t%s' % (current_day, current_count)
            current_day = day
            current_count = count
    if current_day == day:
        print '%s\t%s' % (current_day, current_count)        
        
if __name__=='__main__':
    reducer()
