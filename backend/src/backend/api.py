from fastapi import FastAPI
from backend.data_processing import df, eclipse_total_time, eclipse_avg_time, century_interval, get_avg_time, get_types, get_group_types, century_amount_eclipse

app = FastAPI()

# Help from AI to set limit to avoid crash
@app.get("/lunar/info")
async def show_data(limit: int = 10):
    return df.head(limit).to_dict(orient="records")

"""Initial API calls for test of functions and data"""

@app.get("/lunar/eclipse_time")
async def eclipse_time():
    return eclipse_total_time(df).to_dict()

@app.get("/lunar/eclipse_avg_time")
async def avg_eclipse_time():
    return eclipse_avg_time(df)

@app.get("/lunar/types")
async def eclipse_types():
    return df["Eclipse_Type"].to_dict()

@app.get("/lunar/group_types")
async def eclipse_group_types():
    return df["Eclipse_Group_Type"].to_dict()


"""API calls built for dashboard"""
"""All uses input and output for century"""

# Get min and max century for slider
@app.get("/lunar/century_range")
async def century_max_min():
    return {"min": int(df["Century_nr"].min()),
    "max": int(df["Century_nr"].max())}
    
# Show the inbetweens 
@app.get("/lunar/century_limit")
async def century_limit(start, end):
    return century_interval(start, end).to_dict()

# Show avg time for eclipses
@app.get("/lunar/century_avg")
async def century_avg(start, end):
    return get_avg_time(start, end)

# Show amount in the different types
@app.get("/lunar/century_types")
async def century_types(start, end):
    return get_types(start, end).to_dict()

# Show amount in the different type groups
@app.get("/lunar/century_group_types")
async def century_group_types(start, end):
    return get_group_types(start, end).to_dict()

# Show amount of eclipses
@app.get("/lunar/century_lunar_amount")
async def century_amount_of_eclipse(start, end):
    return century_amount_eclipse(start, end)
