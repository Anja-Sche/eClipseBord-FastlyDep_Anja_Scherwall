import pandas as pd
from backend.constants import DATA_PATH
from clean_data import clean_column_names, extract_year, convert_duration, convert_ecilpse_type, calculate_century #century_name

"""Read and clean data"""
df = pd.read_csv(DATA_PATH / "lunar.csv")
df = clean_column_names(df)
df = extract_year(df)
df = convert_duration(df)
df = convert_ecilpse_type(df)
df = calculate_century(df)
#df["Century"] = df["Century"].apply(century_name)


"""Create functions to use in API calls"""

# Calculate the total time of an eclipse
def eclipse_total_time(df):
    return df["Penumbral_Eclipse_Duration_(m)"] + df["Partial_Eclipse_Duration_(m)"] + df["Total_Eclipse_Duration_(m)"]

# Calculate the average time of the eclipses
def eclipse_avg_time(df):
    total_time = eclipse_total_time(df)
    avg_time = total_time.mean()
    return avg_time

# Choose interval of centuries
def century_interval(start=df["Century_nr"].min(), end=df["Century_nr"].max()):
    start =int(start)
    end = int(end)
    filtered_century = df[df["Century_nr"].between(start, end)]
    return filtered_century

# calculate avg eclipse time in chosen century interval
def get_avg_time(start=df["Century_nr"].min(), end=df["Century_nr"].max()):
    df_filtered = century_interval(start, end)
    return eclipse_avg_time(df_filtered)

# get amount of different types and type groups in chosen century interval
def get_types(start=df["Century_nr"].min(), end=df["Century_nr"].max()):
    df_filtered = century_interval(start, end)
    return df_filtered["Eclipse_Type"].value_counts()

def get_group_types(start=df["Century_nr"].min(), end=df["Century_nr"].max()):
    df_filtered = century_interval(start, end)
    return df_filtered["Eclipse_Group_Type"].value_counts()

# get amount of eclipses in chosen century interval
def century_amount_eclipse(start=df["Century_nr"].min(), end=df["Century_nr"].max()):
    df_filtered = century_interval(start, end)
    return len(df_filtered)