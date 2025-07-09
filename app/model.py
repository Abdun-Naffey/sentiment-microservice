from transformers import pipeline

# Load pre-trained Hugging Face model
sentiment_pipeline = pipeline("sentiment-analysis")

def predict_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)[0]
    label = result["label"].lower()
    return label
