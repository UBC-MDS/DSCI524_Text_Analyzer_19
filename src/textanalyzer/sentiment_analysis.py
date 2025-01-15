from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

def analyze_sentiment(message, model="default"):
    """
    Analyzes the sentiment of a given message and print alert message if it's highly negative
    
    Parameters:
    ----------
    message: str, the message to analyze.
    
    model: str, the model to use for sentiment analysis. 
           the "default" model is TextBlob
           the valid model is: "VADER" and "BERT"
    
    Returns:
    ----------
    dict: return sentiment analysis score and it's label using specified model.
    """
    threshold = 0.2
    # Default model using TextBlob
    if model == "default":
        blob = TextBlob(message)
        polarity = blob.sentiment.polarity
        if polarity < 0 and abs(polarity) >= threshold:
            # Print the alert message
            print(f"ALERT: Message: '{message}' is highly negative")
        if polarity > 0:
            return {"label": "positive", "score": polarity}
        elif polarity < 0:
            return {"label": "negative", "score": polarity}
        else:
            return {"label": "neutral", "score": polarity}
    
    # Custom transformer model
    elif model not in ["VADER", "BERT"]:
            # if the model is not recognized, raise value error
            raise ValueError("Sentiment Analysis model is not recognized, please use a valid model")
    else:
        if model == "VADER":
            sentiment_analysis = SentimentIntensityAnalyzer()
        else:
            sentiment_analysis = pipeline("sentiment-analysis")
        sentiment = sentiment_pipeline(message)[0]
        return {"label": sentiment['label'].lower(), "score": sentiment['score']}
    

    