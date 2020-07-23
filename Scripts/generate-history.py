#  -*- coding: utf-8 -*-

"""Generate full history
"""

import glob
import pandas as pd

tmpdir = "all_versions_exported"

datasets = []

for filename in glob.glob(tmpdir + "/*.csv"):
    print(filename)
    df = pd.read_csv(filename)
    df["AS_OF"] = filename.split(".")[1].replace("_", ":")

    df.rename(columns={df.columns[0]: "DATE_OF_INTEREST",
                       "CASE_COUNT": "NEW_COVID_CASE_COUNT",
                       "HOSPITALIZED_COUNT": "HOSPITALIZED_CASE_COUNT"},
              inplace=True)

    df = df.dropna()
    df["AS_OF"] = pd.to_datetime(df["AS_OF"])
    df["DATE_OF_INTEREST"] = pd.to_datetime(df["DATE_OF_INTEREST"])
    df.set_index("DATE_OF_INTEREST", inplace=True)

    df["Cases/day, 7 day avg"] = df["NEW_COVID_CASE_COUNT"].rolling(window="7D").mean()
    df["Hospitalized/day, 7 day avg"] = df["HOSPITALIZED_CASE_COUNT"].rolling(window="7D").mean()
    df["Deaths/day, 7 day avg"] = df["DEATH_COUNT"].rolling(window="7D").mean()
    datasets.append(df)

df = pd.concat(datasets, sort=True)

df.sort_values(["AS_OF", "DATE_OF_INTEREST"], inplace=True)

df.to_csv("history.csv")
