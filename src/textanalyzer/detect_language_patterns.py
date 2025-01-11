from langdetect import detect
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

def detect_language_patterns(messages, method="language", n=2, top_n=5):
    """
    Detects language patterns in a list of messages.

    Parameters
    ----------
    messages : list of str
        A list of text messages to analyze.

    method : str, default="language"
        The method to use for pattern detection. Supported methods are:
        - "language": Detects the language of each message.
        - "ngrams": Extracts common n-grams.
        - "char_patterns": Analyzes common character patterns.

    n : int, default=2
        The 'n' in n-grams, used when method="ngrams".

    top_n : int, default=5
        The number of top patterns to return.

    Returns
    -------
    list
        A list of detected patterns based on the chosen method.

    Examples
    --------
    >>> messages = ["Building A Python Package is fun!"]
    >>> detect_language_patterns(messages, method="language")
    ['en']

    >>> detect_language_patterns(messages, method="ngrams", n=2, top_n=3)
    [('building python', 1), ('python package', 1), ('package fun', 1)]
    """
    
   