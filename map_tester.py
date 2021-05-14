from json.decoder import JSONDecodeError
import random
import requests
import json

# Coordinates in format (latitude, longitude)
quadrant = [[43.14421196111573, 76.80526294033642],[43.35391130760853, 77.03293833665107]]


for i in range(1000):

    src_lat = random.uniform(quadrant[0][0], quadrant[1][0])
    src_lon = random.uniform(quadrant[0][1], quadrant[1][1])
    dst_lat = random.uniform(quadrant[0][0], quadrant[1][0])
    dst_lon = random.uniform(quadrant[0][1], quadrant[1][1])
    
    osrm_uri = 'http://localhost:5000/route/v1/driving/{},{};{},{}?overview=false&alternatives=4'.format(
        src_lon,
        src_lat,
        dst_lon,
        dst_lat
    )

    brouter_uri = 'http://localhost:17777/brouter?lonlats={},{}|{},{}&profile=car-fast&alternativeidx={}&format=geojson'.format(
        src_lon,
        src_lat,
        dst_lon,
        dst_lat,
        0
    )

    osrm_resp = None
    brouter_resp = None

    try:
        osrm_resp = requests.get(osrm_uri, timeout=1)
        brouter_resp = requests.get(osrm_uri, timeout=1)
    except requests.exceptions.ReadTimeout:
        print('Connection timeout (OSRM freeze)')
        break

    try:
        osrm_resp = json.loads(osrm_resp.text)
        brouter_resp = json.loads(brouter_resp.text)
    except json.JSONDecodeError:
        print('Bad JSON')

    

