import pandas as pd
import numpy as np

def clean_column_names(df):
    df.columns = df.columns.str.replace(' ','_')
    return df

# extract year from date
def extract_year(df):
    df["Year"] = df["Calendar_Date"].str.extract(r"^(-?\d{1,4})", expand=False)
    df["Year"] = pd.to_numeric(df["Year"])
    df["Calendar_Date"] = df["Calendar_Date"].str.replace(r"^(-?\d{1,4})", "", regex=True)
    return df

# convert duration to numeric
def convert_duration(df):
    def convert_time(df, column):
        df[column] = df[column].str.replace("-", "0")
        df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)
        return df

    df = convert_time(df, "Partial_Eclipse_Duration_(m)")
    df = convert_time(df, "Total_Eclipse_Duration_(m)")
    return df

# Clarify eclipse types
def convert_ecilpse_type(df):
    df["Eclipse_Group_Type"] = df["Eclipse_Type"].replace({
        "P": "Partial",
        "N": "Penumbral",
        "T": "Total",
        "T+": "Total",
        "T-": "Total",
        "Nx": "Penumbral",
        "Ne": "Penumbral",
        "Nb": "Penumbral"
    })
    df["Eclipse_Type"]  = df["Eclipse_Type"].replace({
        "P": "Partial",
        "N": "Penumbral",
        "T": "Total",
        "T+": "Total (north)",
        "T-": "Total (south)",
        "Nx": "Penumbral (total)",
        "Ne": "Penumbral (end)",
        "Nb": "Penumbral (begin)"
    })
    return df

# Calculate and name century 
def calculate_century(df):
    df["Century"] = np.where(
        df["Year"] > 0,
        np.ceil(df["Year"] / 100),
        np.floor(df["Year"] / 100)
    ).astype(int)
    df["Century_nr"] = df["Century"]
    return df
    
def century_name(century):
    century_str = str(century)
    if century_str in ["11", "12", "13"]:
        suffix = "th"    
    elif century_str[-1] == "1":
        suffix = "st"
    elif century_str[-1] == "2":
        suffix = "nd"
    elif century_str[-1] == "3":
        suffix = "rd"
    else:
        suffix = "th"

    if century < 0:
        return f"{century_str}{suffix} century BCE"
    else:
        return f"{century_str}{suffix} century"