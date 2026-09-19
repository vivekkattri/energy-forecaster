from config import RAW_DIR, ensure_directories
from src.ingest.smard_client import fetch_json, build_index_url, fetch_weeks

LOAD_CODE = 410
WEEKS_WANTED = 104

ensure_directories()

index = fetch_json(build_index_url(LOAD_CODE))
timestamps = index["timestamps"][-WEEKS_WANTED:]

print(f"Fetching {len(timestamps)} weeks...")
fetch_weeks(LOAD_CODE, timestamps, RAW_DIR)
print("Done.")
