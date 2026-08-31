from fastapi import FastAPI
from backend.data_processing import df, eclipse_total_time

app = FastAPI()

# Help from AI to set limit to avoid crash
@app.get("/lunar/info")
async def show_data(limit: int = 10):
    return df.head(limit).to_dict(orient="records")

@app.get("/lunar/eclipse_time")
async def eclipse_time():
    return eclipse_total_time().to_dict()