import pandas as pd


def financial_stress_index():
    df = pd.read_csv("https://www.financialresearch.gov/financial-stress-index/data/fsi.csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    return df