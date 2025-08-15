from pathlib import Path
import pandas as pd

def load_data(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    df = pd.read_csv(path)
    return df

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={"long": "lon"})
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    return df

def basic_sanity(df: pd.DataFrame) -> None:
    required = {"id","name","rating","address","city","lat","lon"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if not df["rating"].between(0,5).all():
        raise ValueError("Ratings outside 0–5 range.")
    if df[["lat","lon"]].isna().any().any():
        raise ValueError("lat/lon contain NA values, please clean.")

def clean_pipeline(path: str | Path) -> pd.DataFrame:
    df = load_data(path)
    df = standardize_columns(df)
    df = df.dropna(subset=["lat","lon","rating"])
    df["city"] = df["city"].astype(str).str.strip()
    basic_sanity(df)
    return df
