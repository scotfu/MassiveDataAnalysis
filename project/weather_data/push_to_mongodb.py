#usr/bin/python
from pymongo import MongoClient

def connect_db():
    client = MongoClient()
    db = client['project']
    return db

def insert():
    db = connect_db()
    collection = db['weather']
    error = []
    hour_range = [12] + range(1, 13) + range(1, 12)
    for i in range(1, 2):
        file_name = "%s.csv"%i
        handler = open(file_name)
        hour_no = 0
        for line in handler:
            line = line.split(',')
            if line[0] != '\n' and 'Time' not in line[0]:
                if hour_no <24 and hour_range[hour_no] == int(line[0].split(':')[0]):
                    record = insert_record(line)
                    collection.insert(record)
                    hour_no += 1
        if hour_no != 24:
            error.append((file_name,hour_no))
    print error

def insert_record(line):
    record = {}
    header = 'TimeEST,TemperatureF,Dew PointF,Humidity,Sea Level PressureIn,VisibilityMPH,Wind Direction,Wind SpeedMPH,Gust SpeedMPH,PrecipitationIn,Events,Conditions,WindDirDegrees,DateUTC'.split(',')
    for i in range(len(line)):
        record[header[i]] = line[i]
    return record
    
def is_valid():
    pass




if __name__ == '__main__':
    insert()