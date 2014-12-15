import requests
import json

def get_price(s_latitude,s_longitude,end_latitude,end_longitude):
    url = 'https://api.uber.com/v1/estimates/price'

    parameters = {
        'server_token': 'key',
        'start_latitude':s_latitude ,
        'start_longitude':s_longitude,
        'end_latitude': end_latitude,
        'end_longitude':end_longitude,
        
    }

    response = requests.get(url, params=parameters)
    data = json.loads(response.text)
    result = []
    for record in data['prices']:
        result.append((record['display_name'],record['distance'],record['estimate']))

    return result
if __name__ =='__main__':
    print get_price(40.757977,-73.978165,40.751171,-73.989838)