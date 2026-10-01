from config import RAW_DIR, INTERIM_DIR, ensure_directories
from src.features.load import load_all_weeks
ensure_directories()
df = load_all_weeks(RAW_DIR)
df.to_parquet(INTERIM_DIR / "load.parquet")
print(f"Saved {len(df)} rows to load.parquet")