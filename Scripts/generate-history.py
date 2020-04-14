"""Generate full history
"""

import glob
import pandas as pd

datasets = []

for filename in glob.glob("/tmp/all_versions_exported/*.csv"):
    df = pd.read_csv(filename)
    df["AS_OF"] = filename.split(".")[1]

    if "DIAGNOSIS_DATE" in df.columns:
        df["DATE_OF_INTEREST"] = pd.to_datetime(df["DIAGNOSIS_DATE"])
        df.drop(columns=["DIAGNOSIS_DATE"], inplace=True)

    df["AS_OF"] = pd.to_datetime(df["AS_OF"])
    df["DATE_OF_INTEREST"] = pd.to_datetime(df["DATE_OF_INTEREST"])
    df.set_index("DATE_OF_INTEREST", inplace=True)

    df["Cases/day, 7 day avg"] = df["NEW_COVID_CASE_COUNT"].rolling(window="7D").mean()
    df["Hospitalized/day, 7 day avg"] = df["HOSPITALIZED_CASE_COUNT"].rolling(window="7D").mean()
    df["Deaths/day, 7 day avg"] = df["DEATH_COUNT"].rolling(window="7D").mean()
    datasets.append(df)

df = pd.concat(datasets, sort=True)

df.to_csv("history.csv")
