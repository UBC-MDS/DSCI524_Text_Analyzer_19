from textblob import TextBlob

def analyze_sentiment(message, model="default"):
    """
    Analyzes the sentiment of a given message and print alert message if it's highly negative
    
    Parameters:
    ----------
    message: str, the message to analyze.
    
    model: str, the model to use for sentiment analysis. 
            "default" model is TextBlob
    
    Returns:
    ----------
    dict: Sentiment score and it's label.
            - For TextBlob and VADER, returns a sentiment label (positive, negative, neutral).
            - For a custom model, returns the custom output.
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
    elif model == "custom":
        from transformers import pipeline
        sentiment_pipeline = pipeline(model)
        sentiment = sentiment_pipeline(message)[0]
        return {"label": sentiment['label'].lower(), "score": sentiment['score']}
    
    # If the model is not recognized
    else:
        raise ValueError("Unknown sentiment model specified. Choose from 'default', 'vader', or 'custom'.")
    