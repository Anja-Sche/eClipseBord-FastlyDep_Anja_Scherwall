from fastapi import FastAPI
from backend.data_processing import df, eclipse_total_time, eclipse_avg_time, century_interval

app = FastAPI()

# Help from AI to set limit to avoid crash
@app.get("/lunar/info")
async def show_data(limit: int = 10):
    return df.head(limit).to_dict(orient="records")

@app.get("/lunar/eclipse_time")
async def eclipse_time():
    return eclipse_total_time().to_dict()


@app.get("/lunar/eclipse_avg_time")
async def avg_eclipse_time():
    return eclipse_avg_time()

@app.get("/lunar/types")
async def eclipse_types():
    return df["Eclipse_Type"].to_dict()

@app.get("/lunar/group_types")
async def eclipse_types():
    return df["Eclipse_Group_Type"].to_dict()


@app.get("/lunar/lunar_amount")
async def amount_of_eclipse():
    return len(df)

@app.get("/lunar/century_limit")
async def century_limit(start, end):
    return century_interval(start, end).to_dict()