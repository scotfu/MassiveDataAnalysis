#!/usr/bin/python
import sys
from matplotlib.path import Path

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion':
            yield values
            
def mapper():
    agg = {}
    polygon = [[-73.98830652236938,40.74913859730561] ,[-73.98512542247772,40.75359253503799],[-73.98491084575653,40.753490943068066],[-73.98817241191864,40.74907763805909],[-73.98830652236938,40.74913859730561]]# 6th av from 34th to 40th st
    path = Path(polygon)
    i = 0
    for values in parseInput():
        i += 1
        try:
            pickup_location = [float(values[10]), float(values[11])]
            if path.contains_point(pickup_location):
                print ','.join(values)
        except Exception,e:
            pass#print e,'line at',i,'11',values[11],'12',values[12]
            
if __name__ == '__main__':
    mapper()