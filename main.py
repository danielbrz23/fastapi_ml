from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import train, predict, convert

app = FastAPI()

class StockIn(BaseModel):
    ticker: str

class StockOut(StockIn):
    forecast: dict

# routes

@app.get('/ping')
def pong():
    return {"ping":"pong!"}

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail='Model not Found.')
    response_object = {"ticker":ticker, "forecast": convert(prediction_list)}
    return response_object