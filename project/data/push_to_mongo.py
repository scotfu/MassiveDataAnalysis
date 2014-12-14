#!/usr/bin/python
from pymongo import MongoClient
import datetime

def connect_db():
    client = MongoClient()
    db = client['project']
    return db


def trip():
    db = connect_db()
    collection = db['trip']
    file = open('per_hour.data')
    for line in file:
        line = line.strip().split('\t')
        record = {'time':datetime.datetime.strptime(line[0], '%Y-%m-%d-%H'), 'count' : line[1]}        
        collection.insert(record)


def tip():
    db = connect_db()
    collection = db['tip']
    file = open('tip_per_hour.data')
    for line in file:
        line = line.strip().split('\t')
        record = {'time':datetime.datetime.strptime(line[0], '%Y-%m-%d-%H'), 'count' : line[1]}
        collection.insert(record)

def polygon():
    db = connect_db()
    collection = db['polygon']
    file = open('poly_per_hour.data')
    for line in file:
        line = line.strip().split('\t')
        record = {'time':datetime.datetime.strptime(line[0], '%Y-%m-%d-%H'), 'count' : line[1]}
        collection.insert(record)




if __name__ == '__main__':
    polygon()