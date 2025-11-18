from app.model import simple_sentiment


def test_simple_sentiment():
    assert simple_sentiment("good experience") == "positive"
    assert simple_sentiment("bad experience") == "negative"
    assert simple_sentiment("nothing special") == "neutral"
