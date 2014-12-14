#/usr/bin/bash
#add header
echo "TimeEST,TemperatureF,Dew PointF,Humidity,Sea Level PressureIn,VisibilityMPH,Wind Direction,Wind SpeedMPH,Gust SpeedMPH,PrecipitationIn,Events,Conditions,WindDirDegrees,DateUTC<br />
" >>weather.csv
for i in {1..365};do
   tail $i.csv -n24 >> weather.csv
done
