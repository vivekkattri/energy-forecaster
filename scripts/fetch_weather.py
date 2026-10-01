import pandas as pd
from config import RAW_DIR, INTERIM_DIR, ensure_directories
from src.ingest.weather_client import fetch_all_cities
from src.features.weather_data import weather_frame
ensure_directories()
load = pd.read_parquet(INTERIM_DIR / "load.parquet")
start = load["timestamp"].min().strftime("%Y-%m-%d")
end = load["timestamp"].max().strftime("%Y-%m-%d")
print(f"Fetching weather from {start} to {end}...")

responses = fetch_all_cities(start, end, RAW_DIR)
weather = weather_frame(responses)
weather.to_parquet(INTERIM_DIR / "weather.parquet")
print(f"Saved {len(weather)} rows to weather.parquet")