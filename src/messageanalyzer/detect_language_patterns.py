from typing import List, Union, Tuple
from langdetect import detect
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

def detect_language_patterns(messages: List[str], method: str = "language", n: int = 2, top_n: int = 5) -> Union[List[str], List[Tuple[str, int]]]:
    """
    Detects language patterns in a list of messages.

    Parameters
    ----------
    messages : List[str]
        A list of text messages to analyze.

    method : str, default = "language"
        The method to use for pattern detection. Supported methods are:
        - "language": Detects the language of each message.
        - "ngrams": Extracts common n-grams.
        - "char_patterns": Analyzes common character patterns.

    n : int, default = 2
        The 'n' in n-grams, used when method="ngrams".

    top_n : int, default = 5
        The number of top patterns to return.

    Returns
    -------
    Union[List[str], List[Tuple[str, int]]]
        A list of detected patterns based on the chosen method:
        - For "language", a list of detected languages (e.g., ['en', 'fr']).
        - For "ngrams", a list of tuples (ngram, frequency).
        - For "char_patterns", a list of tuples (character, frequency).

    Raises
    ------
    TypeError
        If messages is not a list of strings.
    ValueError
        If method is unsupported.
  
    Examples
    --------
    >>> messages = ["Hello, how are you?", "Bonjour, comment ça va?", "Hola, ¿cómo estás?"]

    Example 1: Detecting languages
    >>> detect_language_patterns(messages, method="language")
    ['en', 'fr', 'es']  # English, French, Spanish

    Example 2: Extracting common 2-grams
    >>> detect_language_patterns(messages, method="ngrams", n=2, top_n=5)
    [('how are', 1), ('are you', 1), ('comment ça', 1), ('ça va', 1), ('cómo estás', 1)]

    Example 3: Analyzing common character patterns
    >>> detect_language_patterns(messages, method="char_patterns", top_n=5)
    [(' ', 8), ('o', 7), ('e', 6), ('a', 5), ('m', 3)]
    """
    if not isinstance(messages, list) or not all(isinstance(msg, str) for msg in messages):
        raise TypeError("messages must be a list of strings")

    if method == "language":
        return [detect(message) for message in messages]

    elif method == "ngrams":
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Parameter 'n' must be a positive integer.")
        vectorizer = CountVectorizer(ngram_range=(n, n))
        ngrams = vectorizer.fit_transform(messages)
        sum_ngrams = ngrams.sum(axis=0)
        ngram_freq = [(word, sum_ngrams[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
        return sorted(ngram_freq, key=lambda x: x[1], reverse=True)[:top_n]

    elif method == "char_patterns":
        all_text = ''.join(messages)
        char_counts = Counter(all_text)
        return char_counts.most_common(top_n)

    else:
        raise ValueError("Unsupported method. Choose from 'language', 'ngrams', or 'char_patterns'.")