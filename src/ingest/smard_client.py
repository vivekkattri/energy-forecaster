import time
import requests
import json
from config import SMARD_BASE_URL

def fetch_json(url):
    response = requests.get(url)
    return response.json()

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