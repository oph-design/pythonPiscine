import pandas as pd

def load(path: str) -> pd.DataFrame:
    """returns dimensions of Dataset"""
    ds = pd.read_csv(path)
    print(f"Loading dataset of dimension {ds.shape}")
    return ds

print(load("population_total.csv"))
