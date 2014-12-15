#!/bin/bash                                                                     
for i in {1..12}
do
   echo 'Merging file '$i
paste -d, <(cat trip_data_$i.csv ) <(cut -d, -f5- trip_fare_$i.csv) > trip_$i.csv
done
