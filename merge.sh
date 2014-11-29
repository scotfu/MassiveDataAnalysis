#!/bin/bash
for i in {1..12}
do
   echo 'Merging file '$i 
paste -d, <(cut -d, -f9,10,11,12,13,14 trip_data_$i.csv ) <(cut -d, -f6,9 trip_fare_$i.csv) > trip_$i.csv
done 

