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

    