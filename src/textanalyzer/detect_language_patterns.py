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
    """
    if not isinstance(messages, list) or not all(isinstance(msg, str) for msg in messages):
        raise TypeError("messages must be a list of strings")

    if method == "language":
        return [detect(message) for message in messages]

    elif method == "ngrams":
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