import os
import requests
import json

def get_environ_value(key):
    try:
        value = os.environ[key]
    except KeyError:
         raise KeyError,'Please check your enviroment variable'
    return value


def get_price(s_latitude,s_longitude,end_latitude,end_longitude):
    url = 'https://api.uber.com/v1/estimates/price'

    parameters = {
        'server_token': get_environ_value('UBER_KEY'),
        'start_latitude':s_latitude ,
        'start_longitude':s_longitude,
        'end_latitude': end_latitude,
        'end_longitude':end_longitude,
        
    }

    response = requests.get(url, params=parameters)
    data = json.loads(response.text)
    result = []
    for record in data['prices']:
        if 'Metered' not in record['estimate']:
            result.append((record['display_name'],record['distance'],get_fare(record['estimate'])))

    return result

def get_fare(price_range):
    #sample price range $1-$10
    #assume tip 20%
    print price_range
    print price_range.split('-')
    low, high = price_range.split('-')
    low = float(low[1:])
    high = float(high)
    fare_low = low * (5/6.0)
    fare_high = high * (5/6.0)
    return '$%.2f-%.2f'%(fare_low,fare_high)


if __name__ =='__main__':
    print get_price(40.757977,-73.978165,40.751171,-73.989838)
