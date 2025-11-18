def simple_sentiment(text: str) -> str:
    text = text.lower()
    if "good" in text:
        return "positive"
    if "bad" in text:
        return "negative"
    return "neutral"
