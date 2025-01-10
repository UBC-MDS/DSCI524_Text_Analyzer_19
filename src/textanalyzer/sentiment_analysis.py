from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(message, model="default"):
    """
    Analyzes the sentiment of a given message.
    
    Parameters:
    ----------
    message: str, the message to analyze.
    
    model: str, the model to use for sentiment analysis. 
            "default" model is TextBlob
    
    Returns:
    ----------
        dict: Sentiment score or label.
            - For TextBlob and VADER, returns a sentiment label (positive, negative, neutral).
            - For a custom model, returns the custom output.
    """
    
    # Default model using TextBlob
    if model == "default":
        blob = TextBlob(message)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            return {"label": "positive", "score": polarity}
        elif polarity < 0:
            return {"label": "negative", "score": polarity}
        else:
            return {"label": "neutral", "score": polarity}
    
    # VADER model
    elif model == "vader":
        analyzer = SentimentIntensityAnalyzer()
        sentiment_score = analyzer.polarity_scores(message)
        if sentiment_score['compound'] > 0.05:
            return {"label": "positive", "score": sentiment_score['compound']}
        elif sentiment_score['compound'] < -0.05:
            return {"label": "negative", "score": sentiment_score['compound']}
        else:
            return {"label": "neutral", "score": sentiment_score['compound']}
    
    # Custom transformer model
    elif model == "custom":
        # Example of using a custom model (e.g., HuggingFace transformers)
        # You can replace this with your own transformer-based model or custom function
        # Here is a placeholder:
        from transformers import pipeline
        sentiment_pipeline = pipeline("sentiment-analysis")
        sentiment = sentiment_pipeline(message)[0]
        return {"label": sentiment['label'].lower(), "score": sentiment['score']}
    
    # If the model is not recognized
    else:
        raise ValueError("Unknown sentiment model specified. Choose from 'default', 'vader', or 'custom'.")