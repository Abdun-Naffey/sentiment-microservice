# app/main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.model import predict_sentiment

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_sentiment(input: TextInput):
    sentiment = predict_sentiment(input.text)
    return {"sentiment": sentiment}
