#! /usr/bin/python

import datetime
import time
import json


import math


from pymongo import MongoClient
from flask import g
from . import app



def connect_db():

    """Connects to the specific database."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['project']
    return db


def get_db():

    """Opens a new database connection if there is none yet for the

    current application context.

    """

    if not hasattr(g, 'mongodb'):
        g.mongodb = connect_db()
    return g.mongodb


#@app.teardown_appcontext
def close_db(error):

    """Closes the database again at the end of the request."""

    if hasattr(g, 'mongodb'):
        g.mongodb.close()


def get_trip(start,end):
    db = get_db()
    collection = db['trip']
    start = datetime.datetime(*time.strptime(start, '%Y-%m-%d')[:6])
    end = datetime.datetime(*time.strptime(end, '%Y-%m-%d')[:6])
    count = list(collection.find({'time':{'$gte':start,'$lte':end}},{'_id':0}))
    result = []
    for t in count:
        v_time = t.get('time').strftime('%Y-%m-%d %H:')
        count = int(t.get('count'))
        result.append({'time':v_time, 'count':count})
    return result

def get_area(start,end):
    db = get_db()
    collection = db['polygon']
    start = datetime.datetime(*time.strptime(start, '%Y-%m-%d')[:6])
    end = datetime.datetime(*time.strptime(end, '%Y-%m-%d')[:6])
    count = list(collection.find({'time':{'$gte':start,'$lte':end}},{'_id':0}))
    result = []
    for t in count:
        v_time = t.get('time').strftime('%Y-%m-%d %H:')
        count = int(t.get('count'))
        result.append({'time':v_time, 'count':count})
    return result
    
def get_bar(start,end):
    db = get_db()
    collection = db['bar']
    start = datetime.datetime(*time.strptime(start, '%Y-%m-%d')[:6])
    end = datetime.datetime(*time.strptime(end, '%Y-%m-%d')[:6])
    count = list(collection.find({'time':{'$gte':start,'$lte':end}},{'_id':0}))
    result = []
    for t in count:
        v_time = t.get('time').strftime('%Y-%m-%d %H:')
        count = int(t.get('count'))
        result.append({'time':v_time, 'count':count})
    return result
    


def get_tip(start,end):
    db = get_db()
    collection = db['tip']
    start = datetime.datetime(*time.strptime(start, '%Y-%m-%d')[:6])
    end = datetime.datetime(*time.strptime(end, '%Y-%m-%d')[:6])
    count = list(collection.find({'time':{'$gte':start,'$lte':end}},{'_id':0}))
    result = []
    for t in count:
        v_time = t.get('time').strftime('%Y-%m-%d %H:')
        count = int(t.get('count'))
        result.append({'time':v_time, 'count':count})
    return result
    
def get_temperature(start,end):
    import time
    db = get_db()
    collection = db['weather']
    UTC_OFFSET_TIMEDELTA = datetime.datetime.utcnow() - datetime.datetime.now()
    start = datetime.datetime(*time.strptime(start, '%Y-%m-%d')[:6]) + UTC_OFFSET_TIMEDELTA
    end = datetime.datetime(*time.strptime(end, '%Y-%m-%d')[:6]) + UTC_OFFSET_TIMEDELTA
    temperature = collection.find({'DateUTC': {'$gte': start, '$lte': end}},{'_id':0})
    result = []
    for t in temperature:
        v_time = (t.get('DateUTC') -UTC_OFFSET_TIMEDELTA).strftime('%Y-%m-%d %H:')
        temperature = float(t.get('TemperatureF'))
        if -200< temperature < 200:
            result.append({'time':v_time, 'temperature':temperature})
    return result
