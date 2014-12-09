for i in {1..365};do 
    wget "http://www.wunderground.com/history/airport/KNYC/2013/1/$i/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&format=1" -O $i.csv
done
