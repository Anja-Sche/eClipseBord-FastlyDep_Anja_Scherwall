import pandas as pd
from backend.constants import DATA_PATH
from clean_data import clean_column_names, extract_year, convert_duration, calculate_century, century_name

df = pd.read_csv(DATA_PATH / "lunar.csv")
df = clean_column_names(df)
df = extract_year(df)
df = convert_duration(df)
df = calculate_century(df)
df["Century"] = df["Century"].apply(century_name)




# Calculate the total time of an eclipse
def eclipse_total_time():
    return df["Penumbral_Eclipse_Duration_(m)"] + df["Partial_Eclipse_Duration_(m)"] + df["Total_Eclipse_Duration_(m)"]

