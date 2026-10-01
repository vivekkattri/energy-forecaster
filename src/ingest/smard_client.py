import time
import requests
import json
from config import SMARD_BASE_URL

def fetch_json(url,params=None,retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url,params,timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            if attempt==retries-1:
                raise
            time.sleep(2)

def build_index_url(code):
    return f"{SMARD_BASE_URL}/{code}/DE/index_hour.json"

def build_data_url(code, timestamp):
    return f"{SMARD_BASE_URL}/{code}/DE/{code}_DE_hour_{timestamp}.json"

def fetch_weeks(code, timestamps, out_dir):
    for timestamp in timestamps:
        path = out_dir / f"{code}_{timestamp}.json"
        if path.exists():
            continue
        url = build_data_url(code, timestamp)
        data = fetch_json(url)
        with open(path, "w") as f:
            json.dump(data, f)
        time.sleep(0.5)