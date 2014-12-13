#!/usr/bin/python
import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion':
            yield values

            
def point_in_poly(point,poly):
   x = point[0]
   y = point[1]
   # check if point is a vertex
   if (x,y) in poly: return True

   # check if point is on a boundary
   for i in range(len(poly)):
      p1 = None
      p2 = None
      if i==0:
         p1 = poly[0]
         p2 = poly[1]
      else:
         p1 = poly[i-1]
         p2 = poly[i]
      if p1[1] == p2[1] and p1[1] == y and x > min(p1[0], p2[0]) and x < max(p1[0], p2[0]):
         return True
      
   n = len(poly)
   inside = False

   p1x,p1y = poly[0]
   for i in range(n+1):
      p2x,p2y = poly[i % n]
      if y > min(p1y,p2y):
         if y <= max(p1y,p2y):
            if x <= max(p1x,p2x):
               if p1y != p2y:
                  xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
               if p1x == p2x or x <= xints:
                  inside = not inside
      p1x,p1y = p2x,p2y

   if inside: return True
   else: return False    

def mapper():
    agg = {}
    polygon = [[-73.98830652236938,40.74913859730561] ,[-73.98512542247772,40.75359253503799],[-73.98491084575653,40.753490943068066],[-73.98817241191864,40.74907763805909],[-73.98830652236938,40.74913859730561]]# 6th av from 34th to 40th st
    for values in parseInput():
        pickup_location = [float(values[10]), float(values[11])]
        if point_in_poly(pickup_location, polygon):
            print ','.join(values)
            
if __name__ == '__main__':
    mapper()