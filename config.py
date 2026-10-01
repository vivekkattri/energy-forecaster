import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
ENTSOE_API_TOKEN = os.environ.get("ENTSOE_API_TOKEN")
SMARD_BASE_URL = "https://www.smard.de/app/chart_data"
ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"
def ensure_directories():
    for directory in [RAW_DIR, INTERIM_DIR, PROCESSED_DIR]:
        directory.mkdir(parents=True, exist_ok=True)