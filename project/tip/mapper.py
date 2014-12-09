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
        tip = float(values[-3])
        fare = float(values[-6])
        if tip >= fare * 0.3:
            print ','.join(values)
            

if __name__=='__main__':
    mapper()


