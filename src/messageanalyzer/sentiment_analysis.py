from typing import List, Dict, Union
from textblob import TextBlob

def analyze_sentiment(messages: List[str], model: str = "Default")  -> List[Dict[str, Union[str, float, bool]]]:
    """
    This function analyzes the sentiment of a list of given messages 
    and returns the sentiment scores and labels for each messange and prints alert message if it's highly negative.
    
    Parameters
    ----------
    messages: List[str]
        The messages to analyze.
    
    model: str, optional
        The model to use for sentiment analysis. The "Default" model is TextBlob.
    
    Returns
    ----------
    List[Dict[str, Union[str, float, bool]]]
        A list of dictionaries, where each dictionary contains:
        - "messages": The original message.
        - "score": The sentiment polarity score.
        - "label": The sentiment category ("positive", "negative", "neutral").
        - "alert" (optional): True if the message is highly negative.
        Alert will be printed if some messages are highly negative, and these messages will be displayed.

    Raises
    ------
    TypeError
        If `messages` is not a list of strings.
    ValueError
        If an unrecognized sentiment analysis model is provided.

    Example
    ----------
    >>> messages = ["I love this!", "This is terrible."]
    >>> analyze_sentiment(messages, "Default")
    [{'message': 'I love this!', 'score': 0.5, 'label': 'positive'},
     {'message': 'This is terrible.', 'score': -1.0, 'label': 'negative', 'alert': True}]
    """
    threshold = 0.2  # Threshold for considering a message as "highly negative"
    
    results = []  
    
    if not isinstance(messages, list) or not all(isinstance(msg, str) for msg in messages):
        raise TypeError("messages must be a list of strings")
    
    for m in messages:
        if model == "Default":
            blob = TextBlob(m)
            polarity = blob.sentiment.polarity
            result = {
                "message": m,
                "score": polarity
            }
            
            # Check for highly negative messages
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