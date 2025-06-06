from typing import Optional
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from textblob import TextBlob

VALID_API_KEY = "yyWq@TAN2j#@j@SCKDjTVqdZxW6N60zJJ4^v2#Y6d7b6C3y!f#0Xx5YBV!NT&mZt"

app = FastAPI()

class SentimentRequest(BaseModel):
  text: str

class SentimentResponse(BaseModel):
  sentiment: str
  subjectivity: float

@app.get("/")
def example_endpoint():
    return {
        "message": "Hello, World!",
        "success": True,
        "data": None
    }

@app.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment_endpoint(
    request_body: SentimentRequest,
    api_key: Optional[str] = Header(None, alias="api-key")
):
    if api_key != VALID_API_KEY: raise HTTPException(status_code=401, detail="Invalid or missing API key.")

    blob = TextBlob(request_body.text)
    polarity = blob.sentiment.polarity 
    subjectivity = float(blob.sentiment.subjectivity)

    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return SentimentResponse(sentiment=sentiment, subjectivity=subjectivity)