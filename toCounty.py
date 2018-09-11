import pandas as pd, requests, json

latlng = '41.429351,-73.679427'

def reverse_geocode(latlng):
    result = {}
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={}'
    request = url.format(latlng)
    data = requests.get(request, headers={'Authorization': 'access_token AIzaSyBhhFzQpr2c7gUuMLGenKIRU4QG1STTGB8'}).json()
    #print(data)
    addrLst = []
    if len(data['results']) > 0:
        addrLst = data['results'][0]['address_components']
    for addr in addrLst:
        if addr['types'][0] == 'administrative_area_level_2':
            result = addr['long_name']
    return result

print(reverse_geocode(latlng))

