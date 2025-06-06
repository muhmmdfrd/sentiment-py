from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment using TextBlob.

    Args:
        text (str): The input text.

    Returns:
        tuple: Sentiment (str) and subjectivity (float).
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Polarity is a float between -1 and 1
    subjectivity = float(blob.sentiment.subjectivity)  # Ensure subjectivity is a float

    # Determine sentiment as a string
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, subjectivity