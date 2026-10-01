import time
import pandas as pd
from config import ARCHIVE_URL
from src.ingest.smard_client import fetch_json
import json

CITIES = {
    "berlin": (52.52, 13.41),
    "hamburg": (53.55, 9.99),
    "munich": (48.14, 11.58),
    "cologne": (50.94, 6.96),
    "frankfurt": (50.11, 8.68),
}
VARIABLES = [
    "temperature_2m",
    "relative_humidity_2m",
    "cloud_cover",
    "wind_speed_10m",
    "shortwave_radiation",
]

def fetch_city_weather(lat, lon, start_date, end_date):
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ",".join(VARIABLES),
        "timezone": "UTC",
    }
    return fetch_json(ARCHIVE_URL, params=params)

def fetch_all_cities(start_date,end_date,raw_dir):
    responses={}
    for name,(lat,lon) in CITIES.items():
       path=raw_dir/f"weather_{name}.json"
       if path.exists():
           with open(path) as f:
               responses[name]=json.load(f)
           continue
       
       data=fetch_city_weather(lat,lon,start_date,end_date)
       with open(path,"w") as f:
           json.dump(data,f)

       responses[name]=data
       time.sleep(1)
    return responses
