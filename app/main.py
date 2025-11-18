from fastapi import FastAPI
from pydantic import BaseModel

from .model import simple_sentiment
from .utils import normalize


app = FastAPI(title="MoodDetector API", version="2.0.0")


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    sentiment: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    cleaned = normalize(payload.text)
    sentiment = simple_sentiment(cleaned)
    return PredictResponse(sentiment=sentiment)
