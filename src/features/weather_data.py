import pandas as pd

def weather_to_frame(data):
    df=pd.DataFrame(data["hourly"])
    df["time"]=pd.to_datetime(df["time"])
    df['time']=df["time"].dt.tz_localize("UTC").dt.tz_convert("Europe/Berlin")
    return df

def weather_frame(respnses):
    frames=[weather_to_frame(r) for r in respnses.values()]
    combined=pd.concat(frames)
    return combined.groupby("time").mean().reset_index()