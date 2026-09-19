import pandas as pd 
import json

def load_week(path):
    with open(path) as f:
        data = json.load(f)

    df = pd.DataFrame(data["series"], columns=["timestamp", "load_mw"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

def load_all_weeks(raw_dir, code=410):
    files = sorted(raw_dir.glob(f"{code}_*.json"))
    frames = [load_week(path) for path in files]
    df = pd.concat(frames, ignore_index=True)
    df=df.dropna(subset=["load_mw"])
    df["timestamp"] = df["timestamp"].dt.tz_localize("UTC").dt.tz_convert("Europe/Berlin")
    return df.sort_values("timestamp").reset_index(drop=True)