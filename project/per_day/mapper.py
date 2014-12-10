#!/usr/bin/env python
import sys
import time


def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.split(',')
        if len(line)>1 and line[0]!='medallion':
            yield line

def format(s,precison):
    f_str = '%.'+str(precison)+'f'
    try:
        return f_str% float(s)
    except Exception,e:
        return '0.00'

def mapper():
    agg = {}
    for line in parseInput():
        pickup_time = time.strptime(line[5], '%Y-%m-%d %H:%M:%S')
        pickup_day = pickup_time.tm_yday
        dropoff_time = time.strptime(line[6], '%Y-%m-%d %H:%M:%S')
        dropoff_day = dropoff_time.tm_yday
        agg[pickup_day] = agg.get(pickup_day, 0) + 1
        agg[dropoff_day] = agg.get(dropoff_day, 0) + 1
        for item in agg.iteritems():
            print '%s\t%s' % item
        
if __name__ =='__main__':
    mapper()

    
