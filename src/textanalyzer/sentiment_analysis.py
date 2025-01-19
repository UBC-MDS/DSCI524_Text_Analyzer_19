from textblob import TextBlob

def analyze_sentiment(message, model="Default"):
    """
    Analyzes the sentiment of a given message and prints an alert message if it's highly negative.
    
    Parameters:
    ----------
    message: str, the message to analyze.
    
    model: str, the model to use for sentiment analysis. 
           the "Default" model is TextBlob.
    
    Returns:
    ----------
    dict: return sentiment analysis score and its polarity: "positive", "negative" and "neutral".
    """
    threshold = 0.2  # Threshold for considering a message as "highly negative"
    
    results = []  
    
    if not isinstance(message, list):
        raise TypeError("Input message should be a list of strings.")
    
    for m in message:
        if model == "Default":
            blob = TextBlob(m)
            polarity = blob.sentiment.polarity
            result = {
                "message": m,
                "score": polarity
            }
            
            # Check for highly negative message
            if polarity < 0 and abs(polarity) >= threshold:
                print(f"ALERT: Message is highly negative - {m}")
                result["alert"] = True  
            
            # Categorize sentiment
            if polarity > 0:
                result["label"] = "positive"
            elif polarity < 0:
                result["label"] = "negative"
            else:
                result["label"] = "neutral"
            
            results.append(result)
    
        else:
            raise ValueError("Sentiment Analysis model is not recognized. Please use a valid model 'Default'.")
    return results