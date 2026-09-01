from fastapi import FastAPI
from backend.data_processing import df, eclipse_total_time, eclipse_avg_time, century_interval, get_avg_time, get_types, get_group_types, century_amount_eclipse

app = FastAPI()

# Help from AI to set limit to avoid crash
@app.get("/lunar/info")
async def show_data(limit: int = 10):
    return df.head(limit).to_dict(orient="records")

"""First API calls for test of functions and data"""

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
async def eclipse_types():
    return df["Eclipse_Group_Type"].to_dict()


"""API calls built for dashboard"""

@app.get("/lunar/century_limit")
async def century_limit(start, end):
    return century_interval(start, end).to_dict()

@app.get("/lunar/century_avg")
async def century_avg(start, end):
    return get_avg_time(start, end)

@app.get("/lunar/century_types")
async def century_types(start, end):
    return get_types(start, end).to_dict()

@app.get("/lunar/century_group_types")
async def century_group_types(start, end):
    return get_group_types(start, end).to_dict()

@app.get("/lunar/century_lunar_amount")
async def century_amount_of_eclipse(start, end):
    return century_amount_eclipse(start, end)
