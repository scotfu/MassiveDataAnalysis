#!/usr/bin/python
import sys, time

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion':
            yield values
            
def mapper():
    agg = {}
    for values in parseInput():
        pickup_time = time.strptime(values[5], '%Y-%m-%d %H:%M:%S')
        day = pickup_time.tm_yday
        hour = (day - 1) * 24 + pickup_time.tm_hour
        agg[hour] = agg.get(hour, 0) + 1
        
    for item in agg.iteritems():
        print '%s\t%s' % item
            

if __name__=='__main__':
    mapper()


