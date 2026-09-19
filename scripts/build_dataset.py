from config import RAW_DIR, PROCESSED_DIR, ensure_directories
from src.features.build_dataset import load_all_weeks
ensure_directories()
df = load_all_weeks(RAW_DIR)
df.to_parquet(PROCESSED_DIR / "load.parquet")
print(f"Saved {len(df)} rows to load.parquet")